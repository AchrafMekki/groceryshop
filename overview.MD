Customer [id, name, email, password, adress, phone]

Product Index[id, name, description, price, quantity, image]

Customer adds to Cart

orders -> combines customer id + product id into order [id, quantity, status]



## Step 1
### Define a mission statement
- Maintain an easy to use online store, investigate customer data and increase engagement with products.

### Define the mission objectives
- Maintain customers' personal information
- Maintain index of products
- Easy Buying Process (Add To Cart, Check-Out, Payment)
- create an invoice for each order
- (Increase customer engangement:
        By Keeping track of customer behaviour(
            purchase history, 
            wishlist, 
            viewed products,
            )
        and recommend products based on that.)
- (Support)
- (Order Tracking)



### Functional Requirements
- register
- login
- homepage -> personalised products
- product index
- allow to place products into shopping cart
- place order from shopping cart
- payment
- confirmation email
- rate products


### Non-Functional Requirements
- admin-dashboard
- maintain customer information
- maintain product information
- user-sessions
- shopping cart implementation(how to do?)
- authentication
- mock payment system
- create an invoice for each order
- create model for store ratings


- api/v1/customer/registration/
    - POST: Register the customer
        - Request body

    ```
        {
        "username":{
                "type": "str",
                "value": "maxm",
                "required": true,
            },
    
        "first_name": {
                "type": "str",
                "value":"Max",
                "required": true,
            },
        "last_name": {
            "type":"str",
            "value":"Mustermann",
            "required": true,
            },
        "password": {
            "type":"password",
            "value":"maxpw2024!",
            "required": true,
        },
        "email": {
            "type":"str",
            "value":"max.mustermann@email.com",
            "required":true,
        },
        "address":{
            "type":"str",
            "value":"Musterstr. 13, 10000 Musterstadt",
            "required":true,
        },
        "phone":{
            "type":"str",
            "value":"+4014516266",
            "required":true,
        },
        "title":{
            "type":"str",
            "value":"Mr.",
            "required": false,
        },
        "birthday":{
            "type":"date",
            "value":"1990-01-01",
            "required": false,
        }
        }
        ```

    Request response
        - Status code: `201 created`
        ```
        {
            "username":"maxm",
            "first_name":"Max",
            "email":"max.mustermann@email.com",
        }
        ```

        - Status code: `400 invalid input`

        ```
        {
            "errorMessage":"Invalid Input"
        }
        ```



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



