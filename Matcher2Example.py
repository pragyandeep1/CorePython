import re
s=input("Enter pattern to check: ")
m=re.match(s,"abcabdefg")
if m!= None:
 print("Match is available at the beginning of the String")
 print("Start Index:",m.start(), "and End Index:",m.end())
else:
 print("Match is not available at the beginning of the String")