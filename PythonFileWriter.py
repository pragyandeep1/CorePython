with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

f = open("test.txt", 'r', encoding='utf-8')
print(f.read(4))  # read the first 4 data
print(f.read(4))  # read the next 4 data
print(f.tell())
print(f.read())  # read in the rest till end of file
print(f.read())  # further reading returns empty sting

for line in f:
 print(line, end = '')


