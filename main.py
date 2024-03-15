from import_data_env import *
from matrice_routage import *
from reseaux_espace_temps import *
from statistique_containers_porta import * 
from statistique_containers_portb import * 
from simulation_event import activity_log


simulation_time = 30

print("Résultat de import_data_env.py :")
print("Port Activities DataFrame:\n", port_activities_df)
print("\nService Schedules DataFrame:\n", service_schedules_df)
print("-" * 50) 

# Exécuter matrice_routage.py
print("Résultat de matrice_routage.py :")
print("Routing Matrix:\n", routing_matrix)
print("-" * 50)

# Exécuter simulation.py
print("Résultat de simulation.py :")
print("Activity Logs:")

for service, log in activity_log.items():
    print(f"\nService: {service}")
    for entry in log:
        print(f"  Time: {entry[0]}, Activity: {entry[1]}, Details: {entry[2:]}")
print("-" * 50)

# Exécuter reseaux_espace_temps.py
print("Résultat de reseaux_espace_temps.py :")
print("Résultat de statistique_containers_porta.py ")
print("Generating space-time network animation...")
