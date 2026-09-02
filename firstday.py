name = "Grace"
age = 18
occupation = "Immaculata University Student"

interests = [
  "Dancing",
  "Reading",
  "Computers",
  "Concerts",
  "Learning"
]

#WELCOME MESSAGE
print("Welcome to the interest profile generator!")
print(".............................................")

print("\nName:", name)
print("Age:", age)
print("Occupation:", occupation)

#DISPLAY INTERESTS
print("\nInterests:")
for interest in interests:
  print("-", interest)
