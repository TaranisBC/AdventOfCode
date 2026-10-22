import time

start_time = time.perf_counter()

poissons = [3,4,3,1,2]

jour = 0
while jour < 256:
    print(f"Jour {jour}")
    nouveaux_poissons = []
    for poisson in poissons:
        if poisson == 0:
            nouveaux_poissons.append(6)
            nouveaux_poissons.append(8)
        else:
            nouveaux_poissons.append(poisson - 1)
    poissons = nouveaux_poissons
    jour += 1

end_time = time.perf_counter()
time_taken = end_time - start_time
print(len(poissons))
print(f"Le script s'est exécuté en {time_taken:.4f} secondes")