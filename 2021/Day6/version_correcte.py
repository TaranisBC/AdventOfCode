import time

start_time = time.perf_counter()
poissons = [3,4,3,1,2]

poissons_tries = [0] * 9

for poisson in poissons:
    poissons_tries[poisson] += 1

print(poissons_tries)
jour = 0
while jour < 80:
    print(f"Jour {jour}")
    nouveaux_poissons = [0] * 9
    for i in range (9):
        if i == 0:
            nouveaux_poissons[8] += poissons_tries[0]
            nouveaux_poissons[6] += poissons_tries[0]
        else:
            nouveaux_poissons[i-1] += poissons_tries[i]
    poissons_tries = nouveaux_poissons.copy()
    jour += 1


end_time = time.perf_counter()
time_taken = end_time - start_time
print(sum(poissons_tries))
print(f"Le script s'est exécuté en {time_taken:.4f} secondes")