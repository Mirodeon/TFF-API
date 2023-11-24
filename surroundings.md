# /surroundings?{lat=:Float}&{lon=:Float}
### GET
+ Response 200

```json

{
    "interest_points": [
        {
            "id": 1,
            "latitude": 0.5,
            "longitude": 0.5,
            "interact": [
                {
                    "id": 1,
                    "timestamp": "2023-11-24T12:40:13Z",
                    "is_enabled": true
                }
            ]
        }
    ],
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
            "timestamp": "2023-11-24T11:37:59Z",
            "url": "urlImage",
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
            "interact": [
                {
                    "id": 1,
                    "timestamp": "2023-11-24T12:40:13Z",
                    "is_enabled": true
                }
            ]
        }
    ]
}

```