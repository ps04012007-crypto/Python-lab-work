import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [45000, 52000, 48000, 61000, 58000, 65000,
         62000, 70000, 68000, 75000, 72000, 80000]

# -------- LINE CHART --------

plt.figure()

plt.plot(months, sales, marker="o")

plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.title("Monthly Sales Revenue")

plt.grid()
plt.show()


# -------- BAR CHART --------

plt.figure()

plt.bar(months, sales)

plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.title("Monthly Sales Revenue")

plt.show()


# -------- HIGHEST AND LOWEST SALES --------

highest_sales = max(sales)
lowest_sales = min(sales)

highest_month = months[sales.index(highest_sales)]
lowest_month = months[sales.index(lowest_sales)]

print("Highest Sales:")
print(highest_month, "₹", highest_sales)

print("\nLowest Sales:")
print(lowest_month, "₹", lowest_sales)