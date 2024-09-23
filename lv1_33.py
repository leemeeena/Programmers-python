code = input()
last_four_words = code[-4:]

if last_four_words == "_eye":
    print("Ophthalmologyc")
elif "head" in code:
    print("Neurosurgery")
elif "infl" in code:
    print("Orthopedics")
elif "skin" in code:
    print("Dermatology")
else:
    print("direct recommendation")