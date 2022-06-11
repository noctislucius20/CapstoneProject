# API for Authentication

## Register a new user

-   Endpoint : `/register`
-   HTTP Method : `POST`
-   Request Headers :
    -   Accept : `application/json`
-   Request Body :

```json
{
    "username": "jerryandriantop@gmail.com",
    "password": "secret123",
    "fullName": "Jerry Andrianto Pangaribuan",
    "gender": "Male",
    "date_of_birth": "2000-04-22",
    "height": 173,
    "weight": 60
}
```

-   Request Header :
    -   Accept : `application/json`
-   Response Body (Success) :

```json
{
    "status": "success",
    "message": "New user created",
    "data": {
        "id": "user-Ps9qXx12",
        "username": "jerryandriantop@gmail.com",
        "fullName": "Jerry Andrianto Pangaribuan",
        "gender": "Male",
        "date_of_birth": "2000-04-22",
        "height": 173,
        "weight": 60
    }
}
```

-   Response Body (Fail) :

```json
{
    "status": "error",
    "message": "Server fail"
}
```

## Login a user

-   Endpoint : `/auth/login`
-   HTTP Method : `POST`
-   Request Headers :
    -   Accept : `application/json`
-   Request Body :

```json
{
    "username": "jerryandriantop@gmail.com",
    "password": "secret123"
}
```

-   Request Header :
    -   Accept : `application/json`
-   Response Body (Success) :

```json
{
    "status": "OK",
    "message": "User logged in successfully",
    "data": {
        "id": "user-Ps9qXx12",
        "username": "jerryandriantop@gmail.com",
        "fullName": "Jerry Andrianto Pangaribuan",
        "gender": "Male",
        "date_of_birth": "2000-04-22",
        "height": 173,
        "weight": 60,
        "age": 22,
        "token": "asdakdjhauwdkhKDHQOIdlasdjlnvkznxkcndowidajhfjhufiqdopjpD;aksdaosjdpwuejpoqjfnoialskdjncvijlandklasdna"
    }
}
```

-   Response Body (Fail) :

```json
{
    "status": "Not Found",
    "message": "User not found"
}
```

```json
{
    "status": "Unauthorized",
    "message": "Wrong password"
}
```

```json
{
    "status": "error",
    "message": "Token is missing!"
}
```

```json
{
    "status": "error",
    "message": "Token is invalid!"
}
```

```json
{
    "status": "error",
    "message": "Server fail"
}
```
