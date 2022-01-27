'''
This is a class activity about using associative arrays.
EXAMPLE FROM SLIDES
teacher ={“LBL”:”Blyth, Lorraine”,”JVI”:“Vieusseux, Jessica”,”RAE”:”Rae”:”Rae, Andy”,”CKN”:”Kneen, Catherine”}
'''

#create an associative array
room={"B503":"Software Development Lab", "A516":"Computing", "A515":"Visual Communication Studio"}


#cycle through each key in the array
for each in room:
    print(each)

#cycle through each value in the array
for each in room:
    print(room[each])

#access an elements value by using it's key directly
print(room["A516"])

'''
Other applications of dictionary data structures might include storing data about a particular object
Example from w3schools:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
'''
#create an array based around an object and its properties
movie = {"title":"Parasite", "year":"2019", "director":"Bong Joon-ho","genre":"Thriller","duration":"132"}

#print key and value pairs for whole array
print(movie)

'''
Changing the array 
'''

#remove an item
#change an items value
#add a new item
