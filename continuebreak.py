for i in range(10):
 if i%2==0:
  continue
print(i)

cart=[10,20,600,60,70]
for item in cart:
 print(item)
 if item>500:
  print("To place this order insurence must be required")
  break
  #continue
print(item)