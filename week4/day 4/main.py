# # module Psychopg2
# import psycopg2

# # connect to the database
# connection = psycopg2.connect(
#     database="Hollywood",
#     user="anabelrivera",
#     password="root",
#     host="localhost",  # or IP address
#     port="5432",
# )


# def retrieve_actors():
#     try:
#         with connection:
#             with connection.cursor() as curs:  # open and close the cursor
#                 query = "SELECT * FROM actors"
#                 curs.execute(query)
#                 data = curs.fetchall()
#                 print(data)

#     except Exception as err:
#         print(err)


# retrieve_actors()


# # def retrieve_actors_cars(last_name):
# #     try:
# #         with connection:
# #             with connection.cursor() as curs:  # open and close the cursor
# #                 query = f"SELECT first_name, movie_id FROM actors INNER JOIN actors_movies on actor.id = producer_movies.actor_id where last_name = '{last_name}'"
# #                 curs.execute(query)
# #                 data = curs.fetchone()  # to get one tupple
# #                 # for info in data:
# #                 #     print(info)
# #                 print(f"{data[0]} has a {data[2]} {data[1]}")

# #     except Exception as err:
# #         print(err)


# # retrieve_actors_cars("Clooney")


# def insert_actor(*info):
#     try:
#         with connection:
#             with connection.cursor() as curs:  # open and close the cursor
#                 query = f"INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES  {info}"
#                 curs.execute(query)
#                 connection.commit()

#     except Exception as err:
#         print(err)


# insert_actor("Johnny", "Depp", "1980/ 4/ 22", 4)
# retrieve_actors()

# connection.close()


# CONDITION 1 - sorted array/ list
# condition 2 - value to compare to
# sorted_array = list(range(1000))
# value_to_search = 2000


def binary_search(array, value_to_search):
    right = len(some_array)
    left = 0
    middle = some_array[len(some_array) // 2]
    iteration = 0

    while True:
        iteration += 1
        if middle == value_to_search:
            print(f"We found it - {value_to_search}")
            print(f"Iterarions: {iteration}")
            break

        elif middle < value_to_search:
            left = middle
            middle = (left + right) // 2
        elif middle > value_to_search:
            right = middle
            middle = (left + right) // 2
        else:
            print("no such value")
            break


some_array = list(range(1000))
value = 1500
binary_search(some_array, value)
