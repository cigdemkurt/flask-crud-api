# Flask CRUD API

This is a simple RESTful API project built with Flask and PostgreSQL.  
It supports basic CRUD operations for Users, Products, Admins, and Categories.

## Technologies
- Flask
- PostgreSQL
- SQLAlchemy
- Postman

## Project Structure
- User CRUD
- Product CRUD
- Admin CRUD
- Category CRUD

## How to Run
1. Install dependencies:
pip install flask flask_sqlalchemy flask_cors psycopg2

2. Create a PostgreSQL database named `ecommerce`.

3. Configure the database URI inside the project.

4. Run the application:
   
5. Test the API with Postman.

## Endpoints Example
- POST /api/users/add
- GET /api/users/
- PUT /api/users/<id>
- DELETE /api/users/<id>

(Same structure for products, admins, and categories.)
