a = 7
b = 11
c = 100
d = 700

print(f"Valores iniciais: A = {a}, B = {b}, C = {c} e D = {d}")

aux = a
a = b
b = c
c = d
d = aux
print(f"Valores trocados: A = {a}, B = {b}, C = {c} e D = {d}")