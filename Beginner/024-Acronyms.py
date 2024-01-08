# Day 3: Create Acronyms using Python
# Write a python program that generates a short form of a word from a given sentence.
a = input("Enter your sentence: ")
b = a.split(" ")
d = []
for item in b:
  d.append(item[0])
def listtostr(s):
  e = ""
  for i in s:
    e += i
  return e
f = listtostr(d)
print(f"The acronym of your given word is {f}.")

# Code below is an alternative code.

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
