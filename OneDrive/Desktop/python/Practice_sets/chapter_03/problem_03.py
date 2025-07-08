lines_double_spaces = "welcom to  my  programe."

print(lines_double_spaces.find("  "))

print(lines_double_spaces.replace("  ", " ")) # strings are immutable, so this returns a new string with double spaces replaced by single spaces

lines_single_spaces = "welcom to my programe."
print(lines_single_spaces.find("  "))