import re

ID=str(input("whats your student ID:"))
if re.search(r"^\D{4}+\d{4}$", ID):
    print("ID Valid")
else :
    print ("Not recognised")
#completed