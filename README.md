# Ohm's Law and Power Calculator

## What it does
This Python program calculates voltage, current, resistance, and electrical power using common electrical formulas. It displays the formula used, gives answers with units, and keeps running until the user chooses to quit.

## How to run it
1. Install Python 3.
2. Save the code as `ohms_law.py`.
3. Open a terminal in the folder containing the file.
4. Run:

```bash
python ohms_law.py
```

On Android, you can paste the code into Pydroid 3 and press Run.

## Sample output

```text
=== Ohm's Law and Power Calculator ===
1. Calculate voltage
2. Calculate current
3. Calculate resistance
4. Calculate power
5. View calculation history
6. Quit
Choose an option (1-6): 1
Enter current in amperes (A): 2
Enter resistance in ohms (Ω): 5
Formula used: V = I × R
Voltage = 10.00 V
```

## My own twist
I added a calculation-history feature. It stores successful calculations during the current session and lets the user view them from the menu. The program also prints the formula used for each calculation and checks for invalid or non-positive number inputs.

## What I learned
I practised writing Python functions, using loops and conditional statements, converting user input to numbers, handling invalid input, and storing results in a list.

## Author
[Your Full Name], ND1 Mechatronics Engineering, YabaTech.
