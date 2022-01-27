#check that the data is specific ie Months
months=["January","February","March","April","May","June","July","August","September","October","November","December"]

data = input("Enter month:")

if data in months:
    print("Month is valid")
else:
    print("Thats not a month.")

