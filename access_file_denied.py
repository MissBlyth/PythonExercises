'''This program checks the credentials of user against those stored in a file.'''

#open the file for reading
myfile=open("data.txt","r")

#read username
username=myfile.readline()
username=username[10:-2]
#print(username)

#read password
password=myfile.readline()
password=password[10:-2]
#print(password)

#close file
myfile.close()
#get username from user
getuser=input("Username:")

#get password from user
getpass=input("Password:")

#compare
if getuser==username and getpass==password:
    #if matching, access granted
    print("Access Granted")
else:
    #else access denied
    print("Access Denied")
