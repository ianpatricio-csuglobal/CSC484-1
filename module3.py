"""
Title: Daily Hydration Logger with Statistics
Author: Ian Patricio
Description:
    This program tracks the user's daily water intake in glasses and logs it with a timestamp.
    It calculates the total, average intake, and how close the user is to the daily goal.
    The program demonstrates exception handling using try, except, and finally blocks.
    Promotes health awareness through hydration encouragement and daily logging.
"""

from datetime import datetime

def hydration_logger():
    print("=" * 69)
    print("Daily Hydration Logger – Stay Refreshed!")
    print("Track your water intake and see your hydration stats.")
    print("=" * 69)

    log = []

    try:
        entries = int(input("\nHow many times did you drink water today? (e.g., 3 times): "))

        if entries <= 0:
            raise ValueError("Number of entries must be a positive number.")

        for i in range(1, entries + 1):
            try:
                glasses = float(input(f"  ➤ Entry #{i}: How many glasses did you drink? "))
                if glasses < 0:
                    raise ValueError("Glasses cannot be negative.")
                timestamp = datetime.now().strftime("%H:%M:%S")
                log.append((timestamp, glasses))
            except ValueError as ve_inner:
                print(f"    Skipping entry due to error: {ve_inner}")
                continue

        total = sum(g[1] for g in log)
        average = total / len(log) if log else 0
        goal = 8  # 8 glasses per day recommended
        goal_diff = total - goal

        print("\nHydration Summary:")
        print(f"  Entries logged: {len(log)}")
        print(f"  Total water intake: {total:.1f} glasses")
        print(f"  Average per entry: {average:.2f} glasses")
        print(f"  Goal difference: {'+' if goal_diff >= 0 else ''}{goal_diff:.1f} glasses")

        if total >= goal:
            print("  You met your hydration goal today! Great work! 🌟")
        else:
            print("  Keep sipping! You're almost there!")

    except ValueError as ve:
        print(f"\nInput Error: {ve}")

    finally:
        print("\nWellness Tip: Drink a glass of water when you wake up, before meals, and before bed.")
        print("Thank you for using the Hydration Logger")

# Run the program
hydration_logger()
