file1=open("output.txt","w")
data=input("Enter the text to write to the file:")
file1.write(data + '\n')
print("Data successfully written to output.txt")
file1.close()

file1=open("output.txt","a")
data1=input("Enter the additional text to append:")
file1.write(data1+'\n')
file1.close()


with open('output.txt', 'r') as file:
    for line in file:
        print(line, end='')
