abbreviation = {"API": "Application Programming Interface",
                "IDE": "Integrated Development Environment",
                "SDK": "Software Development Kit",
                "UI": "User Interface",
                "UX": "User Experience"}

abbreviation["OOP"] = "Object-Oriented Programming"  # adds OOP key and its value abbreviation dictionary
abbreviation["SSH"] = "Secure Shell"  # adds SSH key and its value to the abbreviation dictionary

user_input = input("Enter an abbreviation: ")
uppercase_input = user_input.upper()
if uppercase_input in abbreviation:
    print(f"{uppercase_input} : {abbreviation[uppercase_input]}")
else:
    print("Abbreviation not found")
