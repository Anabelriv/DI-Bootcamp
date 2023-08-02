import psycopg2


def manage_connection(query, type):
    # connect to the database
    connection = None
    try:
        connection = psycopg2.connect(
            database="restaurant",
            user="anabelrivera",
            password="root",
            host="localhost",  # or IP address
            port="5432",
        )
        with connection:
            with connection.cursor() as cursor:  # it closes the transaction
                cursor.execute(query)
                if type == "insert":
                    connection.commit()
                elif type == "select":
                    return cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if connection != None:
            connection.close()  # need to specificaly closed the connection


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = f"INSERT INTO Menu_Items (item_name, item_price) VALUES ('{self.name}', {self.price})"
        manage_connection(query, "insert")

    def delete(self):
        query = f"DELETE FROM Menu_Items WHERE item_name = '{self.name}'"
        manage_connection(query, "insert")

    def update(self, new_name, new_price):
        query = f"UPDATE Menu_Items SET item_name = '{new_name}', item_price = {new_price} WHERE item_name = '{self.name}'"
        manage_connection(query, "insert")
