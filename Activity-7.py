def celToFar(temp):
    fahrenheit = (temp * 1.8) + 32
    return fahrenheit
 
def FarToCel(temp):
    celcius = (5/9)*(temp-32)
    return celcius


user = int(input("Enter 1 for C to F"))
userChoice = int(input("Enter the temperature: "))
if user==1:
    print("The Far eq of Cel = ",celToFar(userChoice))
else:
    print("The Cel eq of Far = ", FarToCel((userChoice)))