l=0
b=200
try:
    print(b/l)
except Exception as ae:
    print(123)
print(1)
age=16
if age>17:
    print("candidate is eligible for Voting and do the vote")
else:

    print("Candidate is not allowed for voting")
    raise  Exception('age is not less then 17 so no voting allowed ')