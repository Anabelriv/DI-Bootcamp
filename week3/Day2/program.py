# with open("choco.txt", "r") as choco_file:
#     all_text = choco_file.readlines()
#     print(all_text[1])
#     for line in enumerate(all_text):
#         print(f'#(index+1) -- {line}')

# 
# with open("choco.txt", "a") as choco_file:
#     choco_file.write("Hellooo") # appends hellooo at the end of the file

# with open("choco.txt", "w") as choco_file:
#     choco_file.write("Hellooo") # appends hellooo at the end of the file

with open("choco.txt", "r+") as choco_file:
    all_lines = choco_file.readlines()
    all_lines.insert(2, "Helloooo  ...  ")
    print(all_lines)
    choco_file.seek(0)
    choco_file.writelines(all_lines)
    print(all_lines)

    