import pandas as pd
import simpy
from import_data_env import *
from DemandManager  import *
from Service  import *


simulation_time = 30  # Simulation time in days

port_activities = port_activities_df.to_dict(orient='index')

# Préparer le dictionnaire pour les activités de port
for port, activities in list(port_activities.items()):
    if 'demands' in port_activities[port] and isinstance(port_activities[port]['demands'], tuple):
        port_activities[port]['demands'] = list(port_activities[port]['demands'])

    for activity, period in list(activities.items()):
        if isinstance(period, (list, tuple)):
            if pd.Series(period).isnull().any():
                del port_activities[port][activity]
            else:
                port_activities[port][activity] = tuple(period) if isinstance(period, list) else period


service_schedules = {}
for index, row in service_schedules_df.iterrows():
    service = row['Service']
    if service not in service_schedules:
        service_schedules[service] = []
    service_schedules[service].append((row['From'], row['To']))

activity_log = {service: [] for service in service_schedules}
env = simpy.Environment()
demand_manager = DemandManager(port_activities)
services = [Service(env, name, schedule, port_activities, demand_manager) for name, schedule in service_schedules.items()] 
ports_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3}


for service in services:
    for entry in service.activity_log:
        port = entry[1][1] if isinstance(entry[1], tuple) else entry[2] if len(entry) > 2 else None
        if port and port not in ports_mapping:
            # Ajouter le nouveau port à ports_mapping avec une valeur y unique
            ports_mapping[port] = max(ports_mapping.values()) + 1
            
env.run(until=simulation_time)

