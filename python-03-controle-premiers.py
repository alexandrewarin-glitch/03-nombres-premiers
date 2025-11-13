import math


try:
    chaine_p = input("Entrez un nombre entier à tester : ")
    p = int(chaine_p)
    if p < 2:
        print(f"{p} : False")
    
    elif p == 2:
        print(f"{p} : True")
    
    elif p % 2 == 0:
        print(f"{p} = 2 x {p // 2} : False")
    
    else:    
        limite = int(math.sqrt(p)) + 1
        for d in range(3, limite, 2):
            if p % d == 0:
                print(f"{p} = {d} x {p // d} : False")
                break 
        else:
            print(f"{p} : True")
except ValueError:
    print(f"Erreur : '{chaine_p}' n'est pas un nombre entier valide.")