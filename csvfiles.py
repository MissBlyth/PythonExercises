'''This program is going to open a csv, get the values out, and rewrite another CSV'''

#open the csv file
myFile=open("data.csv","r")


#create a blank array
names = []

#read each line in the csv file
for x in myFile:
    #removes new line characters
    x=x.strip("\n")

    #turn into an array based on commas
    x = x.split(",")

    #print each part of the line
    names.append(x[0])

#close the csv file
myFile.close()




#create a new file
newFile=open("newdata.csv","w")

#write all names to the file separated by commas
for x in names:
    newFile.write(x + ",")

newFile.close()
#close the file
