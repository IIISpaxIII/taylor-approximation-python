from math import factorial

import numpy as np
first_list=[2,8,5]

first_array=np.array(first_list)


print(type(first_list))

print(type(first_array))

print("SVar 1: ")

# skapar en tom np.array som jag kommer sedan lägga varje term i en talserie.
tal_serie_array = np.array([])

# itererar från 1 till 15 sedan lägger varje nummer i arrayen.
for i in range (1,16):
    number_in_each_index = 1/i
    #lägger varje tal i slutet av array.
    tal_serie_array = np.append(tal_serie_array, number_in_each_index)


summor = np.cumsum(tal_serie_array)

for i in range (15):
   print("n = ", i+1 , ": ", summor[i])


print("Svar 2a: ")
import math
#skapar en tom array för att spara värden. 
exp_koefficenterna_array = np.array([])

#itirerar genom varje index och sedan lägger varje tilldelade element i np.arrayen.
for i in range(15):
    element_in_each_index = 1/math.factorial(i);
    exp_koefficenterna_array = np.append(exp_koefficenterna_array, element_in_each_index)

print(exp_koefficenterna_array)


print("Svar 2b: ")
#skapar en lista med 15 nollor.
fib_list = [0] *15

#min lista med 15 0'or sparas i en variabeln fib_arr med datatypen np.array.
fib_arr = np.array(fib_list)

# andra elementen av arrayen ska vara 1 så att vi kan bygga vidare härifrån.
# vi redan vet att första elementet är 0 då ska vi fortsätta genom algoritmen.
fib_arr[1] = 1

# vi vet redan första och andra elementet dvs index 0 och index 1 så börjar
#vi från element 2 till 14 som blir totallt 15 element.
for i in range(2,15):
    #varje element är summan av två föregående element.
    fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]


print(fib_arr)

print("Svar 2c: ")

# I denna fråga vet jag at resten är 0 när det är en jämn term, dvs 2:a, 4:e... 10:e
# termen ger resultatet 0, medan de udda ger ett specifikt resultat utifrån ett uttryck.

sinus_koefficenter_array = np.array([])

for i in range(15):
    if i %2 == 0:
        sinus_koefficenter_array = np.append(sinus_koefficenter_array, 0)

    else: #om det inte är en jämn index, använd uttrycket.
        sinus_koefficenter_array = np.append(sinus_koefficenter_array, (-1)**((i+1)/2)/math.factorial(i))
                                                                            # borde det inte vara i -1??

print(sinus_koefficenter_array)



print ("Svar 3a: ")

# Returnerar polynomens värde (int) enligt input från user för x.värde och koefficenter.
# (Jag hämtade den från Roberts anteckningar)
def eval_poly(x, coeffs):
    x_arr = np.array([x**i for i in range(len(coeffs))])
    p = x_arr * coeffs
    return np.sum(p)


riktigt_svar = np.exp(2) #räknar e**2

koef_for_approximation = np.array([]) #skapar en tom lista som ska hålla konstanterna för approx.

for i in range(10**100):
    element = 1/math.factorial(i)
    koef_for_approximation = np.append(koef_for_approximation, element)

    #här hittar vi svaret för den polynomen som vi testar.
    approx = eval_poly(2, koef_for_approximation)

    #här räknas hur  stor felmarginalen är för att sedan jämföra med vår mål.
    fel_marginalen = riktigt_svar - approx

    if fel_marginalen < 10**-4 and fel_marginalen > -10**-4:
        print(f'För polynom av grad {i} är polynomets värde så nära e**2 att felmarginalen är mindre än 10**-4.')
        break


print("Svar 3b: ")

riktigt_svar_sin = np.sin(5*np.pi/3) #riktiga svaret för sin.
koef_sin = np.array([])

for i in range(10**100):
    if i%2 == 0:
        koef_sin = np.append(koef_sin, 0) #sinus funktionen returnerar 0 när indexet är jämn
    else:                              # formeln för koeff för sin värden i uppgiften är fel. i-1 ger rätt svar.
        koef_sin = np.append(koef_sin, (-1)**((i-1)/2)/math.factorial(i))

    #här hittar vi svaret för den polynomen som vi testar, där x = 5pi/3
    approx_sin = eval_poly(5*np.pi/3, koef_sin)
    #här räknas hur  stor felmarginalen är för att sedan jämföra med vår mål.
    fel_marginalen_sin= abs(riktigt_svar_sin-approx_sin)

    if fel_marginalen_sin < 10**-4:
        print(f'För polynom av grad {i} är polynomets värde så nära sin(5pi/3) att felmarginalen är mindre än 10**-4.')
        break



#ritning av graf
import matplotlib.pyplot as plt

#ritning av graf för approx sin
x = np.linspace(-3,3,100) #lägger punkter mellan -3 3.
y = np.sin(x)
y_approx = np.array([eval_poly(each_x, koef_sin) for each_x in x])

plt.figure()
plt.plot(x, y, 'o-')
plt.plot(x, y_approx)

plt.xlabel("x")
plt.ylabel("y")
plt.title("approx_sin och original_sin")

plt.grid(True)




# ritning av graf för approx e**2

x = np.linspace(0,3,100) #lägger punkter mellan -3 3.
y = np.exp(x)
y_approx = np.array([eval_poly(each_x, koef_for_approximation) for each_x in x])

#skapa en graf
plt.figure()
plt.plot(x, y, "o-")
plt.plot(x, y_approx)

plt.xlabel("x")
plt.ylabel("y")
plt.title("approx_e och original_e")

plt.grid(True)

#aktivera GUI så att den visualiseras
plt.show()



print ("Svar 4")

def polynom_multiplikation(p1_koeffs, p2_koeffs):

    #längden av polynomer
    p1 = len(p1_koeffs)
    p2 = len(p2_koeffs)
    # förlänger kortare array med nollor
    if p1<p2:
        p1_koeffs=np.append(p1_koeffs,np.zeros(p2-p1))
    else:
        p2_koeffs=np.append(p2_koeffs,np.zeros(p1-p2))

    #längderna blir samma efter if-else kontrollen så nu kan jag använda den när jag sparar
    # resultatet i en ny np.array.
    n = len(p1_koeffs)

    # skapar en array med längden 2n eftersom multiplikation av två polynomer ger en längre polynom.
    resultat_array = np.zeros(2*n)

    for i in range(p1):
        for j in range(p2):
            # Man adderar exponenterna vid multiplikation. Därför sparar jag produkten på index (i + j)
            # Jag använder += för att lägga till på det som redan finns där
            resultat_array[i+j] += p1_koeffs[i] * p2_koeffs[j]


    return resultat_array


p = np.array([1,2])
q = np.array([-3,0,9])
z = np.array([3,0,0])

print(polynom_multiplikation(p,q))
print(polynom_multiplikation(p,z))

p = np.polynomial.Polynomial([1,2])
q = np.polynomial.Polynomial([-3,0,9])
z = np.polynomial.Polynomial([-3,0,0])

print(p*q)
print(p*z)
