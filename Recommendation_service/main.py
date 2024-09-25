# start project

# recommendation_service.py
import pandas as pd
from fastapi import FastAPI, HTTPException
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import numpy as np
from Recommendation_service.sample_data import products

app = FastAPI()

# Dummy product data (you can replace this with real data from your database)


# Create a TF-IDF vectorizer and a KNN model
vectorizer = TfidfVectorizer(stop_words='english')
knn_model = NearestNeighbors(n_neighbors=3, metric='cosine')

# Train the model using product descriptions
tfidf_matrix = vectorizer.fit_transform(products['description'])
knn_model.fit(tfidf_matrix)

# Function to get product recommendations
def recommend_products(product_id: int):
    # Find the product by ID
    product = products[products['id'] == product_id]
    if product.empty:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_index = products.index[products['id'] == product_id].tolist()[0]

    # Vectorize the product description
    product_vector = tfidf_matrix[product_index]

    # Find the nearest neighbors
    distances, indices = knn_model.kneighbors(product_vector)

    # Exclude the product itself and get the recommended products
    recommended_indices = indices.flatten()[1:]  # Ignore the first match (the product itself)
    recommended_products = products.iloc[recommended_indices]

    return recommended_products.to_dict(orient='records')

# API endpoint to get recommendations for a product by ID
@app.get("/recommendations/{product_id}")
def get_recommendations(product_id: int):
    try:
        recommended_products = recommend_products(product_id)
        return {"recommended_products": recommended_products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))