import csv
import re

def is_valid_email (email):
    if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk|nhs.net)$",email):
        return True
    return False

def main():
    email= input("What's your email?").strip()
    name= input("whats your name?").strip()
    if is_valid_email(email):
        print("valid email, saving to contacts...")
        with open("contacts.csv","a") as file:
            writer =  csv.DictWriter (file, fieldnames = ["name","email"])
            writer.writerow({"name":name, "email":email})
    else :
        print("invalid")

if __name__ == "__main__":
    main()