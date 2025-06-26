#!/usr/bin/env python3
"""
Calculator CLI App
A command-line calculator supporting basic and advanced operations.

Author: Calculator CLI
Version: 1.0
"""

import math
import sys
from typing import Union, Optional

class Calculator:
    """A comprehensive calculator class with basic and advanced operations."""
    
    def __init__(self):
        """Initialize calculator with operation history."""
        self.history = []
        self.last_result = 0
    
    # Basic Operations
    def add(self, a: float, b: float) -> float:
        """Addition operation."""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtraction operation."""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiplication operation."""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Division operation with zero division check."""
        if b == 0:
            raise ValueError("Error: Cannot divide by zero!")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
    
    # Advanced Operations
    def power(self, a: float, b: float) -> float:
        """Power operation (a^b)."""
        result = a ** b
        self._add_to_history(f"{a}^{b} = {result}")
        return result
    
    def square_root(self, a: float) -> float:
        """Square root operation."""
        if a < 0:
            raise ValueError("Error: Cannot calculate square root of negative number!")
        result = math.sqrt(a)
        self._add_to_history(f"√{a} = {result}")
        return result
    
    def percentage(self, a: float, b: float) -> float:
        """Calculate percentage (a% of b)."""
        result = (a / 100) * b
        self._add_to_history(f"{a}% of {b} = {result}")
        return result
    
    def modulo(self, a: float, b: float) -> float:
        """Modulo operation (remainder)."""
        if b == 0:
            raise ValueError("Error: Cannot perform modulo with zero!")
        result = a % b
        self._add_to_history(f"{a} mod {b} = {result}")
        return result
    
    # Trigonometric Operations
    def sin(self, a: float) -> float:
        """Sine operation (in degrees)."""
        result = math.sin(math.radians(a))
        self._add_to_history(f"sin({a}°) = {result}")
        return result
    
    def cos(self, a: float) -> float:
        """Cosine operation (in degrees)."""
        result = math.cos(math.radians(a))
        self._add_to_history(f"cos({a}°) = {result}")
        return result
    
    def tan(self, a: float) -> float:
        """Tangent operation (in degrees)."""
        result = math.tan(math.radians(a))
        self._add_to_history(f"tan({a}°) = {result}")
        return result
    
    # Logarithmic Operations
    def log(self, a: float, base: float = math.e) -> float:
        """Logarithm operation."""
        if a <= 0:
            raise ValueError("Error: Logarithm undefined for non-positive numbers!")
        if base <= 0 or base == 1:
            raise ValueError("Error: Invalid logarithm base!")
        
        if base == math.e:
            result = math.log(a)
            self._add_to_history(f"ln({a}) = {result}")
        else:
            result = math.log(a, base)
            self._add_to_history(f"log₍{base}₎({a}) = {result}")
        return result
    
    # Utility Functions
    def _add_to_history(self, operation: str) -> None:
        """Add operation to history."""
        self.history.append(operation)
        if len(self.history) > 50:  # Keep only last 50 operations
            self.history.pop(0)
    
    def show_history(self) -> None:
        """Display calculation history."""
        if not self.history:
            print("No calculations performed yet.")
            return
        
        print("\n" + "="*50)
        print("CALCULATION HISTORY")
        print("="*50)
        for i, operation in enumerate(self.history[-10:], 1):  # Show last 10
            print(f"{i:2d}. {operation}")
        print("="*50)
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
        print("History cleared!")


class CalculatorCLI:
    """Command Line Interface for the Calculator."""
    
    def __init__(self):
        """Initialize CLI with calculator instance."""
        self.calc = Calculator()
        self.operations = {
            '1': ('Addition', self._handle_binary_operation, self.calc.add),
            '2': ('Subtraction', self._handle_binary_operation, self.calc.subtract),
            '3': ('Multiplication', self._handle_binary_operation, self.calc.multiply),
            '4': ('Division', self._handle_binary_operation, self.calc.divide),
            '5': ('Power', self._handle_binary_operation, self.calc.power),
            '6': ('Square Root', self._handle_unary_operation, self.calc.square_root),
            '7': ('Percentage', self._handle_binary_operation, self.calc.percentage),
            '8': ('Modulo', self._handle_binary_operation, self.calc.modulo),
            '9': ('Sine', self._handle_unary_operation, self.calc.sin),
            '10': ('Cosine', self._handle_unary_operation, self.calc.cos),
            '11': ('Tangent', self._handle_unary_operation, self.calc.tan),
            '12': ('Natural Log', self._handle_unary_operation, self.calc.log),
            '13': ('Logarithm', self._handle_logarithm, None),
        }
    
    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "="*60)
        print("🧮 ADVANCED CALCULATOR CLI")
        print("="*60)
        print("Basic Operations:")
        print("  1. Addition (+)")
        print("  2. Subtraction (-)")
        print("  3. Multiplication (×)")
        print("  4. Division (÷)")
        print("\nAdvanced Operations:")
        print("  5. Power (^)")
        print("  6. Square Root (√)")
        print("  7. Percentage (%)")
        print("  8. Modulo (mod)")
        print("\nTrigonometric Functions:")
        print("  9. Sine (sin)")
        print(" 10. Cosine (cos)")
        print(" 11. Tangent (tan)")
        print("\nLogarithmic Functions:")
        print(" 12. Natural Logarithm (ln)")
        print(" 13. Logarithm (log)")
        print("\nUtility Options:")
        print("  h. Show History")
        print("  c. Clear History")
        print("  q. Quit")
        print("="*60)
    
    def get_number(self, prompt: str) -> float:
        """Get a number from user input with validation."""
        while True:
            try:
                value = input(prompt).strip()
                if value.lower() == 'last' and hasattr(self.calc, 'last_result'):
                    return self.calc.last_result
                return float(value)
            except ValueError:
                print("❌ Invalid input! Please enter a valid number or 'last' for last result.")
    
    def _handle_binary_operation(self, operation_func) -> None:
        """Handle operations that require two numbers."""
        print(f"\n--- {operation_func.__doc__} ---")
        num1 = self.get_number("Enter first number (or 'last' for last result): ")
        num2 = self.get_number("Enter second number (or 'last' for last result): ")
        
        try:
            result = operation_func(num1, num2)
            self.calc.last_result = result
            print(f"✅ Result: {result}")
        except ValueError as e:
            print(f"❌ {e}")
    
    def _handle_unary_operation(self, operation_func) -> None:
        """Handle operations that require one number."""
        print(f"\n--- {operation_func.__doc__} ---")
        num = self.get_number("Enter number (or 'last' for last result): ")
        
        try:
            result = operation_func(num)
            self.calc.last_result = result
            print(f"✅ Result: {result}")
        except ValueError as e:
            print(f"❌ {e}")
    
    def _handle_logarithm(self, _) -> None:
        """Handle logarithm with custom base."""
        print("\n--- Logarithm Operation ---")
        num = self.get_number("Enter number (or 'last' for last result): ")
        base = self.get_number("Enter base (or press Enter for base 10): ")
        
        if base == 0:  # User pressed Enter
            base = 10
        
        try:
            result = self.calc.log(num, base)
            self.calc.last_result = result
            print(f"✅ Result: {result}")
        except ValueError as e:
            print(f"❌ {e}")
    
    def run(self) -> None:
        """Main application loop."""
        print("🎉 Welcome to the Advanced Calculator CLI!")
        print("💡 Tip: You can type 'last' to use the result from your previous calculation")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip().lower()
            
            if choice == 'q':
                print("\n👋 Thank you for using Calculator CLI!")
                print("🔢 Total calculations performed:", len(self.calc.history))
                sys.exit(0)
            
            elif choice == 'h':
                self.calc.show_history()
            
            elif choice == 'c':
                self.calc.clear_history()
            
            elif choice in self.operations:
                operation_name, handler, operation_func = self.operations[choice]
                handler(operation_func)
            
            else:
                print("❌ Invalid choice! Please select from the menu options.")
            
            # Pause before showing menu again
            input("\nPress Enter to continue...")


def main():
    """Main function to run the calculator."""
    try:
        calculator_cli = CalculatorCLI()
        calculator_cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 Calculator CLI terminated by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


# Example usage and testing functions
def run_examples():
    """Run some example calculations for demonstration."""
    print("🧪 Running Calculator Examples...")
    calc = Calculator()
    
    # Basic operations
    print("Basic Operations:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 3 = {calc.subtract(10, 3)}")
    print(f"4 × 7 = {calc.multiply(4, 7)}")
    print(f"15 ÷ 3 = {calc.divide(15, 3)}")
    
    # Advanced operations
    print("\nAdvanced Operations:")
    print(f"2^8 = {calc.power(2, 8)}")
    print(f"√64 = {calc.square_root(64)}")
    print(f"15% of 200 = {calc.percentage(15, 200)}")
    
    # Show history
    calc.show_history()

# Uncomment the line below to run examples
# run_examples()