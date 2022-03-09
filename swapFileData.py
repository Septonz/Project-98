import os

def swapData():
    file1=input("Type in your first file: ")
    file2=input("Type in your second file: ")

    with open(file1,'r') as reader:
        file1_data=reader.readlines()

    with open(file2,'r') as reader:
        file2_data=reader.readlines()
    
    with open(file1,'w') as writer:
        writer.writelines(file2_data)

    with open(file2,'w') as writer:
        writer.writelines(file1_data)
   
swapData()