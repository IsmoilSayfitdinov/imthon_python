from db.db_connect import Dbconnect


def create_table():
    city = """
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            create_date TIMESTAMP default now()
        )
    """

    address = """
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            city_id INT REFERENCES city(city_id),
            create_date TIMESTAMP default now()
        )
    """


    customers = """
        CREATE TABLE customer(
            customer_id SERIAL PRIMARY KEY,
            firstname VARCHAR(20),
            lastname VARCHAR(20),
            username VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(50),
            phone VARCHAR(40),
            address_id INT REFERENCES address(address_id),
            create_date TIMESTAMP default now()
        )
    """

    menejers = """
        CREATE TABLE menejers(
            menejer_id SERIAL PRIMARY KEY,
            firstname VARCHAR(20),
            lastname VARCHAR(20),
            username VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(50),
            phone VARCHAR(40),
            address_id INT REFERENCES address(address_id),
            create_date TIMESTAMP default now()
        )
    """

    category = """
        CREATE TABLE category(
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_date TIMESTAMP default now()
        )
    """

    regions = """
        CREATE TABLE regions(
            region_id SERIAL PRIMARY KEY ,
            name VARCHAR(20)
        )
    """

    products = """
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            description TEXT,
            price NUMERIC,
            count INT,
            category_id INT REFERENCES category(category_id),
            region INT REFERENCES regions(region_id),
            create_date TIMESTAMP default now()
        )
    """

    payment = """
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            amound NUMERIC,
            card INT,
            product_id INT REFERENCES product(product_id),
            customer_id INT REFERENCES customer(customer_id),
            create_date TIMESTAMP default now()
        )
    """

    shop_lacatipon = """
        CREATE TABLE shop_lacatipon(
            shop_l_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_date TIMESTAMP default now()
        )
    """

    shop_directors = """
        CREATE TABLE shop_directors(
            shop_d_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            shop_l_id INT REFERENCES shop_lacatipon(shop_l_id),
            create_date TIMESTAMP default now()
        )
    """


    data = {
        "city": city,
        "address": address,
        "customers": customers,
        "menejers": menejers,
        "category": category,
        "regions": regions,
        "products": products,
        "payment": payment,
        "shop_lacatipon": shop_lacatipon,
        "shop_directors": shop_directors
    }

    for i in data:
        print(f"{i}: {Dbconnect.connect(data[i], "create")}")

if __name__ == "__main__":
    create_table()