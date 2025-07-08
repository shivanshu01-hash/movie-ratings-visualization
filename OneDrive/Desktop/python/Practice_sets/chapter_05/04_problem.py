# Demonstrates how set handles duplicate and different data types when adding elements
s = set()

s.add(20)
s.add(20.0)
s.add("20")

print(s)