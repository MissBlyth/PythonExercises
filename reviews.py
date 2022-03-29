#import the Element Tree library for reading xml files
import xml.etree.ElementTree as ET

#parse the xml file into a DOM (document object model)
reviewXML = ET.parse("reviews.xml")

#get the root node of the tree
root=reviewXML.getroot()

#see the XML structure - tags, attributes
for x in root.iter():
    print(x.tag, x.attrib)

rest1 = root[0].get('name')
print("Press 1 to review ", rest1)
rest2 = root[1].get('name')
print("Press 2 to review ",rest2)

#get restaurant selection
select_rest=input("Enter the restaurant number:")
select_rest= int(select_rest) - 1


#print selection


#get rating from user
newrating=input("How many stars would you rate this dining experience:")

#get comment from user
newcomment = input("Please leave a comment to explain your rating:")

#get existing rating attribute from restaurant XML
oldrating =  root[select_rest].get('rating')

#change the review rating to the new information
root[select_rest].set('rating',newrating)


#add the new comment review
appcomment = ET.SubElement(root[select_rest], "comment")
appcomment.text = newcomment

#rewrite the xml file to check the changes are there....
reviewXML.write('output.xml')


#print(root[0].tag) #gets first branch
#print(root[0][1].tag) #gets second sub branch
#print(root[0].attrib) #gets the attribute names and values

#get value of attributes using their names
#print(root[0].get("year"))
#print(root[1].get("genre"))
'''
#get text from a node - 3 actors from the first movie
print(root[0][0].text)
print(root[0][1].text)
print(root[0][2].text)

#get the 5 actors from the second movie
print(root[1][0].text)
print(root[1][1].text)
print(root[1][2].text)
print(root[1][3].text)
print(root[1][4].text)

'''
#search a branch for children with specific names
#only searches direct child nodes
#or movie in root.findall('movie'):
    #get title from the tag
    #print(movie.get("title"))

#search the whole tree for a tag (returns all children!)
#searches every node for a match
#for actor in root.iter('actor'):
    #print(actor.text)


