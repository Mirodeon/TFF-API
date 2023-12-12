# /user/data
### GET
+ Headers
   * Authorization: Bearer < access_token > 
+ Response 200

```json

[
    {
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
]

```
# /user/data/{user_id}
### GET
+ Headers
   * Authorization: Bearer < access_token >   
+ Response 200

```json

{
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

```
# /user/data/
### POST
+ Headers
   * Authorization: Bearer < access_token > 
+ Request
```json

{
    "clan_id": 2,
    "animal": "animal",
    "landscape": "landscape",
    "hobby": "hobby"
}

```  
+ Response 201

```json

{
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

```