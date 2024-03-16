from classes import City, Address, Customer, Menejers, Category, Regions, Product, Payment, Shop_directors, Shop_location
def city_table():
    select_city = input("""
        1. Insert
        2. Update
        3. Delete
        4. Select
        0. Back
    """)

    if select_city == "1":
        city_name = input("Enter your city name: ")
        city = City(city_name)
        city.insert()
        return city_table()
    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(City.update("city", column_name, new_data, old_data))
        return city_table()

    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")

        print(City.delete("city", column_name, data))
        return city_table()

    elif select_city == "4":
        data = City.select("city")

        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)
        return city_table()

    elif select_city == "0":
        return main()
def address_table():
    select_city = input("""
        1. Insert
        2. Update
        3. Delete
        4. Select
        0. Back
        """)

    if select_city == "1":
        name = input("Enter address name: ")
        city = int(input("Enter city id: "))
        address = Address(name, city)
        address.insert()
        return address_table()
    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")

        print(Address.update("address", column_name, new_data, old_data))
        return address_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")

        print(Address.delete("address", column_name,data))
        return address_table()

    elif select_city == "4":
        data = Address.select_inner_join()
        for i in data:
            print(f"""
                Address Name: {i[0]}
                City Name: {i[1]}
            """)
        return address_table()

    elif select_city == "0":
        return main()
def cutomers_table():
    select_city = input("""
            1. Insert
            2. Update
            3. Delete
            4. Select
            0. Back
            """)

    if select_city == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter lastname: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        address = int(input("Enter address id: "))
        customer = Customer(first_name, last_name, username, password, email, phone, address)
        customer.insert()
        return cutomers_table()
    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Customer.update("customer", column_name, new_data, old_data))
        return cutomers_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        print(Customer.delete("customer", column_name, data))
        return cutomers_table()
    elif select_city == "4":
        data = Customer.select_inner_join()
        for i in data:
            print(f"""
                First Name: {i[0]}
                Last Name: {i[1]}
                User Name: {i[2]}
                Password: {i[3]}
                Email: {i[4]}
                Phone Number: {i[5]}
                Address: {i[6]}
            """)
        return cutomers_table()
    elif select_city == "0":
        return main()
def menejrs_table():
    select_city = input("""
            1. Insert
            2. Update
            3. Delete
            4. Select
            0. Back
            """)

    if select_city == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter lastname: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        address = int(input("Enter address id: "))
        menejers = Menejers(first_name, last_name, username, password, email, phone, address)
        menejers.insert()
        return menejrs_table()
    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Menejers.update("menejers", column_name, new_data, old_data))
        return menejrs_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        print(Menejers.delete("menejers", column_name, data))
        return menejrs_table()
    elif select_city == "4":
        data = Menejers.select_inner_join()
        for i in data:
            print(f"""
                First Name: {i[0]}
                Last Name: {i[1]}
                User Name: {i[2]}
                Password: {i[3]}
                Email: {i[4]}
                Phone Number: {i[5]}
                Address: {i[6]}
            """)
        return menejrs_table()
    elif select_city == "0":
        return main()
def category_table():
    select_city = input("""
       1. Insert
       2. Update
       3. Delete
       4. Select
       0. Back
           """)

    if select_city == "1":
        name = input("Enter name category: ")
        catgory = Category(name)
        catgory.insert()
        return category_table()
    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Category.update("category", column_name, new_data,old_data))
        return category_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        print(Category.delete("category", column_name, data))
        return category_table()
    elif select_city == "4":
        data = Category.select()
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)

        return category_table()
    elif select_city == "0":
        return main()
def regions_table():
    select_city = input("""
           1. Insert
           2. Update
           3. Delete
           4. Select
           0. Back
               """)
    if select_city == "1":
        name = input("Enter new name: ")
        regiosn = Regions(name)
        regiosn.insert()
        return regions_table()

    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Regions.update("regions", column_name, new_data, old_data))
        return regions_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        print(Regions.delete("regions", column_name, data))
        return regions_table()
    elif select_city == "4":
        data = Regions.select()
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)
        return regions_table()


def products_table():
    select_city = input("""
       1. Insert
       2. Update
       3. Delete
       4. Select
       0. Back
           """)
    if select_city == "1":
        name = input("Enter new name: ")
        description = input("Enter new description: ")
        price = int(input("Enter new price: "))
        count = int(input("Enter count: "))
        catgorys = int(input("Enter categor id: "))
        regions = int(input("Enter regions id: "))
        products = Product(name,description,price,count,catgorys,regions)
        products.insert()
        return products_table()
    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Product.update("product", column_name, new_data, old_data))
        return products_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        print(Product.delete("product", column_name, data))
        return products_table()
    elif select_city == "4":
        data = Product.select_inner_join()
        for i in data:
            print(f"""
                Name: {i[0]}
                Description: {i[1]}
                Price: {i[2]}
                Count: {i[3]}
                Category: {i[4]}
                Regions: {i[5]}
            """)
        return products_table()

def payment_table():
    select_city = input("""
           1. Insert
           2. Update
           3. Delete
           4. Select
           0. Back
               """)
    if select_city == "1":
        amoud = int(input("Enter Amount: "))
        card = int(input("Enter card: "))
        product = int(input("Enter product: "))
        customer = int(input("Enter customer: "))
        payment = Payment(amoud, card, product, customer)
        payment.insert()
        return payment_table()
    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Payment.update("payment",column_name, old_data, new_data))
        return payment_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        print(Payment.delete("payment", column_name, data))
        return payment_table()
    elif select_city == "4":
        data = Payment.select_inner_join()
        for i in data:
            print(f"""
                Amound: {i[0]}
                Card: {i[1]}
                Profucts: {i[2]}
                Customer: {i[3]}
            """)
        return payment_table()
    elif select_city == "0":
        return main()

def shop_location_table():
    select_city = input("""
       1. Insert
       2. Update
       3. Delete
       4. Select
       0. Back
           """)
    if select_city == "1":
        name = input("Enter name: ")
        shop_l = Shop_location(name)
        shop_l.insert()
        return shop_location_table()
    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter data: ")
        old_data = input("Enter old data: ")
        print(Shop_location.update("shop_lacatipon", column_name, old_data, new_data))
        return shop_location_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        print(Shop_location.delete("shop_lacatipon", column_name, data))
        return shop_location_table()
    elif select_city == "4":
        data = Shop_location.select()
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)
        return shop_location_table()
    elif select_city == "0":
        return main()


def shop_director_table():
    select_city = input("""
           1. Insert
           2. Update
           3. Delete
           4. Select
           0. Back
               """)

    if select_city == "1":
        name = input("Enter name: ")
        shop_l = int(input("Enter shop location id: "))

        shop_d = Shop_directors(name, shop_l)
        shop_d.insert()
        return shop_director_table()

    elif select_city == "2":
        column_name = input("Enter column name: ")
        new_data = input("Enter new data: ")
        old_data = input("Enter old data: ")
        print(Shop_directors.update("shop_directors", column_name, new_data, old_data))
        return shop_director_table()
    elif select_city == "3":
        column_name = input("Enter column name: ")
        data = input("Enter date: ")
        print(Shop_directors.delete("shop_directors", column_name, data))
        return shop_director_table()
    elif select_city == "4":
        data = Shop_directors.select_inner_join()
        for i in data:
            print(f"""
                Name: {i[0]}
                Location: {i[1]}
            """)
        return shop_director_table()
    elif select_city == "0":
        return main()
    



def main():
    selecty = input("""
        1. City
        2. Address
        3. Customers
        4. Menejers
        5. Category
        6. Regions
        7. Products
        8. Payment
        9. Shop_location
        10. Shop Directors
    """)

    if selecty == "1":
        return city_table()
    elif selecty == "2":
        return address_table()
    elif selecty == "3":
        return cutomers_table()
    elif selecty == "4":
        return menejrs_table()
    elif selecty == "5":
        return category_table()
    elif selecty == "6":
        return regions_table()
    elif selecty == "7":
        return products_table()
    elif selecty == "8":
        return payment_table()
    elif selecty == "9":
        return shop_location_table()
    elif selecty == "10":
        return shop_director_table()


if __name__ == '__main__':
    main()