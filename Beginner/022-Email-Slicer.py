# Day 1: Email Slicer.
# In essence, Email Slicer is just a simple tool that will take an email address as input and slice it to produce the username and the
# domain associated with it. The email must be divided into two strings by using ‘@’ as the separator.
a = input("Enter your email address: ")
b = a.split("@")
print(f"The username is {b[0]} and the domain associated is {b[1]}")

# OR. It can be solved like this as well.

email = input("Enter Your Email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
print(f"Your username is {username} & domain is {domain}")
