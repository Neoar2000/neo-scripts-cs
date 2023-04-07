password = "pass"
guess = ""

while guess != password:
    guess = input("Enter the password to access: ")
    if guess != password:
        print("Wrong password.")

print("Welcome, Neo!")
