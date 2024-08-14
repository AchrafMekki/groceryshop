- api/v1/customer/registration/
    - POST: Register the customer
        - Header
            - Content-Type: `application/jason`
            - Accept: `application/json`
        - Request body
            - Fields
                - username (str)
                    - required `true`, unique `true`
                - first_name (str)
                    - required `false`, default `""`
                - last_name (str)
                    - required `true`
                - password (str)
                    - required `true`
                - email (str)
                    - required `true`, unique `true`
                - address (str)
                    - required `true`
                - phone (str)
                    - required `true`
                - title (str)
                    - required `false`, default `""`
                - birthday (date)
                    - required `false`, default `""`

    ```json
        {
        "username":"maxm",
        "first_name": "Max",
        "last_name": "Mustermann",
        "password": "maxpw2024!",
        "email": "max.mustermann@email.com",
        "address":"Musterstr. 13, 10000 Musterstadt",
        "phone":"+4014516266",
        "title":"Mr."
        "birthday":"1990-01-01"   
        },
     
        
        ```

    Request response
        - Status code: `201 created`
        ```json
        {
            "username":"maxm",
            "first_name":"Max",
            "email":"max.mustermann@email.com",
        }
        ```

        - Status code: `400 invalid input`

        ```json
        {
            "error": "bad_input",
            "detail": "Invalid input for registration"
        }
        ```

- `api/v1/customer/profile/`
    - `GET`: View the customer profile
    - **Header**
        - Authentication `Token`
        - Accept `application/json`
    - **Response**
        - Status code: `200 ok`
        ```json
            {
                ## what do we want to see on homeage
            }

        ```
        - status code: `401` Unauthorized
            ```json
                {
                    "error": "invalid_token",
                    "detail": "Token was not given or has expired"
                }

            ```

- `/api/v1/customer/login/`
    - `POST`: Login customer
        - Request body
        ```json
            {
                "username": "maxm",
                "password": "maxpw2024!"
            }
        ```
        - Response
            - Status code: `202` Accepted
                - Response body
                    ```json
                        {
                            "token": "8383737skksghslslslghhe9393938slslghhslls-3349wiskghhos339slghs",
                            "refresh_token": "hshlh38837lsjghslshghso39398sikgghslhglhi292irkjhgl;shldjtl9hgs"
                        }
                    ```
            - Status code: `400`: Invalid input     

api/v1/product/
    - GET: /product/ list all products

Response Body
    {
        "name":"Banana",
        "image":"img",
        "price":3,
        "description":"this is a banana",
        "brand":"Chiquita",
        "stock":2
        
    },
      {
        "name":"Apple",
        "image":"img",
        "price":2,
        "description":"this is an apple",
        "brand":"Pink Lady",
        "stock":1
        
    },
        {
        "name":"Kiwi",
        "image":"img",
        "price":4,
        "description":"this a kiwi",
        "brand":"Zespri",
        "stock":3
        
        }


    - Request Body