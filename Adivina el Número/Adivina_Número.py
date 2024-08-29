import random


def adivina_el_numero(x):
        print()
        print("=============================")
        print(" ¡Bienvenido(a) al Juego !")
        print("=============================")
        print("Tu meta es adivinar el numero generado por la computadora.")

        numero_aletorio=random.randint(1,x) #numero aletorio 1 y x

        prediccion=0 
        
        while prediccion!= numero_aletorio:
            print()
            prediccion=int(input(f"Adivina un numero entero entre 1 y {x} \n "))
            
            if prediccion < numero_aletorio:
                print()
                print("Intenta otra vez. este numero es muy pequeño.")
                print()
            elif prediccion > numero_aletorio:
                print()
                print("Intenta otra vez. este numero es muy grande.")
                print()

        print(f"¡Felicitaciones! Adivinastes el numero {numero_aletorio} correctamente")  
                 

adivina_el_numero (10)