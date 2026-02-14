# DJANGO JWT AUTH PROJECT

A simple and secure authentication system using Django REST Framework and JWT tokens.

# Features:

- User registration

- Login with access & refresh tokens

- Token refresh

- Logout with token blacklisting

- Protected routes

- Rate limiting

- Postman collection for testing

# Tech Stack

- Python – Backend language

- Django & DRF – Web framework & API tools

- djangorestframework-simplejwt – JWT authentication

- SQLite – Default database

- Postman – API testing & documentation

# Setup

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# API Endpoints

POST /register/ – Create a new user

POST /login/ – Get access & refresh tokens

POST /refresh/ – Refresh access token

POST /logout/ – Logout & blacklist token

Protected endpoints require Authorization: Bearer <access_token> header.

# Author

Built with persistence and learning every day.

## Notes

This project was built for learning purposes and improved based on feedbacks from fellow developers.
Suggestions and improvements are welcomed
- 
