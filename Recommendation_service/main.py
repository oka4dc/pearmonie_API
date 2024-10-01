# main.py
import pika
import json
import asyncpg
from fastapi import FastAPI
from model import recommendation_model  # Import the ML model

app = FastAPI()

DATABASE_URL = "postgresql://username:password@localhost:5432/ecommerce_db"

# Function to get database connection
async def get_database_connection():
    return await asyncpg.connect(DATABASE_URL)

# Function to fetch recommendations (same category products)
async def fetch_recommendations(product_id: int):
    conn = await get_database_connection()
    query = """
        SELECT p.id, p.name, p.price
        FROM products_product p
        WHERE p.category_id = (
            SELECT category_id FROM products_product WHERE id = $1
        ) AND p.id != $1
    """
    recommendations = await conn.fetch(query, product_id)
    await conn.close()
    return recommendations

# Reorder the recommendations using an ML model
def reorder_recommendations(product_id: int, recommendations):
    recommended_product_ids = recommendation_model.recommend(product_id)

    # Sort the fetched recommendations based on the ML model's recommended order
    reordered_recommendations = sorted(
        recommendations, 
        key=lambda x: recommended_product_ids.tolist().index(x['id']) if x['id'] in recommended_product_ids else len(recommended_product_ids)
    )
    return reordered_recommendations

# Send recommendations back to RabbitMQ
def send_recommendations_to_rabbitmq(recommendations, product_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue for recommendations
    channel.queue_declare(queue='recommendations')

    # Create the message
    message = json.dumps({
        'product_id': product_id,
        'recommendations': [dict(rec) for rec in recommendations]
    })

    # Publish message to RabbitMQ
    channel.basic_publish(exchange='', routing_key='recommendations', body=message)

    connection.close()

# Listen for product views from RabbitMQ
def listen_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue for product views
    channel.queue_declare(queue='product_views')

    # Callback function when a message is received
    def callback(ch, method, properties, body):
        data = json.loads(body)
        product_id = data['product_id']
        print(f"Received product view for product: {product_id}")

        # Fetch products in the same category
        recommendations = await fetch_recommendations(product_id)

        # Reorder the recommendations using the ML model
        reordered_recommendations = reorder_recommendations(product_id, recommendations)

        # Send reordered recommendations back to RabbitMQ
        send_recommendations_to_rabbitmq(reordered_recommendations, product_id)

    # Consume messages from the 'product_views' queue
    channel.basic_consume(queue='product_views', on_message_callback=callback, auto_ack=True)

    print('Waiting for product view messages...')
    channel.start_consuming()

@app.on_event("startup")
def startup_event():
    # Start RabbitMQ listener on FastAPI startup
    import threading
    threading.Thread(target=listen_to_rabbitmq).start()

@app.get("/")
async def root():
    return {"message": "Product Recommendation Service"}
