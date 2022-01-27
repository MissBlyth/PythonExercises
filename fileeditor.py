'''
File editing program
Will open and read a files contents - tick
Will rewrite the contents from input
'''
#open the data file for reading
myfile = open("data.txt","r")
#read and print the contents of the file
print(myfile.read())
#close the file to free the memory space
myfile.close()

#get new content from the user
newContent=input("Enter new file content:")

#open the data file for writing
myfile = open("data.txt","w")
#write new data to the file
myfile.write(newContent)
#close the file to free the memory space
myfile.close()
