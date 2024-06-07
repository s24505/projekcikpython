# Patryk Niedźwiecki
# s24505

# Dokumentacja Projektu Zarządzania Sklepem

## Opis ogólny

Aplikacja zarządzania sklepem umożliwia zarządzanie pracownikami, produktami i kasami w sklepie. Użytkownik może dodawać, edytować, usuwać i wyświetlać pracowników oraz produkty, a także zarządzać kasami, przypisując do nich pracowników. Aplikacja zapisuje dane do plików JSON, aby zachować stan między uruchomieniami.

## Klasa `Employee`

### Działanie

Klasa `Employee` reprezentuje pracownika sklepu. Każdy pracownik ma unikalne ID, imię oraz może być przypisany do kasy. Pracownik może być skonwertowany na słownik (do zapisu) oraz utworzony ze słownika (podczas odczytu).

### Metody

- `__init__(self, id, name)`: Inicjalizuje nowego pracownika z podanym ID i imieniem.
- `__str__(self)`: Zwraca reprezentację tekstową pracownika, w tym przypisaną kasę.
- `to_dict(self)`: Zwraca słownik reprezentujący pracownika.
- `from_dict(data)`: Tworzy obiekt `Employee` na podstawie słownika.

## Klasa `Product`

### Działanie

Klasa `Product` reprezentuje produkt w sklepie. Każdy produkt ma unikalne ID, nazwę, cenę oraz ilość. Produkt może być skonwertowany na słownik (do zapisu) oraz utworzony ze słownika (podczas odczytu).

### Metody

- `__init__(self, id, name, price, quantity)`: Inicjalizuje nowy produkt z podanym ID, nazwą, ceną i ilością.
- `__str__(self)`: Zwraca reprezentację tekstową produktu.
- `to_dict(self)`: Zwraca słownik reprezentujący produkt.
- `from_dict(data)`: Tworzy obiekt `Product` na podstawie słownika.

## Klasa `Cash`

### Działanie

Klasa `Cash` reprezentuje kasę w sklepie. Każda kasa ma unikalne ID, ilość pieniędzy oraz może mieć przypisanego pracownika (kasjera). Kasa może być skonwertowana na słownik (do zapisu) oraz utworzona ze słownika (podczas odczytu).

### Metody

- `__init__(self, id, amount)`: Inicjalizuje nową kasę z podanym ID i ilością pieniędzy.
- `assign_cashier(self, employee: Employee)`: Przypisuje pracownika do kasy. Jeśli kasa miała przypisanego kasjera, zostaje on usunięty.
- `__str__(self)`: Zwraca reprezentację tekstową kasy, w tym przypisanego kasjera.
- `to_dict(self)`: Zwraca słownik reprezentujący kasę.
- `from_dict(data, employees)`: Tworzy obiekt `Cash` na podstawie słownika i dostępnych pracowników.

## Klasa `Store`

### Działanie

Klasa `Store` zarządza pracownikami, produktami i kasami. Umożliwia dodawanie, edytowanie, usuwanie i wyświetlanie tych elementów oraz przypisywanie kasjerów do kas. Klasa ta zawiera również metody do zapisywania i ładowania danych z plików JSON.

### Metody

- `__init__(self)`: Inicjalizuje nowy sklep z pustymi słownikami pracowników, produktów i kas.
- `add_employee(self, id, name)`: Dodaje nowego pracownika.
- `edit_employee(self, id, new_name)`: Edytuje dane pracownika.
- `remove_employee(self, id)`: Usuwa pracownika, usuwając jednocześnie przypisanie do kasy (jeśli istnieje).
- `add_product(self, id, name, price, quantity)`: Dodaje nowy produkt.
- `edit_product(self, id, name, price, quantity)`: Edytuje dane produktu.
- `remove_product(self, id)`: Usuwa produkt.
- `add_cash(self, id, amount)`: Dodaje nową kasę.
- `assign_cashier_to_cash(self, cash_id, employee_id)`: Przypisuje kasjera do kasy.
- `display_employees(self)`: Wyświetla wszystkich pracowników.
- `display_products(self)`: Wyświetla wszystkie produkty.
- `display_cashes(self)`: Wyświetla wszystkie kasy.
- `save_data(self)`: Zapisuje dane pracowników, produktów i kas do plików JSON.
- `load_data(self)`: Ładuje dane pracowników, produktów i kas z plików JSON.

## Funkcja `main`

### Działanie

Funkcja `main` uruchamia aplikację i obsługuje interfejs użytkownika, umożliwiając wybór operacji zarządzania pracownikami, produktami i kasami.

### Operacje

1. **Zarządzanie pracownikami:**
   - **Dodawanie pracownika:** Użytkownik podaje ID i imię nowego pracownika, który jest dodawany do sklepu.
   - **Edytowanie pracownika:** Użytkownik podaje ID i nowe imię pracownika, którego dane są aktualizowane.
   - **Usuwanie pracownika:** Użytkownik podaje ID pracownika, który jest usuwany ze sklepu.
   - **Wyświetlanie pracowników:** Lista wszystkich pracowników jest wyświetlana na ekranie.

2. **Zarządzanie produktami:**
   - **Dodawanie produktu:** Użytkownik podaje ID, nazwę, cenę i ilość nowego produktu, który jest dodawany do sklepu.
   - **Edytowanie produktu:** Użytkownik podaje ID, nową nazwę, cenę i ilość produktu, którego dane są aktualizowane.
   - **Usuwanie produktu:** Użytkownik podaje ID produktu, który jest usuwany ze sklepu.
   - **Wyświetlanie produktów:** Lista wszystkich produktów jest wyświetlana na ekranie.

3. **Zarządzanie kasami:**
   - **Dodawanie kasy:** Użytkownik podaje ID i ilość pieniędzy w nowej kasie, która jest dodawana do sklepu.
   - **Przypisywanie kasjera do kasy:** Użytkownik podaje ID kasy i ID pracownika, który ma zostać przypisany do kasy.
   - **Wyświetlanie kas:** Lista wszystkich kas jest wyświetlana na ekranie.

4. **Zamykanie programu:** Program kończy działanie, zapisując dane do plików JSON.

### Uwagi

- **Przechowywanie danych:** Aplikacja zapisuje dane do plików `employees.json`, `products.json` oraz `cashes.json`, co umożliwia utrwalenie stanu pomiędzy uruchomieniami programu.
- **Integralność danych:** Aby zapewnić integralność danych, należy zawsze używać metod `save_data` i `load_data` do zapisywania i ładowania stanu aplikacji.
- **Interfejs użytkownika:** Aplikacja działa w trybie tekstowym, pozwalając użytkownikowi na wybór opcji poprzez podanie odpowiednich numerów operacji.
