from sorting import sorting


def __main__():

    while True:
        print("\nChoose an algorithm to sort with!")
        print("1: Bubble Sort")
        print("2: Insertion Sort")
        print("3: Selection Sort")
        print("4: Quick Sort")
        choice = input("Use algorithm nr: ")

        if choice == "1":
            sorter = sorting("Bubble Sort")
            sorter.loop("bubble")
        elif choice == "2":
            sorter = sorting("Insertion Sort")
            sorter.loop("insertion")
        elif choice == "3":
            sorter = sorting("Selection Sort")
            sorter.loop("selection")
        elif choice == "4":
            sorter = sorting("Quick Sort")
            sorter.loop("quick")
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    __main__()
