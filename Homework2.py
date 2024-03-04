Celsius = int(input('Enter Grad Celsius:'))
Grad = 'Fahrenheit'
Grad1 = 'Kelvin'
print(Grad, Celsius  * 9/5 + 32)
print(Grad1, Celsius + 273.15)

#Task 2

V1 = int(input('Enter Liters:'))
T1 = int(input('Enter Temperature:'))
V2 = int(input('Enter Liters1:'))
T2 = int(input('Enter Temperature1:'))
Temperature1 = (V1 + V2)
Volume1 = (V1 * T1 + V2 * T2) / (V1 + V2)
Result = 'Volume'
Result1 = 'Temperature'
print(Result, Temperature1)
print(Result1, Volume1)

#Task 3

a = int(input('Value'))
b = input('Action')
c = int(input('Value2'))
if b == '+':
    print(a + c)
elif b == '-':
    print(a - c)
elif b == '*':
    print(a * c)
elif b == '/':
  if c != 0:
    print(a / c)
  else:
      print('Error')

