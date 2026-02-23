import re
number= str(input("Whats your phone number?"))
if re.search("07+\d{9}",number):
    print ("Phone number valid")
#complete!!