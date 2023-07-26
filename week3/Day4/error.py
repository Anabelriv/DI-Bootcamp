# Create a colorize(text, color) function that contain this tuple colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
# If the color parameter is not present in the tuple, raise a ValueError exception
# If the text parameter is not a string raise a TypeError Exception
# make sure to catch the exception

def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    try:
        if not isinstance(text, str):
            raise TypeError("Text parameter must be a string.")

        if color not in colors:
            raise ValueError("Invalid color. Choose one of: cyan, yellow, blue, green, magenta.")
    except Exception as err: # except (TypeError, ValueError) as e:
        print(err)

    else:
        print("everything is ok")

        


colorize(1, "blue")
colorize('abc',"black")
colorize("abc", "blue")
