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
- 'GET /api/protected/' - Protcted endpoint

## Notes

This project was built for learning purposes and improved based on feedbacks from fellow developers.
Suggestions and improvements are welcomed
- 
- 
