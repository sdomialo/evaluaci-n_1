#Ejercicio 2: Cálculo de Interés Compuesto

#Crea un programa que calcule el interés compuesto.

#Guarda en una variable capital_inicial el valor 1000.

#Lee por pantalla la tasa de interés anual, que deberá estar entre 1% y 10%.

#Eleva la tasa de interés a sí misma por el número de años (por ejemplo, 5 años).

#Multiplica el capital_inicial por el resultado anterior en sí mismo.

#Muestra el capital final.


capital_inicial = 1000


tasa_interes_anual = float(input("Ingrese la tasa de interés anual (entre 1% y 10%): "))

numero_de_años = int(input("Ingrese el número de años: "))


if tasa_interes_anual < 1 or tasa_interes_anual > 10:
    print("La tasa de interés debe estar entre 1% y 10%.")
else:
    tasa_interes_decimal = tasa_interes_anual / 100
    capital_final = capital_inicial * (1 + tasa_interes_decimal) ** numero_de_años

    print("El capital final es:", capital_final)
