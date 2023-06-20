##Exception Handling(ZeroDivisionError)-->
try:
    age=int(input("Age>"))
    income=int(input("Income>"))
    risk=income/age
    print(f"Risk>{risk}")
except ValueError:
    print("Invalid value!!")
except ZeroDivisionError:
    print("Zero cannot be denominator!!")
