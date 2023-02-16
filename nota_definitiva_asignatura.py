# Programa para hallar la nota definitiva de nc, cp, na, au, bi

print("-----------------------------------------")
print("----------- VALOR NOTA DEFINIDA ---------")
print("-----------------------------------------")

#Input
nc = int(input("digite el valor de cognitiva: "))
np = int(input("digite el valor de procedimental: "))
na = int(input("digite el valor de actitudinal: "))
au = int(input("digite el valor de autoevaluacion: "))
bi = int(input("digite el valor de bimestral: "))

#Processing
nd = (0.3*nc) + (0.3*np) + (0.1*na) + (0.1*au) + (0.2*bi)


#output
print("-------------------------------------")
print("------------ RESULTADOS -------------") 
print("-------------------------------------")
print("NOTA DEFINIDA " + str(nd))