# FastAPI MVC Web Application

This project is a web application built using FastAPI, SQLAlchemy for ORM, and Pydantic for data validation. The application follows the MVC (Model-View-Controller) design pattern and includes functionality for user authentication and post management.

## Features

- User Signup and Login with JWT authentication
- Create, Retrieve, and Delete Posts
- In-memory caching for optimized post retrieval
- Dependency injection for database sessions and authentication
- Extensive data validation using Pydantic models

## Project Structure

/app
/models # SQLAlchemy models
/schemas # Pydantic schemas
/routers # FastAPI route handlers
/services # Business logic and data access
/utils # Utility functions and dependencies
main.py # Application entry point
database.py # Database setup and session management
config.py # Configuration settings


## Installation

### Prerequisites

- Python 3.8+
- MySQL database

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/fastapi-mvc-app.git
    cd fastapi-mvc-app
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Update the `DATABASE_URL` in `database.py` with your MySQL database credentials.

    ```python
    DATABASE_URL = "mysql+aiomysql://user:password@localhost/dbname"
    ```

5. **Run database migrations:**

    Ensure your database is set up with the necessary tables.

    ```bash
    alembic upgrade head
    ```

6. **Start the application:**

    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints

### Authentication

- **Signup**

    ```http
    POST /auth/signup
    ```

    **Request Body:**

    ```json
    {
        "email": "user@example.com",
        "password": "password"
    }
    ```

    **Response:**

    ```json
    {
        "id": 1,
        "email": "user@example.com"
    }
    ```

- **Login**

    ```http
    POST /auth/login
    ```

    **Request Body:**

    ```json
    {
        "email": "user@example.com",
        "password": "password"
    }
    ```

    **Response:**

    ```json
    {
        "access_token": "jwt_token",
        "token_type": "bearer"
    }
    ```

### Posts

- **Add Post**

    ```http
    POST /post/addpost
    ```

    **Request Body:**

    ```json
    {
        "text": "This is a new post"
    }
    ```

    **Headers:**

    ```http
    Authorization: Bearer <access_token>
    ```

    **Response:**

    ```json
    {
        "id": 1,
        "text": "This is a new post"
    }
    ```

- **Get Posts**

    ```http
    GET /post/getposts
    ```

    **Headers:**

    ```http
    Authorization: Bearer <access_token>
    ```

    **Response:**

    ```json
    [
        {
            "id": 1,
            "text": "This is a new post"
        }
    ]
    ```

- **Delete Post**

    ```http
    DELETE /post/deletepost
    ```

    **Request Body:**

    ```json
    {
        "post_id": 1
    }
    ```

    **Headers:**

    ```http
    Authorization: Bearer <access_token>
    ```

    **Response:**

    ```json
    {
        "detail": "Post deleted successfully"
    }
    ```

## Configuration

Update the `config.py` file to customize the application settings such as `SECRET_KEY`, `ALGORITHM`, and `ACCESS_TOKEN_EXPIRE_MINUTES`.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
