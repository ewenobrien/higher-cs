names = []
marks = []

for index in range(5):
    name =  str(input("Enter your name"))
    names.append(name)
    

for index in range(5):
    mark = int(input("Enter your mark out of 100"))
    while mark > 100 or mark < 0:
        print("Invalid number")
        break
    else:
        marks.append(mark)
    
print ("Marks are as follows", marks)
print ("Names are as follows", names)


    


