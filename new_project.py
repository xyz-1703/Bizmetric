import pyodbc

class RestaurantSystem:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=LAPTOP-UIRB00PE\SQLEXPRESS;"
                "DATABASE=proj;"
                "Trusted_Connection=yes;"
            )
            self.cursor = self.conn.cursor()
            print("Database connected successfully.")
        except Exception as e:
            print("Database connection failed.")
            print("Error:", e)


    def show_menu(self):
        try:
            self.cursor.execute("SELECT id, name, price FROM menu")
            items = self.cursor.fetchall()

            print("\n------ MENU ------")
            for item in items:
                print(f"{item.id}. {item.name} - ${item.price}")

        except Exception as e:
            print("Error fetching menu:", e)


    def generate_order_id(self):
        try:
            self.cursor.execute("SELECT ISNULL(MAX(order_id),0) + 1 FROM orders")
            return self.cursor.fetchone()[0]
        except Exception as e:
            print("Error generating order ID:", e)
            return None

    def take_order(self):
        try:
            order_id = self.generate_order_id()

            if order_id is None:
                return

            print(f"\nNew Order ID: {order_id}")

            while True:
                self.show_menu()
                choice = input("Enter menu ID (or 'done'): ")

                if choice.lower() == "done":
                    break

                try:
                    choice = int(choice)
                    quantity = int(input("Enter quantity: "))

                    self.cursor.execute(
                        "SELECT id, name, price FROM menu WHERE id = ?",
                        (choice,)
                    )
                    item = self.cursor.fetchone()

                    if item:
                        item_id, name, price = item
                        total_price = float(price) * quantity

                        self.cursor.execute("""
                            INSERT INTO orders
                            (order_id, item_id, item_name, quantity, rate, total_price)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (order_id, item_id, name, quantity, price, total_price))

                        self.conn.commit()
                        print(f"{name} added successfully.")
                    else:
                        print("Invalid menu ID.")

                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                except Exception as e:
                    print("Error while adding item:", e)

            print("Order completed successfully.")

        except Exception as e:
            print("Error taking order:", e)

    def print_bill(self):
        try:
            order_id = int(input("Enter Order ID: "))

            self.cursor.execute("""
                SELECT item_name, quantity, rate, total_price
                FROM orders
                WHERE order_id = ?
            """, (order_id,))

            items = self.cursor.fetchall()

            if not items:
                print("Order not found.")
                return

            bill_text = f"\n------ BILL (Order {order_id}) ------\n"
            grand_total = 0

            for item in items:
                line = f"{item.item_name} x{item.quantity} @ ${item.rate} = ${item.total_price}"
                bill_text += line + "\n"
                grand_total += float(item.total_price)

            bill_text += "----------------------------\n"
            bill_text += f"Total Amount: ${grand_total}\n"

            print(bill_text)

            # Ask if user wants to download
            choice = input("Do you want to download this bill? (yes/no): ").lower()

            if choice == "yes":
                filename = f"bill_order_{order_id}.txt"
                with open(filename, "w") as file:
                    file.write(bill_text)
                print(f"Bill downloaded successfully as {filename}")

        except ValueError:
            print("Invalid order ID.")
        except Exception as e:
            print("Error generating bill:", e)



if __name__ == "__main__":
    system = RestaurantSystem()

    while True:
        print("\n1. Show Menu")
        print("2. Take Order")
        print("3. Print Bill")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.show_menu()

        elif choice == "2":
            system.take_order()

        elif choice == "3":
            system.print_bill()

        elif choice == "4":
            print("System closed. SQL Server still respects you.")
            break

        else:
            print("Invalid choice.")
