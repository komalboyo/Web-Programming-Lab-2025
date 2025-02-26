# Write a python program to reverse a content a file and store it in another file.

fname = input("Enter the filename: ")
f = open(fname, 'r')
content = f.read()
reversed_content = content[::-1]
file = open("q1_output.txt", 'w')
file.write(reversed_content)
print(f"Content has been reversed")
