matrix_string = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

matrix_rows = matrix_string.split("\n")

num_columns = max(len(row) for row in matrix_rows)

for i in range(len(matrix_rows)):
    matrix_rows[i] = matrix_rows[i].ljust(num_columns)

decoded_message = ""
for j in range(num_columns):
    for i in range(len(matrix_rows)):
        char = matrix_rows[i][j]
        if char.isalpha():
            decoded_message += char
    decoded_message += " "

print("Decoded message:", decoded_message)
