from flask import Flask, request
import pandas as pd
import json
import math


app = Flask(__name__)


# Importing the json files and converting them to respective dataframes

ProductsDf = pd.read_json('/Users/amitnegi/PycharmProjects/RestApi_CoolBlue/Products.json')

ProductTypesDf = pd.read_json('/Users/amitnegi/PycharmProjects/RestApi_CoolBlue/ProductsType.json')

# Mapping urls to corresponding values
# (127.0.0.1.5050/) For welcome page
# (127.0.0.1.5050/Products) For getting Products information page
# (127.0.0.1.5050/ProductTypes) For getting Product Type information page

@app.route("/")
def hello():
    return "****  Welcome to the products catalog  ***"


@app.route("/Products", methods=['GET'])
def get():
    return ProductsDf.to_html()


@app.route("/ProductTypes", methods=['GET'])
def getType():
    return ProductTypesDf.to_html()

CompleteDetails= ProductsDf.merge(ProductTypesDf, left_on='productTypeId', right_on='id')
print(CompleteDetails.to_string())



# TASK 1: For checking Products information
# (127.0.0.1.5050/ProductId?id=product_id) Returns product information for a corresponding product_id
@app.route("/ProductId")
def index1():
    prod_id = request.args
    for key, value in prod_id.items():
        a = int(value)
        return (CompleteDetails[CompleteDetails['id_x'] == a]).to_html()


# TASK 2 : For checking ProductType information
# (127.0.0.1.5050/ProductType?id=productTypeId) Returns product type information for a corresponding productTypeId
@app.route("/ProductType")
def index2():
    prod_type = request.args
    for key, value in prod_type.items():
        a = int(value)
    return CompleteDetails[CompleteDetails['id_y'] == a].to_html()


# TASK 3: implementing insurance conditions:


@app.route("/Calculate_Insurance")
def index3():
    prod_id1 = request.args
    for key, value in prod_id1.items():
        b = int(value)
        Price = CompleteDetails.loc[CompleteDetails.id_x == b, 'salesPrice']
        product = CompleteDetails.loc[CompleteDetails.id_x == b, 'name_y']
        print(product)
        Price1= math.ceil(Price)

# Defining a function that calculates the insurance

        def calculate(Price1):
            if (Price1 < 500):
                str= "No insurance needed"
            elif (Price1 >= 500 & Price1 < 2000):
                str="Insurance Cost 1000"
            elif (Price1 >= 2000):
                str = "Insurance Cost 2000"

            return str

        return calculate(Price1)


if __name__ == "__main__":
    app.run()
