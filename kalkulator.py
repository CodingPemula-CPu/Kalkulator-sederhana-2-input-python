#KinsProject

#input1
number1 = eval(input("Masukkan bilangan pertama : "))
print(float(number1))

#operator
operator = input("Masukkan Operator (+,-,*,/): ")
print(operator)

#input2
number2 = eval(input("Masukkan bilangan kedua : "))
print(float(number2))

if operator == '*':
    print("Hasil Perkaliannya : ",number1 * number2)

elif operator == '+':
    print("Hasil Penjumlahannya : ", number1 + number2)

elif operator == '-':
    print("Hasil Pengurangannya : ", number1 - number2)

elif operator == '/':
    print("Hasil Pembagiannya : ", number1 / number2)