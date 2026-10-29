"""
Ohm's Law and Power Calculator
A beginner-friendly Python mini project for ND1 Mechatronics Engineering.
"""

# Store each successful calculation so the user can review it later.
calculation_history = []


def get_positive_number(prompt):
    """Ask for a number greater than zero and handle invalid input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number, such as 12 or 2.5.")


def calculate_voltage():
    """Calculate voltage using V = I * R."""
    current = get_positive_number("Enter current in amperes (A): ")
    resistance = get_positive_number("Enter resistance in ohms (Ω): ")
    voltage = current * resistance
    formula = "V = I × R"
    result = f"Voltage = {voltage:.2f} V"
    print(f"Formula used: {formula}")
    print(result)
    calculation_history.append(f"{formula}: {result}")


def calculate_current():
    """Calculate current using I = V / R."""
    voltage = get_positive_number("Enter voltage in volts (V): ")
    resistance = get_positive_number("Enter resistance in ohms (Ω): ")
    current = voltage / resistance
    formula = "I = V / R"
    result = f"Current = {current:.2f} A"
    print(f"Formula used: {formula}")
    print(result)
    calculation_history.append(f"{formula}: {result}")


def calculate_resistance():
    """Calculate resistance using R = V / I."""
    voltage = get_positive_number("Enter voltage in volts (V): ")
    current = get_positive_number("Enter current in amperes (A): ")
    resistance = voltage / current
    formula = "R = V / I"
    result = f"Resistance = {resistance:.2f} Ω"
    print(f"Formula used: {formula}")
    print(result)
    calculation_history.append(f"{formula}: {result}")


def calculate_power():
    """Calculate electrical power using one of three valid formula pairs."""
    print("\nChoose the known values:")
    print("1. Voltage and current (P = V × I)")
    print("2. Current and resistance (P = I² × R)")
    print("3. Voltage and resistance (P = V² / R)")

    while True:
        choice = input("Choose 1, 2, or 3: ").strip()
        if choice == "1":
            voltage = get_positive_number("Enter voltage in volts (V): ")
            current = get_positive_number("Enter current in amperes (A): ")
            power = voltage * current
            formula = "P = V × I"
            break
        elif choice == "2":
            current = get_positive_number("Enter current in amperes (A): ")
            resistance = get_positive_number("Enter resistance in ohms (Ω): ")
            power = current ** 2 * resistance
            formula = "P = I² × R"
            break
        elif choice == "3":
            voltage = get_positive_number("Enter voltage in volts (V): ")
            resistance = get_positive_number("Enter resistance in ohms (Ω): ")
            power = voltage ** 2 / resistance
            formula = "P = V² / R"
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

    result = f"Power = {power:.2f} W"
    print(f"Formula used: {formula}")
    print(result)
    calculation_history.append(f"{formula}: {result}")


def show_history():
    """Display previous calculations; this is the project's extra feature."""
    if not calculation_history:
        print("No calculations have been made yet.")
    else:
        print("\n--- Calculation History ---")
        for number, item in enumerate(calculation_history, start=1):
            print(f"{number}. {item}")


def main():
    """Display the menu and repeat until the user chooses to quit."""
    while True:
        print("\n=== Ohm's Law and Power Calculator ===")
        print("1. Calculate voltage")
        print("2. Calculate current")
        print("3. Calculate resistance")
        print("4. Calculate power")
        print("5. View calculation history")
        print("6. Quit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            calculate_voltage()
        elif choice == "2":
            calculate_current()
        elif choice == "3":
            calculate_resistance()
        elif choice == "4":
            calculate_power()
        elif choice == "5":
            show_history()
        elif choice == "6":
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid menu option. Please enter a number from 1 to 6.")


# Start the program when this file is run directly.
if __name__ == "__main__":
    main()
