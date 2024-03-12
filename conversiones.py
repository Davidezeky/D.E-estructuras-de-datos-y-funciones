import sys

peso_chileno = int(sys.argv[1])

SOL = 0.0046
ARS = 0.093
USD = 0.0013

soles = peso_chileno * SOL
pesos_argentinos = peso_chileno * ARS
dolares = peso_chileno * USD

print(f"los {peso_chileno} CLP equivalen a:")
print(f"{soles} Soles")
print(f"{pesos_argentinos} Pesos Argentinos")
print(f"{dolares} Dólares")