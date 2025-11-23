from customer import Customer
from coffee import Coffee


def main():
    customers = {}
    coffees = {}

    print("Welcome to the Coffee Shop!")

    while True:
        print("\nOptions:")
        print("1: Create Customer")
        print("2: Create Coffee")
        print("3: Place Order")
        print("4: Show Customer Orders")
        print("5: Show Coffee Info")
        print("6: Most Aficionado for a Coffee")
        print("0: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            try:
                customer = Customer(name)
                customers[name] = customer
                print(f"Customer '{name}' created!")
            except ValueError as e:
                print(e)

        elif choice == "2":
            name = input("Enter coffee name: ")
            try:
                coffee = Coffee(name)
                coffees[name] = coffee
                print(f"Coffee '{name}' created!")
            except ValueError as e:
                print(e)

        elif choice == "3":
            cust_name = input("Enter customer name: ")
            coffee_name = input("Enter coffee name: ")
            price = float(input("Enter price (1.0 - 10.0): "))

            if cust_name not in customers or coffee_name not in coffees:
                print("Customer or Coffee does not exist.")
                continue

            customer = customers[cust_name]
            coffee = coffees[coffee_name]

            try:
                order = customer.create_order(coffee, price)
                print(f"Order placed: {cust_name} -> {coffee_name} for ${price}")
            except ValueError as e:
                print(e)

        elif choice == "4":
            cust_name = input("Enter customer name: ")
            if cust_name in customers:
                customer = customers[cust_name]
                print(f"Orders for {cust_name}:")
                for order in customer.orders():
                    print(f"- {order.coffee.name} at ${order.price}")
            else:
                print("Customer does not exist.")

        elif choice == "5":
            coffee_name = input("Enter coffee name: ")
            if coffee_name in coffees:
                coffee = coffees[coffee_name]
                print(f"{coffee_name} info:")
                print(f"- Orders: {coffee.num_orders()}")
                print(f"- Average price: ${coffee.average_price():.2f}")
                print(f"- Customers: {[c.name for c in coffee.customers()]}")
            else:
                print("Coffee does not exist.")

        elif choice == "6":
            coffee_name = input("Enter coffee name: ")
            if coffee_name in coffees:
                coffee = coffees[coffee_name]
                most = Customer.most_aficionado(coffee)
                if most:
                    print(f"Most aficionado: {most.name}")
                else:
                    print("No orders yet for this coffee.")
            else:
                print("Coffee does not exist.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
