#get input from the user
data = input("Enter a temperature in Celsius:")

#check if the data is numbers
if data.isnumeric() == True:
    #convert data to a float
    cels = float(data)
    fahr = (cels * 9/5) + 32
    print(cels, "degress celsius is ", fahr, "degrees Fahrenheit.")
else:
    print("Data not valid")

#print the type and the data
print(type(data), data)
