# SmartSaver: Investment Return Estimator
# Author: Ian Patricio
# Description: Simulates how an initial investment grows annually over 30 years.

# Starting funds and annual return rate
starting_funds = 1000.0       # dollars
growth_rate = 0.07            # 7% annual increase

# Header
print("📈 SmartSaver - 30-Year Investment Outlook 📈")
print("--------------------------------------------")
print(f"{'Year':<6}{'Projected Value ($)':>20}")
print("--------------------------------------------")

# Simulate year-by-year growth
for period in range(1, 31):
    value = starting_funds * ((1 + growth_rate) ** period)
    print(f"{period:<6}{value:>20,.2f}")