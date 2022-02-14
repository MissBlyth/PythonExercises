'''  Working with Files '''
#opening files for reading
#myFile=open("data.txt","r")

#opening files for writing
#myFile=open("data.txt","w")

#opening files for appending.
myFile=open("data.txt","a")

#reading file contents
#print(myFile.read())

#writing to a file
#myFile.write("Software Development is my favourite subject.")

#appending a file
myFile.write("Software Development is my favourite subject.")

#closing files
myFile.close()
