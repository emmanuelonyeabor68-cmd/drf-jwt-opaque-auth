# Secure DRF Authentication API

A Simple authentication API built with **Django Rest Framework** using:

- JWT for access token
- Opaque tokens for refresh
- Refresh token rotation for better security

## What this project does

- Users log in with username and password
- API returns a short lived JWT access token
- API also returns an opaque refresh token
- When access expires, refresh token is used to get new tokens
- Old refresh tokens are revoked automatically

 # Tech Stack

 - Python
 - Django
 - Django Rest Framework
 - SimpleJWT
 - Postman (for testing)

# Endpoints

- 'POST /api/login/' - Login and get tokens
- 'POST /api/refresh/' - Refresh access tokens
- 'GET /api/protected/' - Protected endpoint
- 'POST /api/logout/' - logged out and tokens get deleted

# Logout Endpoint

- Added a logout endpoint to revoke opaque refresh tokens
- when a user logs out, their refresh token is deleted from the database
- Access token will expire manually after their short lifetime
- Ensure that old refresh tokens cannot be reused

## Notes

This project was built for learning purposes and improved based on feedbacks from fellow developers.
Suggestions and improvements are welcomed
- 
