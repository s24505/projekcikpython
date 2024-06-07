import json

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cash_assigned = None

    def __str__(self):
        return f"ID: {self.id}, Imie: {self.name}, Przypisana kasa: {self.cash_assigned}"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "cash_assigned": self.cash_assigned}

    @staticmethod
    def from_dict(data):
        employee = Employee(data["id"], data["name"])
        employee.cash_assigned = data["cash_assigned"]
        return employee


class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id}, Nazwa: {self.name}, Cena: ${self.price}, Liczba produktow: {self.quantity}"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "quantity": self.quantity}

    @staticmethod
    def from_dict(data):
        return Product(data["id"], data["name"], data["price"], data["quantity"])


class Cash:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
        self.cashier = None

    def assign_cashier(self, employee):
        if self.cashier:
            print(f"Usuwam kasjera {self.cashier.name} z kasy {self.id}")
            self.cashier.cash_assigned = None
        self.cashier = employee
        employee.cash_assigned = self.id

    def __str__(self):
        return f"ID: {self.id}, Kasa: ${self.amount}, Kasjer: {self.cashier.name if self.cashier else 'Brak'}"

    def to_dict(self):
        return {"id": self.id, "amount": self.amount, "cashier_id": self.cashier.id if self.cashier else None}

    @staticmethod
    def from_dict(data, employees):
        cash = Cash(data["id"], data["amount"])
        cashier_id = data.get("cashier_id")
        if cashier_id and cashier_id in employees:
            cash.assign_cashier(employees[cashier_id])
        return cash


class Store:
    def __init__(self):
        self.employees = {}
        self.products = {}
        self.cashes = {}

    def add_employee(self, id, name):
        if id in self.employees:
            print("ID pracownika istnieje.")
            return
        self.employees[id] = Employee(id, name)
        self.save_data()

    def edit_employee(self, id, new_name):
        if id not in self.employees:
            print("Pracownik nie znaleziony.")
            return
        self.employees[id].name = new_name
        self.save_data()

    def remove_employee(self, id):
        if id not in self.employees:
            print("Pracownik nie znaleziony.")
            return
        employee = self.employees.pop(id)
        if employee.cash_assigned:
            self.cashes[employee.cash_assigned].cashier = None
        self.save_data()

    def add_product(self, id, name, price, quantity):
        if id in self.products:
            print("Produkt o takim ID juz istnieje.")
            return
        self.products[id] = Product(id, name, price, quantity)
        self.save_data()

    def edit_product(self, id, name, price, quantity):
        if id not in self.products:
            print("Produkt nie znaleziony.")
            return
        product = self.products[id]
        product.name = name
        product.price = price
        product.quantity = quantity
        self.save_data()

    def remove_product(self, id):
        if id not in self.products:
            print("Produkt nie znaleziony.")
            return
        self.products.pop(id)
        self.save_data()

    def add_cash(self, id, amount):
        if id in self.cashes:
            print("Kasa o takim numerze istnieje.")
            return
        self.cashes[id] = Cash(id, amount)
        self.save_data()

    def assign_cashier_to_cash(self, cash_id, employee_id):
        if cash_id not in self.cashes:
            print("Kasa nie znaleziona.")
            return
        if employee_id not in self.employees:
            print("Pracownik nie znaleziony.")
            return
        cash = self.cashes[cash_id]
        employee = self.employees[employee_id]
        cash.assign_cashier(employee)
        self.save_data()

    def display_employees(self):
        for employee in self.employees.values():
            print(employee)

    def display_products(self):
        for product in self.products.values():
            print(product)

    def display_cashes(self):
        for cash in self.cashes.values():
            print(cash)

    def save_data(self):
        with open("employees.json", "w") as f:
            json.dump([e.to_dict() for e in self.employees.values()], f)
        with open("products.json", "w") as f:
            json.dump([p.to_dict() for p in self.products.values()], f)
        with open("cashes.json", "w") as f:
            json.dump([c.to_dict() for c in self.cashes.values()], f)

    def load_data(self):
        try:
            with open("employees.json", "r") as f:
                employees = json.load(f)
                for data in employees:
                    employee = Employee.from_dict(data)
                    self.employees[employee.id] = employee
        except FileNotFoundError:
            pass

        try:
            with open("products.json", "r") as f:
                products = json.load(f)
                for data in products:
                    product = Product.from_dict(data)
                    self.products[product.id] = product
        except FileNotFoundError:
            pass

        try:
            with open("cashes.json", "r") as f:
                cashes = json.load(f)
                for data in cashes:
                    cash = Cash.from_dict(data, self.employees)
                    self.cashes[cash.id] = cash
        except FileNotFoundError:
            pass


def main():
    store = Store()
    store.load_data()

    while True:
        print("\nWitamy w sklepie, wybierz opcje aby kontynuowac:")
        print("1. Zarzadzaj pracownikami")
        print("2. Zarzadzaj produktami")
        print("3. Zarzadzaj kasami")
        print("4. Wyjscie")

        choice = input("Podaj wybor: ")

        if choice == '1':
            print("\n1. Dodaj pracownika")
            print("2. Edytuj pracownika")
            print("3. Usun pracownika")
            print("4. Wyswietl pracownikow")
            print("5. Powrot do menu")

            emp_choice = input("Podaj wybor: ")

            if emp_choice == '1':
                id = input("Podaj ID nowego pracownika: ")
                name = input("Podaj imie nowego pracownika: ")
                store.add_employee(id, name)
            elif emp_choice == '2':
                id = input("Podaj ID pracownika: ")
                name = input("Podaj imie pracownika: ")
                store.edit_employee(id, name)
            elif emp_choice == '3':
                id = input("Podaj ID pracownika: ")
                store.remove_employee(id)
            elif emp_choice == '4':
                store.display_employees()
            elif emp_choice == '5':
                continue
            else:
                print("Niepoprawny wybor.")

        elif choice == '2':
            print("\n1. Dodaj produkt")
            print("2. Edytuj produkt")
            print("3. Usun produkt")
            print("4. Wyswietl produkty")
            print("5. Powrot do menu")

            prod_choice = input("Podaj wybor: ")

            if prod_choice == '1':
                id = input("Podaj ID nowego produktu: ")
                name = input("Podaj nazwe nowego produktu: ")
                price = float(input("Podaj cene produktu: "))
                quantity = int(input("Podaj ilosc produktu: "))
                store.add_product(id, name, price, quantity)
            elif prod_choice == '2':
                id = input("Podaj ID produktu: ")
                name = input("Podaj nowa nazwe produktu: ")
                price = float(input("Podaj nowa cene produktu: "))
                quantity = int(input("Podaj ilosc produktu: "))
                store.edit_product(id, name, price, quantity)
            elif prod_choice == '3':
                id = input("Podaj ID produktu: ")
                store.remove_product(id)
            elif prod_choice == '4':
                store.display_products()
            elif prod_choice == '5':
                continue
            else:
                print("Niepoprawny wybor.")

        elif choice == '3':
            print("\n1. Dodaj kase")
            print("2. Przypisz kasjera do kasy")
            print("3. Wyswietl kasy")
            print("4. Powrot do menu")

            cash_choice = input("Podaj wybor: ")

            if cash_choice == '1':
                id = input("Podaj ID kasy: ")
                amount = float(input("Podaj ilosc pieniedzy w kase: "))
                store.add_cash(id, amount)
            elif cash_choice == '2':
                cash_id = input("Podaj ID kasy: ")
                employee_id = input("Podaj ID pracowika do przypisania: ")
                store.assign_cashier_to_cash(cash_id, employee_id)
            elif cash_choice == '3':
                store.display_cashes()
            elif cash_choice == '4':
                continue
            else:
                print("Niepoprawny wybor.")

        elif choice == '4':
            print("Zamykanie programu.")
            break

        else:
            print("Niepoprawny wybor.")


if __name__ == "__main__":
    main()
