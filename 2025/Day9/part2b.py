### Solution volée de stOneskull sur GitHub, vraiment intéressante.
from itertools import combinations
from multiprocessing import Pool
from shapely.geometry import Polygon, box

# Refactorisation de la fonction pour prendre le polygone en paramètre
def check_rectangle(p1, p2, floor):
    x1, y1 = p1
    x2, y2 = p2

    # Shapely.box, un polygone rectangulaire
    rectangle = box(
        min(x1, x2), min(y1, y2),
        max(x1, x2), max(y1, y2)

    )

    # La méthode contains de polygon vérifie si une forme est entièrement contenue dans une autre
    if floor.contains(rectangle):
        return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    return 0

with open("input.txt", "r") as file:
    # List comprehension pour extraire toutes les coordonées sous forme de tuple
    red_tiles = [
        tuple(map(int, line.strip().split(",")))
        for line in file
    ]

# Création du polygone formé par les tuiles rouges
theater_floor = Polygon(red_tiles)


with Pool() as pool:
    # Combinations crée toutes les associations possibles de tuiles en diagonale (coins opposés des rectangles)
    # Tasks prépare les paramètres à passer à la fonction check_rectangle dans starmap
    tasks = ((t1, t2, theater_floor) for t1, t2 in combinations(red_tiles, 2))
    # starmap reçoit une fonction et un tuple contenant les paramètres de la fonction. À la fin tous les résultats
    # sont regroupés dans une liste. pool.starmap() exécute en multi thread
    areas = pool.starmap(
        check_rectangle, tasks
    )

print(max(areas))