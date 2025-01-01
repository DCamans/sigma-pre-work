from datetime import datetime

print("Welcome to the age calculator!")

def age_calculator(user_date):
    selected_date=datetime.strptime(user_date,"%d-%m-%Y")
    today = datetime.today()
    age = today.year-selected_date.year
    if (today.month,today.day)<(selected_date.month,selected_date.day):
        age-=1
    return age


user_date=input("Please enter a date (DD-MM-YYYY)")
age=age_calculator(user_date)
print(f"The calculated age is: {age}")

