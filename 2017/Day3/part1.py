import math
target = 368078

couche = math.ceil((math.sqrt(target) - 1) / 2)
valeur_max = (2 * couche + 1) **2

points_centraux = [valeur_max - couche * i for i in [1,3,5,7]]

distance_points_centraux = [abs(target - point) for point in points_centraux]
print(distance_points_centraux)

print(min(distance_points_centraux) + couche)

