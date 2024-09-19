# E-commerce API

An e-commerce API built with Django and Django REST Framework (DRF) that supports product management, user authentication, and order processing.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Authors and Acknowledgments](#authors-and-acknowledgments)
- [Contact Information](#contact-information)

## Installation

### Prerequisites
- Python 3.11
- Django
- Django REST Framework
- PostgreSQL

### Setup
1. Clone the repository:
    ```mkdir Ecommerce
    git clone git@github.com:oka4dc/pearmonie_API.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ecommerce
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up environment variables:
    - Create a `.env` file in the project root and add your environment variables.

5. Run migrations:
    ```bash
    python manage.py migrate
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints
- **User Authentication**:
    - `/api/auth/register/` - Register a new user
    - `/api/auth/login/` - Log in a user

- **Product Management**:
    - `/api/products/` - List all products
    - `/api/products/<id>/` - Retrieve, update, or delete a specific product

- **Order Processing**:
    - `/api/orders/` - Create a new order
    - `/api/orders/<id>/` - Retrieve order details

### Environment Variables
- `SECRET_KEY` - The secret key for Django.
- `DATABASE_URL` - The database URL for PostgreSQL.

## Features

- User registration and authentication
- Product catalog management
- Order creation and tracking

## API Documentation

### Authentication

#### Register a new user
- **Endpoint**: `/api/auth/register/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
- **Response**:
    ```json
    {
      "id": "integer",
      "username": "string"
    }
    ```

#### Log in a user
- **Endpoint**: `/api/auth/login/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
- **Response**:
    ```json
    {
      "token": "string"
    }
    ```

### Product Management

...

## Testing

To run the tests, use the following command:
```bash
python manage.py test
