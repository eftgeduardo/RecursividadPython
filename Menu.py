
#1
def factorial(n):
  if(n==1):
    return n 
  else: 
    return n * factorial(n-1)
#2
def Sumatoria(n):
  if(n==1):
    return n
  else: 
    return n + Sumatoria(n-1)
#3
def potencia(x,n):
  if(n==1):
    return x
  else:
    return x * potencia(x,(n-1))
#4
def multiplicacion(m,n):
  if(n==1):
    return m
  else:
    return m + multiplicacion(m,n-1)
#5
def division(m,n):
  if(m==n):
    return 1
  else:
    return 1 + division(m-n,n)
#6
def potencia2(x,n):
  if(n==1):
    return x
  else: 
    return  multiplicacion(x, potencia(x,(n-1)))
#7
def palindromo(s):    
  if(len(s)==0):
    print("Error: no se encontro ningun texto")
  else:    
    if(s[len(s)-1]==s[0]):
      if(len(s)<3):
        return print("Es palindromo")
      else:
        return palindromo(s[1:(len(s)-1)])
    else: 
      print("no es palindromo")

#8
def inversionString(s):
  if(len(s)==1):
    return s
  else:
    return s[len(s)-1]+inversionString(s[:len(s)-1])
#9 
def torresHanoi(x,i,f):
  if(x==1):
    return ""+str(i)+"-"+str(f)+"\n"
  else:
    return torresHanoi(x-1,i,(6-i-f))+ torresHanoi(1,i,f)+ torresHanoi(x-1,(6-i-f),f)
#10 no estoy seguro
def funcionFor(inicial,final,paso):
  if(inicial==final):
    return inicial
  else:
    return funcionFor(inicial+paso,final,paso)
#11 
def fibonacci(n):
  if (n==0):return 0
  elif (n==1):return 1
  else:
    return int(fibonacci(n-1))+int(fibonacci(n-2))

def forFibonacci(i,n):
  if(i==n):
    print(fibonacci(i))
    return 
  else:
    print(fibonacci(i),end=",")
    return forFibonacci(i+1,n)

def main():
  print("MENU")
  print("1. Factorial")
  print("2. Sumatoria")
  print("3. Potencia")
  print("4. Multiplicacion")
  print("5. division")
  print("6. Potencia2")
  print("7. Palindromo")
  print("8. Inversion de String")
  print("9. Torres Hanoi")
  print("10. fibonacci")
  choice=int(input("escriba un numero:"))
  print("___________________")
  Menu[choice]()

def MenuFactorial():
  print("Factorial X")
  x = int(input())
  print ("Resultado= {}".format(factorial(x)))
def MenuSumatoria():
  print("Sumatoria X")
  x = int(input("x"))
  print ("Resultado= {}".format(Sumatoria(x)))
def MenuPotencia():
  print("Potencia x^y")
  x = int(input("x= "))
  y = int(input("^y= "))
  print ("Resultado {}".format(potencia(x,y)))
def MenuMultiplicacion():
  print("Potencia x*y")
  x = int(input("x= "))
  y = int(input("y= "))
  print ("Resultado {}".format(multiplicacion(x,y)))
def MenuDivision():
  print("Division x/y")
  x = int(input("x= "))
  y = int(input("y= "))
  print ("Resultado {}".format(division(x,y)))
def MenuPotencia2():
  print("Division x^y")
  x = int(input("x= "))
  y = int(input("^y = "))
  print ("Resultado {}".format(potencia2(x,y)))
def MenuPalindromo():
  print("Palindromo")
  s=input("Palabra= ")
  print ("Resultado {}".format(palindromo(s)))
def MenuInversionString():
  print("Palindromo")
  s=input("Palabra= ")
  print ("Resultado {}".format(inversionString(s)))
def MenuTorreHanoi():
  print("Torres Hanoi")
  x=int(input("cantidad de discos:"))
  i=int(input("posicion inicial: "))
  f=int(input("posicion Final: "))
  print("Resultado: ")
  print(torresHanoi(x,i,f))
def MenuFibonacci():
  print("Fibonacci")
  x=int(input("numero:"))
  forFibonacci(0,x)
  #print ("Resultado: {}".format(fibonacci(x)))

#lambda
Menu={
  1:MenuFactorial,
  2:MenuSumatoria,
  3:MenuPotencia,
  4:MenuMultiplicacion,
  5:MenuDivision,
  6:MenuPotencia2,
  7:MenuPotencia2,
  8:MenuInversionString,
  9:MenuTorreHanoi,
  10:MenuFibonacci
}


if __name__=='__main__':
  main()
  







