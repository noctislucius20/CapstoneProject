# API for Chat-Bot

## Predicting chat category

-   Endpoint : `bot/chat/predict`
-   HTTP Method : `POST`
-   Request Headers :
    -   Accept : `application/json`
-   Request Body :

```json
{
    "chat_content": "halo"
}
```

-   Request Header :
    -   Accept : `application/json`
-   Response Body (Success) :

```json
{
    "status": "success",
    "data": {
        "predicted_label": "greeting"
    }
}
```

-   Response Body (Fail) :

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
