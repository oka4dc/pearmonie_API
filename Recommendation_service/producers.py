import pika
import json


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
