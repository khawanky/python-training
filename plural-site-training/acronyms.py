def find_acronym():
    look_up = input("Software acronym to search:\n")
    found = False
    # TODO: Doing something
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")

        if not found:
            print('This acronym does not exist')

def add_acronym():
    acronym = input('Acronym to add:\n')
    definition = input('Acronym definition:\n')
    with open('acronyms.txt', 'a') as file:
        # if acronym in file.read():
            # print("Acronym already exists")
        # else:
        file.write(acronym + " - " + definition + "\n")

def main():
    choice = input('Do you want to find(F) or add(A) an acronym:\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
    else:
        print("Bad choice!")

main()
