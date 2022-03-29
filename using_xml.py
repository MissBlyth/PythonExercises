#import the Element Tree library for reading xml files
import xml.etree.ElementTree as ET

#parse the xml file into a DOM (document object model)
myXML = ET.parse("data.xml")

#get the root node of the tree
root=myXML.getroot()


#see the XML structure - tags, attributes
for x in root.iter():
    print(x.tag, x.attrib)

print(root[0].tag) #gets first branch
print(root[0][1].tag) #gets second sub branch
print(root[0].attrib) #gets the attribute names and values

#get value of attributes using their names
print(root[0].get("year"))
print(root[1].get("genre"))
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
for movie in root.findall('movie'):
    #get title from the tag
    print(movie.get("title"))

#search the whole tree for a tag (returns all children!)
#searches every node for a match
for actor in root.iter('actor'):
    print(actor.text)


