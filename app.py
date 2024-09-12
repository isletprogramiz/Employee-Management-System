from functions import EmployeeRegister, EmployeeLogin, EmployeeUpdate, EmployeeRemove

def show_main_menu():
    print("Choose an option:")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Register as New User")

def show_admin_menu():
    print("Admin Menu:")
    print("1. Update Employee Details")
    print("2. Remove Employee")
    print("3. View All Details")

def show_user_menu():
    print("User Menu:")
    print("1. View Your Details")

def main():
    while True:
        show_main_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Admin Login
            admin = EmployeeLogin()
            if admin:
                show_admin_menu()
                admin_choice = int(input("Enter your choice: "))
                
                if admin_choice == 1:
                    EmployeeUpdate()
                elif admin_choice == 2:
                    EmployeeRemove()
                elif admin_choice == 3:
                    EmployeeLogin()
                else:
                    print("Invalid choice")
        elif choice == 2:
            # User Login
            user = EmployeeLogin()
            if user:
                show_user_menu()
                user_choice = int(input("Enter your choice: "))
                
                if user_choice == 1:
                    print(user)  # Display user details
                else:
                    print("Invalid choice")
        elif choice == 3:
            # Register as New User
            EmployeeRegister()
            print("Registration successful. You can now login to view your details.")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
