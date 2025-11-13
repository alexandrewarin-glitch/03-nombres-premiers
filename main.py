"""
Script pour la vérification de nombres premiers.

Ce module définit une fonction 'isprime' optimisée pour tester
si un nombre est premier, et une fonction 'main' pour
afficher les nombres premiers de 0 à 99.
"""

#### Fonction secondaire

def isprime(p: int) -> bool:
    """
    Vérifie si un nombre entier p est premier.

    Utilise une approche optimisée (6k +/- 1) sans import
    et avec une seule variable d'itération.

    Args:
        p (int): Le nombre entier à tester.

    Returns:
        bool: True si p est premier, False sinon.
    """

    # --- Cas de base ---
    # Gère 0, 1 (False) et 2, 3 (True) en une seule ligne.
    if p <= 3:
        return p > 1

    # --- Filtres rapides ---
    # Gère les multiples de 2 et 3 (non premiers).
    if p % 2 == 0 or p % 3 == 0:
        return False

    # --- Optimisation 6k +/- 1 ---
    # On teste les diviseurs 5, 7, 11, 13, 17, 19...
    # On s'arrête quand d*d dépasse p (plus rapide que sqrt(p)).
    d = 5
    while d * d <= p:
        if p % d == 0 or p % (d + 2) == 0:
            return False
        d += 6  # On saute au prochain couple 6k +/- 1

    # Si la boucle se termine sans trouver de diviseur, p est premier.
    return True

#### Fonction principale

def main() -> None:
    """
    Fonction principale du script.

    Itère sur les nombres de 0 à 99 et affiche
    ceux qui sont premiers sur une seule ligne.
    """

    # Itère sur tous les nombres dans l'intervalle [0, 100)
    for n in range(100):
        # Appelle la fonction de vérification de primalité
        if isprime(n):
            # Affiche le nombre premier, suivi d'une virgule et d'un espace.
            print(n, end=", ")

    # Imprime un retour à la ligne final pour la propreté.
    print()


if __name__ == "__main__":
    main()
