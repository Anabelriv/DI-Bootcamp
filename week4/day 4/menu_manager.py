import psycopg2
from menu_item import MenuItem, manage_connection


class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = (
            f"SELECT item_name, item_price FROM Menu_Items WHERE item_name = '{name}'"
        )
        result = manage_connection(query, "select")
        if result:
            name, price = result[0]
            return MenuItem(name, price)
        return None

    @classmethod
    def all_items(cls):
        query = "SELECT item_name, item_price FROM Menu_Items"
        results = manage_connection(query, "select")
        return [MenuItem(name, price) for name, price in results]
