# /auth/verification/
### POST
+ Request
```json

{
    "username": "username",
    "email": "email",
    "password": "password"
}

```
+ Response 200

```json

{
    "available": {
        "id": 1,
        "username": "username",
        "email": "email",
        "is_active": false
    }
}

```