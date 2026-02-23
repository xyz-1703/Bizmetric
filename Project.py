class CourseSystem:

    courses = [
        "hr", "finance", "marketing", "ds",
        "data science", "human resource"
    ]

    analytics_available = [
        "hr", "finance", "marketing", "human resource"
    ]

    BASE_FEES = 200000
    HOSTEL_FEES = 200000
    FOOD_PER_MONTH = 2000
    TRANSPORT_PER_SEM = 13000

    def __init__(self):
        self.subject = ""
        self.analytics = "N"
        self.hostel = "N"
        self.food_months = 0
        self.transport = 0

    def get_course(self):
        subject = input("Enter course (HR/Finance/Marketing/DS): ").lower()
        if subject in self.courses:
            self.subject = subject
        else:
            print("Invalid course!")

    def get_analytics(self):
        if self.subject not in self.analytics_available:
            print("Analytics not available.")
            return

        choice = input("Do you want analytics? (Y/N): ").upper()
        if choice in ["Y", "N"]:
            self.analytics = choice
        else:
            print("Invalid choice. Taking N.")

    def get_hostel(self):
        choice = input("Hostel required? (Y/N): ").upper()
        if choice in ["Y", "N"]:
            self.hostel = choice
        else:
            print("Invalid choice. Taking N.")

    def get_food(self):
        try:
            months = int(input("Food months: "))
            if months >= 0:
                self.food_months = months
            else:
                print("Invalid months.")
        except:
            print("Invalid input.")

    def get_transport(self):
        try:
            choice = input("Transport (semester/annual): ").lower()

            if choice == "semester":
                sem = int(input("How many semesters? "))
                self.transport = sem * self.TRANSPORT_PER_SEM

            elif choice == "annual":
                self.transport = 2 * self.TRANSPORT_PER_SEM

            else:
                print("Invalid option.")

        except:
            print("Invalid input.")


    def calculate_total(self):
        total = self.BASE_FEES

        if self.analytics == "Y":
            total += self.BASE_FEES * 0.10

        if self.hostel == "Y":
            total += self.HOSTEL_FEES

        total += self.food_months * self.FOOD_PER_MONTH
        total += self.transport

        return total

  
    def show_bill(self):
        total = self.calculate_total()
        print("\n------ TOTAL ANNUAL COST ------")
        print("Course:", self.subject)
        print("Analytics:", self.analytics)
        print("Hostel:", self.hostel)
        print("Food months:", self.food_months)
        print("Transport:", self.transport)
        print("TOTAL =", int(total))


def menu():
    system = CourseSystem()

    while True:
        print("\n1. Enter Course")
        print("2. Add Analytics")
        print("3. Add Hostel")
        print("4. Add Food")
        print("5. Add Transport")
        print("6. Show Bill")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.get_course()

        elif choice == "2":
            system.get_analytics()

        elif choice == "3":
            system.get_hostel()

        elif choice == "4":
            system.get_food()

        elif choice == "5":
            system.get_transport()

        elif choice == "6":
            system.show_bill()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


menu()