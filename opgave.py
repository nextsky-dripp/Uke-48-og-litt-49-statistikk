import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
 
x = 1
x1 = [-6, -5, -4, -7, -8, -7, -2, -1, -1]           #her er de forskjelige talene fra yr og storm
x2 = [-8, -12, -16, -15, -16, -13, -2, -10, -12]
y = [0,1, 2, 3, 4, 5, 6, 7, 8]  
 
dager = [27, 28, 29, 30, 1, 2, 3, 4, 5] # her er dagene
 
plt.xlabel("dag") # er står det på grafen hva x aksen gjør her er x = dag
plt.ylabel("temperatur") # og her er y aksen for tempraturen
 
plt.xticks(y, dager)
 
 
while x:
    valg = int(input("velg hva du vil ha:\n 1) begge grafer\n 2) Yr\n 3) Storm\n")) #Det er hva som komer i terminale og det står vordan du får den grafen du vil med og skrive 1, 2, eller 3.
    match valg:
        case 1: # Er nesten som vist ikke så. henrik viste meg dete
            print(f" resultatet for yr.no er:\n gjennomsnittet er: {np.mean(x1)}\n medianen er: {np.median(x1)}\n typetallet er {stats.mode(x1)}\n") # dise to er det sama som de neden for men den gjør det med bege to så du kan letere se forskjelden
            print(f" resultatet for Storm er:\n gjennomsnittet er: {np.mean(x2)}\n medianen er: {np.median(x2)}\n typetallet er {stats.mode(x2)}")
 
            plt.plot(x1, linestyle='--', marker='o', color='b', label='Yr.no') #styrer fargen for yr og den styrer hvordan grafen ser ut som farge og vordan strekern er. Den under gjør det same for storm
            plt.plot(x2, linestyle='--', marker='o', color='r',label='Storm')
 
            plt.legend()
 
            plt.show()
            x = 0
        case 2:
            print(f" resultatet for yr.no er:\n gjennomsnittet er: {np.mean(x1)}\n medianen er: {np.median(x1)}\n typetallet er {stats.mode(x1)}\n") #Det printer gjenomsnite og medianen og det i terminalen
 
            plt.plot(x1, linestyle='--', marker='o', color='b', label='Yr.no')
 
            plt.legend()
            plt.show()
            x = 0
 
            # Dene koden viser resultatet for storm
        case 3:
            print(f" resultatet for Storm er:\n gjennomsnittet er: {np.mean(x2)}\n medianen er: {np.median(x2)}\n typetallet er {stats.mode(x2)}") #Det printer gjenomsnite og medianen og det i terminalen
           
            plt.plot(x2, linestyle='--', marker='o', color='r',label='Storm')
 
            plt.legend()
            plt.show()
            x = 0
 
                #Vist det du skriver ikke er riktig komer dene komentaren opp
        case _:
            print("you did not input a valid number")
 
 
 
 
 
            #henrik har hjolpet meh med lit av koden og vist meg ting som case. jeg mener han fortener en 6
