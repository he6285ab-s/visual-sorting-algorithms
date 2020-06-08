from sorting_window import sorting_window as sort_win

def __main__():
    
    while True:
        print("\nChoose an algorithm to sort with!")
        print("1: Bubble Sort")
        choice = input("Use algorithm nr: ")

        if choice == "1":
            sorter = sort_win()
            sorter.loop("bubble")
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    __main__()

