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
    "available": true
}

```
+ Response 400

```json

{
    "username": [
        "This field may not be blank.",
        "Ensure this field has at least 4 characters.",
        "Ensure this field has no more than 24 characters.",
        "This field must be unique."
    ],
    "email": [
        "This field may not be blank.",
        "Enter a valid email address.",
        "This field must be unique."
    ],
    "password": [
        "This field may not be blank.",
        "Ensure this field has at least 8 characters."
    ]
}

```