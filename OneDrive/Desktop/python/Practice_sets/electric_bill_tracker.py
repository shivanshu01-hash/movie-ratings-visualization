electric_bills = [
    {"name": "Ramesh Sharma", "bill": 1350, "due_date": "15-07-2025"},
    {"name": "Sita Verma", "bill": 980, "due_date": "18-07-2025"},
    {"name": "Anil Kumar", "bill": 2100, "due_date": "12-07-2025"},
    {"name": "Priya Singh", "bill": 750, "due_date": "20-07-2025"},
    {"name": "Mohan Rao", "bill": 1625, "due_date": "16-07-2025"},
    {"name": "Kavita Joshi", "bill": 890, "due_date": "14-07-2025"},
    {"name": "Sunil Patel", "bill": 1200, "due_date": "19-07-2025"},
    {"name": "Farhan Ahmed", "bill": 1750, "due_date": "21-07-2025"},
    {"name": "Lakshmi Devi", "bill": 1050, "due_date": "13-07-2025"},
    {"name": "Rajesh Reddy", "bill": 950, "due_date": "17-07-2025"}
]
name = input("Enter your name: ")

bill = next((b for b in electric_bills if b["name"].lower() == name.lower()), None)

if bill:
    print(f"{name}, your bill of ₹{bill['bill']:.2f} is due: {bill['due_date']}")
else:
    print("Name not found in records.")
