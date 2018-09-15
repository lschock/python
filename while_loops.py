#Repeating things in code is a frequent need. While repeats code until an expression is no longer True.

print("This is just an example of how a 'while' loop works.  It is not good code in a real application as a password checker!")

import sys

MASTER_PASSWORD = "montypython"  #ALL CAPS INDICATE THIS IS A CONSTANT AND WILL NOT CHANGE
password = input("Please enter the super secret password:  ").lower()
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again:  ")
    attempt_count += 1
print("Welcome to secret town!")    
