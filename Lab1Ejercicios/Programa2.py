print("*** CALCULAR SEGUNDOS DE UNA HORA DADA ***")
horas = input("Ingrese las hora del dia HH: ")
minutos = input("Ingrese los minutos de la hora MM: ")
segundos = input("Ingrese los segundos del minuto SS: ")

horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

segundosCalculados = horas * 3600 + minutos * 60 + segundos

segundosCalculados = int(segundosCalculados)

if horas < 0 or horas > 24: 
    print("**Hora fuera de rango vuelva a intentarlo")
elif minutos < 0 or minutos > 59:
    print("**Minuto fuera de rango vuelva a intentarlo")
elif segundos < 0  or segundos > 59:
    print("**Segundo fuera de rango vuelva a intentarlo")
else: 
    print("Los segundos totales de la hora del dia",horas,":",minutos,":",segundos," es:",segundosCalculados)
