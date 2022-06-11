# API for Food Service

## Predicting food category

-   Endpoint : `food/predict`
-   HTTP Method : `POST`
-   Request Headers :
    -   Accept : `application/json`
-   Request Body :

```json
{
    "food_name": "Nasi goreng",
    "when": "2, 3, 4"
}
```

-   Request Header :
    -   Accept : `application/json`
-   Response Body (Success) :

```json
{
    "status": "success",
    "data": {
        "dinner": {
            "gizi_needed": {
                "energi": 477.8,
                "karbohidrat_total": 91.4,
                "lemak_total": 9.0,
                "protein": 12.9
            },
            "recommended": [
                {
                    "gizi": {
                        "energi": 340.0,
                        "karbohidrat_total": 78.5,
                        "lemak_total": 6.0,
                        "protein": 10.0
                    },
                    "nama_makanan": "la pasta royale cheese bolognese"
                }
            ]
        }
    }
}
```

-   Response Body (Fail) :

```json
{
    "status": "error",
    "message": "Food not exist"
}
```

```json
{
    "status": "Unauthorized",
    "message": "Token is invalid!"
}
```

```json
{
    "status": "error",
    "message": "Server fail"
}
```
