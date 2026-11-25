# M12P1 Module 12 Patrick Chang 11/24/2026

#define variables
def display_names(names):
    for i in range(10):
        print(names[i])


def display_reverse(names):
    for i in range(9, -1, -1):
        print(names[i])

#names
def main():
    names = [
        "Pinky",
        "Browny",
        "Yellowy",
        "Orangey",
        "Bluey",
        "Purpley",
        "Redy",
        "Greeny",
        "Blacky",
        "Whitey",
    ]
#outputs
    print("Names in order:")
    display_names(names)

    print("\nNames in reverse:")
    display_reverse(names)


main()