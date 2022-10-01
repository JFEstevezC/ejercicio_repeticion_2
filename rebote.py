print("-------------------------------------------------------------------")
print("-----------------------REBOTE DE LA PELOTA-------------------------")
print("-------------------------------------------------------------------")

h = int (input("Escriba la altura h de la que se deja caer la perlota: "))
p = h/5
i = 0

while h >= p:

    h = h - h * (10/100)
    i = i + 1

print ("El número de rebotes que tuvo la pelota es: " + str (i))