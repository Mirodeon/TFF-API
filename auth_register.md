# /auth/register
### POST
+ Request
```json

{
    "username": "username",
    "email": "email",
    "password": "password"
}

```
+ Response 201

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