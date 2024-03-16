from db.db_connect import Dbconnect

class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        return Dbconnect.connect(query, "select")

    @staticmethod
    def update(table, column_name, new_data, old_data):
        query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
        return Dbconnect.connect(query, "update")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        return Dbconnect.connect(query, "delete")

class City(Base):
    def __init__(self, name):
        self.name = name

    def insert(self):
        query = f"INSERT INTO city(name) VALUES ('{self.name}')"
        return Dbconnect.connect(query, "insert")

class Address(Base):
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def insert(self):
        query = f"INSERT INTO address(name, city_id) VALUES('{self.name}','{self.city}')"
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = " SELECT address.name,  city.name FROM address INNER JOIN city ON address.city_id = city.city_id"
        return Dbconnect.connect(query, "select")

class Customer(Base):
    def __init__(self, firstname, lastname, username, password, email, phone, address):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address

    def insert(self):
        query = f"""
            INSERT INTO customer(firstname, lastname, username, password, email, phone, address_id) 
                VALUES ('{self.firstname}','{self.lastname}','{self.username}','{self.password}','{self.email}','{self.phone}', {self.address})
        """
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = f"""SELECT customer.firstname, customer.lastname, customer.username, customer.password, customer.email, customer.phone, address.name FROM customer INNER JOIN address ON customer.address_id = address.address_id;  """
        return Dbconnect.connect(query, "select")

class Menejers(Base):
    def __init__(self, firstname, lastname, username, password, email, phone, address):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address

    def insert(self):
        query = f"""
            INSERT INTO customer(firstname, lastname, username, password, email, phone, address_id) 
                VALUES ('{self.firstname}','{self.lastname}','{self.username}','{self.password}','{self.email}','{self.phone}', {self.address})
        """
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = f"""SELECT menejers.firstname, menejers.lastname, menejers.username, menejers.password, menejers.email, menejers.phone, address.name FROM menejers INNER JOIN address ON menejers.address_id = address.address_id;  """
        return Dbconnect.connect(query, "select")

class Category(Base):
    def __init__(self, name):
        self.name = name

    def insert(self):
        query = f"INSERT INTO category(name) VALUES ('{self.name}')"
        return Dbconnect.connect(query, "insert")

class Regions(Base):
    def __init__(self, name):
        self.name = name

    def insert(self):
        query = f"INSERT INTO regions(name) VALUES ('{self.name}')"
        return Dbconnect.connect(query, "insert")

class Product(Base):
    def __init__(self, name, description, price, count, category, region):
        self.name = name
        self.description = description
        self.price = price,
        self.count = count
        self.category = category
        self.region = region

    def insert(self):
        query = f"""INSERT INTO product(name,description, price, count, category, region)
            VALUES ('{self.name}', '{self.description}', {self.price}, {self.count}, {self.category}, {self.region})
         """

        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = f"""
        SELECT product.name, product.description, product.price, product.count, category.name, regions.name FROM product 
            INNER JOIN category 
                ON product.category_id = category.category_id 
            INNER JOIN regions 
                ON product.region = regions.region_id;
        """
        return Dbconnect.connect(query, "select")

class Payment(Base):
    def __init__(self, amound, card, product, customer):
        self.amound = amound
        self.card = card
        self.product = product
        self.customer = customer

    def insert(self):
        query = f"""INSERT INTO payment(amound, card, product_id, customer_id)
            VALUES({self.amound}, {self.card}, {self.product}, {self.customer})
        """
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = "SELECT payment.amound, payment.card, product.name, customer.username FROM payment INNER JOIN product ON payment.product_id = product.product_id INNER JOIN customer ON payment.customer_id = customer.customer_id;"
        return Dbconnect.connect(query, "select")

class Shop_location(Base):
    def __init__(self, name):
        self.name = name,

    def insert(self):
        query = f"""INSERT INTO shop_lacatipon(name) VALUES('{self.name}')"""
        return Dbconnect.connect(query, "select")


class Shop_directors(Base):
    def __init__(self, name, shop_l_id):
        self.name = name
        self.shop_l_id = shop_l_id

    def insert(self):
        query = f"""INSERT INTO shop_directors(name, shop_l_id) VALUES('{self.name}', {self.shop_l_id})"""
        return Dbconnect.connect(query, "insert")

    @staticmethod
    def select_inner_join():
        query = "SELECT shop_directors.name, shop_lacatipon.name FROM shop_directors INNER JOIN shop_lacatipon ON shop_directors.shop_l_id = shop_lacatipon.shop_l_id;"
        return Dbconnect.connect(query, "select")




