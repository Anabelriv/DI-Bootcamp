import requests
import random
import psycopg2


# Function to fetch data from the REST Countries API
def fetch_countries_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from API.")
        return None


# Function to select 10 random countries from the list
def get_random_countries(countries_data):
    return random.sample(countries_data, 10)


# Function to save country data to the database
def save_country_to_database(country):
    query = "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)"
    data = (
        country["name"]["common"],
        country.get("capital", ""),
        country["flags"].get("png", ""),
        country.get("subregion", ""),
        country.get("population", 0),
    )
    manage_connection(query, data, "insert")


def manage_connection(query, data=None, type="select"):
    # Connect to the database
    connection = None
    try:
        connection = psycopg2.connect(
            database="countries",
            user="anabelrivera",
            password="root",
            host="localhost",  # or IP address
            port="5432",
        )
        with connection:
            with connection.cursor() as cursor:  # it closes the transaction
                if data:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query)
                if type != "select":
                    connection.commit()
                else:
                    return cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if connection != None:
            connection.close()  # need to specifically close the connection


def main():
    countries_data = fetch_countries_data()
    if countries_data:
        random_countries = get_random_countries(countries_data)
        for country in random_countries:
            save_country_to_database(country)


if __name__ == "__main__":
    main()
