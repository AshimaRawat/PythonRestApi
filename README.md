# PythonRestApi

This repository contains a RestApi created in Flask that can return product information and the insurance necessary to cover the risks of delivering them. The product details are in separate file(.json files).

The project is running at: http://127.0.0.1:5050

Software Programs used:

Python 3.8.8
Flask 2.2.1
PyCharm 2022.2 (Community Edition)

Steps to setup: 1.Clone the application git clone https://github.com/Ashimarawat/PythonRestApi.git

The app will start running at  http://127.0.0.1:5050.

Explore Rest APIs The app defines following CRUD APIs. 

Methodology:
1. Import necessary libraries like flask, request and pandas
2. Load the Products and productType json files into the main.py
4. Set the following url mappings to retrieve the information like:
5. 
    a. 127.0.0.1:5050/ -> For welcome page
    
    b. 127.0.0.1:5050/Products -> For getting Products information page
    
    c. 127.0.0.1:5050/ProductTypes -> For getting Product Type information
    
    d. 127.0.0.1:5050/ProductId?id=product_id -> Returns product information for a product with id= product_id
    
    e. 127.0.0.1:5050/ProductType?id=productTypeId -> Returns product type for a product with productTypeId
    
    f. 127.0.0.1:5050/Calculate_Insurance?id=product_id -> Returns insurance details
    
    
    
