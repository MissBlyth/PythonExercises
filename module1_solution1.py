'''This program is going to open a csv, get the values out, and rewrite another CSV'''
#ANALYSING THE FILE
#open the csv file
students=open("student_data.csv","r")

#TRACKING THE ERRORS
#EXISTENCE CHECK
#RANGE CHECK - 7 TO 12
#CHECK STUDENT ID


#create a blank array FOR VALID DATA
validstudents = []

#create tracking variables
blanks=0
outofrange=0
siderrors=0


#read each line in the csv file
for x in students:
    is_valid=True

    #removes new line characters
    y=x.strip("\n")
    #turn into an array based on commas
    y = y.split(",")

    for z in y:
        if z == "":
            blanks+=1
            is_valid=False

    studentid=y[2]
    yearlevel=y[3]

    try:
        if int(yearlevel) >= 7 and int(yearlevel) <= 12:
            is_valid=True
    except:
        is_valid=False
        outofrange += 1

    #print each part of the line
    if is_valid == True:
        validstudents.append(x)

#close the csv file
students.close()

#output errors

#CREATE THE COPY

#create a new file
newFile=open("newdata.csv","w")

#write all names to the file separated by commas
for x in validstudents:
    newFile.write(x)

#close the file
newFile.close()

#output the analysis of errors
print("Blanks:", blanks)
print("Year Level out of range:", outofrange)
print("Student ID errors:", siderrors)
