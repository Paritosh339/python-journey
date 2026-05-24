def convert_temp(temp, unit):
    if unit == "C":
     convert1 = (temp * 9/5) + 32
     return f"{temp}°C = {convert1}°F"

    elif unit == "F":
     convert2 = (temp - 32) * 5/9
     return f"{temp}°F = {convert2}°C"
    else:
        return("invalid input")

temp = float(input("Please enter your temperature: "))
unit = input("Please enter your temperature unit: ").upper()

print(convert_temp(temp, unit))
