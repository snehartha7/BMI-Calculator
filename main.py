import time



while True:
    unit = input("Which system do you want to use ? (Metric/Imperial) : ").lower()
    
    if unit == "metric":
        weight_1 = float(input("Enter your weight in Kgs. : "))
        height_1 = float(input("Enter your weight in metres : "))
        bmi = weight_1 / (height_1 ** 2)
        print(bmi)
    elif unit == "imperial" : 
        weight_2 = float(input("Enter your weight in lbs. = "))
        height_2 = float(input("Enter your height in inches : "))
        bmi = weight_2 / (height_2 ** 2)
        print(bmi)
    else :
        print("Invalid input.")
    
    
    if bmi < 18.5 :
        print("underweight.")
    elif 18.5 <= bmi < 25 :
        print("Healthy weight.")
    elif 25 <= bmi < 30 :
        print("Overweight.") 
    else :
        print("Obesity.")  
    
    time.sleep(1)
    
    a = input("Do you want to continue : (Y/N) ").lower()
    
    if a == "y":
        continue
    elif a == "n":
        break
    else:
        print("invalid input.")