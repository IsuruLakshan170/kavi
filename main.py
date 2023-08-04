filename = 'textfile.txt'

with open(filename, 'w') as file:
    for i in range(1, 11):
        row = f"[{i},{i},{i}]\n"
        file.write(row)

import os

# Check if the file exists before reading
if not os.path.exists(filename):
    print("File not found.")
else:
    # Get the file size in bytes
    file_size_bytes = os.path.getsize(filename)

    # Convert file size to kilobytes (KB)
    file_size_kb = file_size_bytes / 1024

    print(f"The size of the file '{filename}' is {file_size_kb:.2f} KB.")





























#----------------------------



















# import json

# # message2 = "[[0,1,12],[0,1,12]]"

# # # Parse the JSON string into a Python object (nested list)
# # parsed_message = json.loads(message2)

# # # Convert the nested list to an integer array
# # integer_array = []
# # for sublist in parsed_message:
# #     integer_subarray = [int(element) for element in sublist]
# #     integer_array.append(integer_subarray)

# # print(type(integer_array))
# # import json

# # # Assuming you have the integer array as 'integer_array'
# # integer_array = [[0, 1, 12], [0, 1, 12]]

# # # Convert the integer array to a JSON string
# # json_string = json.dumps(integer_array)

# # print(type(json_string))
# filename = 'textfile.txt'
# integer_array = []

# with open(filename, 'r') as file:
#     for line in file:
#         # Use eval() to convert the string representation of the list into a list object
#         line_list = eval(line.strip())
#         integer_array.append(line_list)

# print(integer_array)

# json_string = json.dumps(integer_array)
# print(type(json_string))
