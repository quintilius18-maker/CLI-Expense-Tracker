'''

Program entry point
Menu display
User interaction
Navigation

'''

if __name__ == "__main__":
    pass

def main():
    print('-' * 100)
    print('Welcome to the CLI Tracker!')
    print('Please select an option:')
    print('1. Add expense')
    print('2. View expenses')
    print('3. Search expenses')
    print('4. Monthly Summary')
    print('5. Delete expense')
    print('6. Exit')
    exit = False
    while not exit:
        choice = input('Enter your choice: ')
        if choice == '1':
            # Add expense
            pass
        elif choice == '2':
            # View expenses
            pass
        elif choice == '3':
            # Search expenses
            pass
        elif choice == '4':
            # Monthly summary
            pass
        elif choice == '5':
            # Delete expense
            pass
        elif choice == '6':
            exit = True
        else:
            print('Invalid choice. Please try again.')

main()