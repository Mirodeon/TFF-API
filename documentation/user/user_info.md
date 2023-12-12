# /user/info
### GET
+ Headers
   * Authorization: Bearer < access_token > 
+ Response 200

```json

[
    {
        "id": 1,
        "username": "username",
        "is_active": true
    }
]

```
# /user/info/{user_id}
### GET
+ Headers
   * Authorization: Bearer < access_token >   
+ Response 200

```json

{
    "id": 1,
    "username": "username",
    "is_active": true
}

```