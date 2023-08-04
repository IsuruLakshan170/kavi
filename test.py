data = "[Isuru,21,1]"
data = data.strip("[]")  # Removing brackets from the string
data_list = data.split(',')

name = data_list[0]
age = int(data_list[1])  # Converting age to an integer
gender = int(data_list[2])  # Converting gender to an integer

print("Name:", name)
print("Age:", age)
print("Gender:", gender)
