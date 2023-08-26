desired = input("What is the desired age you wish to calculate the time until? ")
age = input("What is your current age? ")

dINT = int(desired)
ageINT = int(age)
days = 365*(dINT-ageINT)
weeks = 52*(dINT-ageINT)
months = 12*(dINT-ageINT)
print(f"you have {days} days, {weeks} weeks, or {months} months left until {desired} years old.")

