


  import os
  
filepath = input("Enter path for file: ")
filename = input("Enter name of file: ")
if not os.path.exists(filepath):
    os.makedirs(filepath)
fullname = os.path.join(filepath,filename + ".csv")
  

name = input("Enter full name: ")
address = input("Enter Address: ")
phone = input("Enter Phone Number: ")
fileobj = open(fullname, "w")
fileobj.write(name+'\n'   " "   +address+'\n'  " "   +phone +'\n')
fileobj.close()
  
fileobj = open(fullname, "r")
print('\n')
print(fileobj.read())   

