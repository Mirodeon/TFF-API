# /auth/login
### POST
+ Request
```json

{
    "email": "email",
    "password": "password"
}

```
+ Response 200

```json

{
    "refresh": "refresh token",
    "access": "access token",
    "user": {
        "id": 1,
        "username": "username",
        "email": "email",
        "is_active": true
    }
}

```