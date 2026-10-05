def get_number():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Not a number. Please try again.")


number = get_number()
print("You entered:", number)
