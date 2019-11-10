import matplotlib.pyplot as plt
%matplotlib inline

expense_labels = ["Home Rent", "Food", "phone/Internet Bill", "Car", "Other Utilities"]
expense_values = [1400, 600, 300, 410, 250]

plt.pie(expense_values, labels = expense_labels, radius = 2, 
        autopct='%.2f%%', shadow=True, 
        explode=[0, 0.1, 0, 0, 0],
        startangle=180)

plt.savefig("piechart_expenses.png", bbox_inches="tight", padinches=1, transprent=True)
plt.savefig("c:/users/anand/Exercises/Ex_MatplotLib/piechart_expenses.pdf", bbox_inches="tight", padinches=1, transprent=True)

plt.show()