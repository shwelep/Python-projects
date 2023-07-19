def slice():
    print("Welcome to the email Slicer :)")
    print(" ")

    email_input = input('Input your email address: ')
    userName, domain = email_input.split("@")
    domain, extension = domain.split(".")

    print("User Name:", userName)
    print("Domain:", domain)
    print("Extension:", extension)

while True:
    slice()
