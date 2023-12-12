# /user/details
### GET
+ Headers
   * Authorization: Bearer < access_token > 
+ Response 200

```json

[
    {
        "id": 1,
        "username": "username",
        "is_active": true,
        "data": {
            "clan": {
                "id": 2,
                "name": "name",
                "effect_id": 3
            },
            "food": 0,
            "limite_food": 5,
            "lvl": 1,
            "exp": 0,
            "limite_exp": 5,
            "image": "url"
        }
    }
]

```
# /user/details/{user_id}
### GET
+ Headers
   * Authorization: Bearer < access_token >   
+ Response 200

```json

{
    "id": 1,
    "username": "username",
    "is_active": true,
    "data": {
        "clan": {
            "id": 2,
            "name": "name",
            "effect_id": 3
        },
        "food": 0,
        "limite_food": 5,
        "lvl": 1,
        "exp": 0,
        "limite_exp": 5,
        "image": "url"
    }
}

```