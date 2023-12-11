# /clan/user
### GET
+ Response 200

```json

[
    {
        "id": 1,
        "name": "name",
        "effect_id": 1,
        "users": [
            {
                "id": 1,
                "username": "username",
                "is_active": true
            }
        ]
    }
]

```   
# /clan/user/:id
### GET
+ Response 200

```json

{
    "id": 1,
    "name": "name",
    "effect_id": 1,
    "users": [
        {
            "id": 1,
            "username": "username",
            "is_active": true
        }
    ]
}

```