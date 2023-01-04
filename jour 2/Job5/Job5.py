def calcul(num1,operator,num2):
 result = str(num1) + operator + str(num2)
 return eval(result)

print (calcul(12, "/", 3))