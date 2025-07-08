# name1 = input("Enter your first name:")
# name2 = input("Enter your last name:") 

# full_name = f"{name1.capitalize()} {name2.capitalize()}"
# print(f"Your\'s welcome in my project, {full_name}")

def create_name(name1, name2):
    return f"Your full name is: {name1.capitalize()} {name2.capitalize()}"
    
name1 = input("Enter your first name: ")
name2 = input("Enter your last name: ")

full_name = create_name(name1, name2)
print(full_name)
