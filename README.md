# Pearmonie E-Commerce Microservices Architecture

This project consists of two microservices:  
1. **E-commerce Service**: Built with Django, Django REST Framework (DRF) and djangosimpleJWT, providing user registration, login, logout, and product management (CRUD).  
2. **AI Product Recommendation Service**: Built with FastAPI, NumPy,Pandas and sklearn, offering product recommendations product catergory viewed by the user.

## Table of Contents
- [Overview](#overview)
- [Microservices Architecture](#microservices-architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting up E-commerce Service](#setting-up-e-commerce-service)
  - [Setting up Product Recommendation Service](#setting-up-product-recommendation-service)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Overview

This project demonstrates a microservice architecture for an e-commerce platform. It includes user authentication, product management, and product recommendation functionalities. The two services are decoupled with communication via RabbitMQ, ensuring scalability and independent deployment.

## Microservices Architecture

1. **E-commerce Service (Django + DRF)**  
   - Handles user authentication (register, login, logout).
   - Manages products (Create, Read, Update, Delete).
   - Exposes RESTful APIs to interact with user and product data.

2. **Product Recommendation Service (FastAPI + NumPy + Pandas)**  
   - Provides product recommendations based on user data.
   - Uses Pandas for data processing NumPy for numerical operations AND Sklearn for machine learning.
   - Exposes a fast and lightweight API for integrating recommendations into the e-commerce platform.

## Features

### E-commerce Service (Django + DRF)
- **User Authentication**: Registration, Login, and Logout functionalities.
- **Product Management**: Full CRUD (Create, Read, Update, Delete) capabilities for products with relationship with the store and catergory table.
- **Database**: PostgreSQL for storing user and product data and redis for product Cacheing.

### Product Recommendation Service (FastAPI + NumPy + Pandas)
- **Recommendation Engine**: Recommends products based on user viewed product and product catergory
- **Data Handling**: Uses Pandas for processing product datasets and NumPy for fast numerical computations.

## Tech Stack

### E-commerce Service
- **Backend**: Django, Django REST Framework and djangosimpleJWT
- **Database**: PostgreSQL, Redis
- **Containerization**: Docker, Docker Compose

### Product Recommendation Service
- **Backend**: FastAPI
- **Data Processing**: Pandas, NumPy and scikit learn
- **Containerization**: Docker

## Installation

### Prerequisites
- Docker & Docker Compose installed
- Python 3.10+
- PostgreSQL
- Redis

### Setting up E-commerce Service without Docker

1. **Clone the repository**:
   ```bash
   git clone git@github.com:oka4dc/pearmonie_API.git
   cd Ecommerce
   Create a virtual environment and activate it, then install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cd Ecommerce (in the project root directory where the manage.py reside)
   python manage.py makemigrations
   python manage,py migrate
   python manage.py create-groups
   python manage.py createsuperuser

   ```

2. **Create and configure `.env` file**:
   - Add database credentials, secret key, etc., in the `.env` file.
   ```env
   SECRET_KEY=your_secret_key
   DB_NAME=ecommerce_db
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=db
   DB_PORT=5432
   ```

3. **Build and run the service**:
   ```bash
   cd Ecommerce (in the project root directory where the manage.py reside)
   docker-compose up --build
   ```

4. **Run migrations**:
   ```bash
   docker-compose exec web python manage.py migrate
   ```
5. **Run create-groups to manage users access roles**:
   ```bash
   docker-compose exec web python manage.py create-groups
   ```

6. **Create a superuser** (Optional):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

### Setting up Product Recommendation Service

1. **Navigate to the FastAPI service directory**:
   ```bash
   cd Recommendation_service
   ```

2. **Install dependencies**:
   Create a virtual environment and activate it, then install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the service**:
   ```bash
   fastapi run main.py
   ```

Alternatively, you can use Docker:
```bash
docker build -t recommendation_service .
docker run -p 8001:8000 recommendation_service
```

## Usage

### E-commerce Service

- **Registration**:  
   POST `/api/v1/auth/register/`  
   Request Body:
   ```json
   {
     "username": "user",
     "password": "pass123",
     "email": "user@example.com"
   }
   ```

- **Login**:  
   POST `/api/v1/auth/login/`  
   Request Body:
   ```json
   {
     "username": "user",
     "password": "pass123"
   }
   ```

- **Product CRUD**:  
   - GET `/api/v1/products/` (List all products)
   - POST `/api/v1/products/` (Create a new product)
   - GET `/api/v1/products/{id}/` (Retrieve product details)
   - PUT `/api/v1/products/{id}/` (Update product)
   - DELETE `/api/v1/products/{id}/` (Delete product)

### Product Recommendation Service

- **Get Recommendations**:  
   GET `/recommendations/`  
   Query Parameters:
   - `product_id`: The ID of the product for whom to generate recommendations.
   - `top_n`: Number of recommendations to return (default is 5).

Example:
```
GET http://localhost:8001/recommendations/?user_id=123&top_n=5
```

Response:
```json
{
   "product_id": 123,
   "recommendations": [
     {"product_id": 1, "name": "Product 1", "score": 9.5},
     {"product_id": 2, "name": "Product 2", "score": 8.7},
     ...
   ]
}
```

## API Endpoints

### E-commerce Service
| Method | Endpoint                      | Description            |
|--------|-------------------------------|------------------------|
| POST   | `/api/v1/auth/register/`       | Register a new user    |
| POST   | `/api/v1/auth/login/`          | Login a user           |
| POST   | `/api/v1/auth/logout/`         | Logout a user          |
| GET    | `/api/v1/products/`            | List all products      |
| POST   | `/api/v1/products/`            | Create a new product   |
| GET    | `/api/v1/products/{id}/`       | Get product details    |
| PUT    | `/api/v1/products/{id}/`       | Update a product       |
| DELETE | `/api/v1/products/{id}/`       | Delete a product       |

### Product Recommendation Service
| Method | Endpoint            | Description                                |
|--------|---------------------|--------------------------------------------|
| GET    | `/recommendations/`  | Get product recommendations for a user     |

## License
This project is licensed under the MIT License.
