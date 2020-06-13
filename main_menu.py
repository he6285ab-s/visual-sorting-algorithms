from sorting import sorting

def __main__():
    
    while True:
        print("\nChoose an algorithm to sort with!")
        print("1: Bubble Sort")
        print("2: Insertion Sort")
        print("3: Selection Sort")
        choice = input("Use algorithm nr: ")

        if choice == "1":
            sorter = sorting("Bubble Sort")
            sorter.loop("bubble")
            del(sorter)
        elif choice == "2":
            sorter = sorting("Insertion Sort")
            sorter.loop("insertion")
            del(sorter)
        elif choice == "3":
            sorter = sorting("Selection Sort")
            sorter.loop("selection")
            del(sorter)
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    __main__()

