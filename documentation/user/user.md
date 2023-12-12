# /user
### GET
+ Headers
   * Authorization: Bearer < access_token > 
+ Response 200

```json

[
    {
        "id": 1,
        "username": "username",
        "email": "email",
        "is_active": true
    }
]

```
# /user/{user_id}
### GET
+ Headers
   * Authorization: Bearer < access_token >   
+ Response 200

```json

{
    "id": 1,
    "username": "username",
    "email": "email",
    "is_active": true
}

```