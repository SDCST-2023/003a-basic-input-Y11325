#! python3
"""
Ask the user for their name and their email address.
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.
"""
data = input("Press the Enter Key to fill out your name and email address: ")
print("\n\n")
question1 = "Name: "
question2 = "Email Address: "
response1 = input(question1)
print("\n\n")
response2 = input(question2)
print("\n\n")
print(f"Your name is {response1}, and your email is {response2}\n")
