# /clan/cat
### GET
+ Response 200

```json

[
    {
        "id": 1,
        "name": "name",
        "effect_id": 1,
        "cats": [
            {
                "id": 1,
                "owner": {
                    "id": 1,
                    "username": "username",
                    "is_active": true
                },
                "clan": {
                    "id": 1,
                    "name": "name",
                    "effect_id": 1
                },
                "name": "name",
                "job": "job",
                "lvl": 1,
                "exp": 0,
                "limite_exp": 5,
                "timestamp": "2023-11-24T11:37:59Z",
                "image": "urlImage",
                "origin": {
                    "id": 1,
                    "latitude": 0.5,
                    "longitude": 0.5
                },
                "position": {
                    "id": 1,
                    "latitude": 0.5,
                    "longitude": 0.5
                },
                "alive": true,
                "radius": 50
            }
        ]
    }
]

```   
# /clan/cat/:id
### GET
+ Response 200

```json

{
    "id": 1,
    "name": "name",
    "effect_id": 1,
    "cats": [
        {
            "id": 1,
            "owner": {
                "id": 1,
                "username": "username",
                "is_active": true
            },
            "clan": {
                "id": 1,
                "name": "name",
                "effect_id": 1
            },
            "name": "name",
            "job": "job",
            "lvl": 1,
            "exp": 0,
            "limite_exp": 5,
            "timestamp": "2023-11-24T11:37:59Z",
            "image": "urlImage",
            "origin": {
                "id": 1,
                "latitude": 0.5,
                "longitude": 0.5
            },
            "position": {
                "id": 1,
                "latitude": 0.5,
                "longitude": 0.5
            },
            "alive": true,
            "radius": 50
        }
    ]
}

```