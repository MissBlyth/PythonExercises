#import the Element Tree library for reading xml files
import xml.etree.ElementTree as ET

#parse the xml file into a DOM (document object model)
reviewXML = ET.parse("reviews.xml")

#get the root node of the tree
root=reviewXML.getroot()
#restaurant 1

#see the XML structure - tags, attributes
for x in root.iter():
    print(x.tag, x.attrib)

rest1 = root[0].get('name')
print("Press 1 to review ", rest1)
rest2 = root[1].get('name')
print("Press 2 to review ",rest2)


#get restaurant selection - convert input to index
while True:
    select_rest=input("Enter the restaurant number:")
    try:
        select_rest= int(select_rest) - 1
        break
    except:
        print("Please enter a number.")

restname = root[select_rest].get('name')

print("Please enter your review for ", restname)


#get rating from user
newrating=input("How many stars would you rate this dining experience:")

#get comment from user
newcomment = input("Please leave a comment to explain your rating:")

#get existing rating attribute from restaurant XML
oldrating =  root[select_rest].get('rating')

#change the review rating to the new information
root[select_rest].set('rating',newrating)

#add the new comment to the xml tree structure
appcomment = ET.SubElement(root[select_rest], "comment")
appcomment.text = newcomment


#rewrite the xml file to check the changes are there
reviewXML.write('output.xml')

#write the output files for all restaurants
for x in root.iter("restaurant"):
    #create filename for restaurant
    filename= x.get('name') + ".txt"
    #open the file
    myFile=open(filename, "w")

    #get attribues
    myFile.write(x.get('name'))
    myFile.write(x.get('rating'))

    #get comments
    for y in x.iter("comment"):
        myFile.write(y.text)

    #close the file

    myFile.close()


