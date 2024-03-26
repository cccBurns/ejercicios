#Pedir al usuario que intruduzca un numero y mostrar si es par o impar.

numero = int(input("Introduce un numero: "))

if numero % 2 == 0:
    print("El numero", numero, "es par")
else:
    print("El numero", numero, "es impar")
    
input("Presiona Enter para salir...")