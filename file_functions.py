#create the file object, open for reading
myfile = open("data.txt", "r")

#print the whole file contents
#print(myfile.read())

#print line by line
#print(myfile.readline())
#print(myfile.readline())

#go through file line by line
for line in myfile:
    print(line)
#close the file
myfile.close()


#open the file for over-writing
myfile=open("data.txt", "w")
#write new content to the file
myfile.write("new file contents\n")
#close the file
myfile.close()

#open the file for adding more content
myfile=open("data.txt", "a")
#write new content to the file
myfile.write("added content\n")
#close the file
myfile.close()
