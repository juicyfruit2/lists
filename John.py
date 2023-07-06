# Wrote a program called John that takes in a user’s input as a string.

# created a variable to create a list to store incorrect names 
incorrect_names =[]

# used a while loop,if statement,.append,.lower() to output the incorrect names 
while True :
    user_input = str(input("Enter your name:"))
    
    if user_input == "John".lower():
     break

    incorrect_names.append(user_input)
print(incorrect_names)
