# Minium

A Medium-like blogging platform built with Django REST Framework.

## Tech Stack
- Django
- Django REST Framework
- PostgreSQL (planned)

## Features Implemented
- User registration
- JWT authentication (login/refresh)
- Protected endpoints

## Post Management System
- Create, read, update, and delete posts (CRUD)
- Automatic slug generation for SEO-friendly URLs
- Unique slug handling to prevent conflicts
- Author assignment handled automatically from authenticated user
### Permission system:
- Public read access
- Authenticated users can create posts
- Only post owners can update or delete posts