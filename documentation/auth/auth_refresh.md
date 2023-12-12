# /auth/refresh/
### POST
+ Request
```json

{
    "refresh": "refresh token"
}

```
+ Response 200

```json

{
    "access": "access token"
}

```
+ Response 401

```json

{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}

```