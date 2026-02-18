class CourseCalculator:

    # allowed courses
    courses = {
        "hr": "HR",
        "human resource": "HR",
        "finance": "Finance",
        "marketing": "Marketing",
        "ds": "DS",
        "data science": "DS"
    }

    analytics_available = ["HR", "Finance", "Marketing"]

    BASE_FEES = 200000
    HOSTEL_FEES = 200000
    FOOD_PER_MONTH = 2000
    TRANSPORT_PER_SEM = 13000


    # ---------- COURSE ----------
    def get_course(self):
        while True:
            try:
                subject = input(
                    "Enter course (HR / Finance / Marketing / DS): "
                ).lower()

                if subject in self.courses:
                    return self.courses[subject]
                else:
                    print("Invalid course. Try again.")

            except Exception as e:
                print("Error:", e)


    # ---------- ANALYTICS ----------
    def get_analytics(self, subject):

        if subject not in self.analytics_available:
            print("Analytics not available for this course.")
            return "N"

        while True:
            choice = input("Do you want analytics? (Y/N): ").upper()
            if choice in ["Y", "N"]:
                return choice
            print("Please enter Y or N.")


    # ---------- HOSTEL ----------
    def get_hostel(self):
        while True:
            choice = input("Hostel needed? (Y/N): ").upper()
            if choice in ["Y", "N"]:
                return choice
            print("Please enter Y or N.")


    # ---------- FOOD ----------
    def get_food_months(self):
        while True:
            try:
                months = int(input("Food months: "))
                if months >= 0:
                    return months
                else:
                    print("Months cannot be negative.")
            except ValueError:
                print("Enter valid number.")


    # ---------- TRANSPORT ----------
    def get_transport(self):
        while True:
            try:
                choice = input(
                    "Transport option (semester / annual / none): "
                ).lower()

                if choice == "semester":
                    sem = int(input("How many semesters? "))

                    if sem <= 0:
                        print("Semesters must be positive.")
                        continue

                    return sem * self.TRANSPORT_PER_SEM

                elif choice == "annual":
                    return 2 * self.TRANSPORT_PER_SEM

                elif choice == "none":
                    return 0

                else:
                    print("Invalid option. Try again.")

            except ValueError:
                print("Enter numeric value for semesters.")


    # ---------- TOTAL ----------
    def calculate_total(self, analytics, hostel, food_months, transport):

        total = self.BASE_FEES

        if analytics == "Y":
            total += self.BASE_FEES * 0.10

        if hostel == "Y":
            total += self.HOSTEL_FEES

        total += food_months * self.FOOD_PER_MONTH
        total += transport

        return total


    # ---------- BILL ----------
    def print_bill(self, subject, analytics, hostel,
                   food_months, transport, total):

        print("\n------ TOTAL ANNUAL COST ------")
        print("Course:", subject)
        print("Analytics:", analytics)
        print("Hostel:", hostel)
        print("Food months:", food_months)
        print("Transport charges:", transport)
        print("TOTAL COST =", int(total))


# ================= MAIN =================
if __name__ == "__main__":

    system = CourseCalculator()

    subject = system.get_course()
    analytics = system.get_analytics(subject)
    hostel = system.get_hostel()
    food_months = system.get_food_months()
    transport = system.get_transport()

    total = system.calculate_total(
        analytics, hostel, food_months, transport
    )

    system.print_bill(
        subject, analytics, hostel,
        food_months, transport, total
    )
