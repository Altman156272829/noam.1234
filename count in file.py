with open("count_txt.txt","w") as file:
    file.write("hello world bye world bye ok bye")

with open("count_txt.txt","r") as file:
    data =file.read()
print(data)
