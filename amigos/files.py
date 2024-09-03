
# w=write , r =read , r+ = read/write , a = append

# file = open("./data.csv", "r")
# file.write("id,name,email\n")
# file.write("1,GFF,sdff@gama.com\n")
# file.write("2,sddddddddd,email@fake.com\n")
# file.write("3,aaa,Aaa@AAA.com\n")

# print(file.read())

# for line in file:
#     print(line)

# print(file.readlines())


# file.close()

import os.path

file_name = "data.csv"

if not os.path.isfile(file_name):
    print("Nooooooooooo")
else:
    with open(file_name, "r") as file:
        print(file.readlines())





