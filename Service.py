simulation_time = 30 

class Service:
    def __init__(self, env, name, schedule, port_activities, demand_manager):
        self.env = env
        self.name = name
        self.schedule = schedule
        self.port_activities = port_activities
        self.demand_manager = demand_manager  # Accès au Gestionnaire de Demandes
        self.activity_log = []
        self.env.process(self.run())

    def run(self):
        while True:
            for start_port, end_port in self.schedule:
                # Gestion du chargement
                loading_period = self.port_activities[start_port].get('loading', [0])
                time_until_loading = max(loading_period[0] - self.env.now, 0)
                yield self.env.timeout(time_until_loading)
                self.activity_log.append((self.env.now, 'loading', start_port))
                yield self.env.timeout(1)  # Simule le chargement pour un jour
                
                # Gestion des demandes (livraison) via le DemandManager
                demands = self.demand_manager.get_demands_for_port(start_port)
                demands_list = list(demands)
                for demand in demands_list[:]:  # Itération sur une copie pour permettre la suppression
                    if self.env.now >= demand['date_depart']:
                        self.activity_log.append((self.env.now, 'delivering', demand['ContainerID'], start_port))
                        yield self.env.timeout(1)  # Simule la livraison de la demande
                        demands_list.remove(demand)  # Supprime la demande après livraison
                
                # Voyage vers le port suivant si nécessaire
                if start_port != end_port:
                    self.activity_log.append((self.env.now, 'traveling to', end_port))
                    yield self.env.timeout(1)  # Suppose un jour de voyage
                
                # Gestion du déchargement
                unloading_period = self.port_activities[end_port].get('unloading', [0])
                time_until_unloading = max(unloading_period[0] - self.env.now, 0)
                yield self.env.timeout(time_until_unloading)
                self.activity_log.append((self.env.now, 'unloading at', end_port))
                yield self.env.timeout(1)  # Simule le déchargement pour un jour
                
                # Vérifie si le temps de simulation a été atteint avant de commencer un nouveau cycle
                if self.env.now >= simulation_time:
                    break
                else:
                    # Ajuste pour le prochain cycle
                    cycle_length = 13  # Longueur du cycle ajustée selon les besoins
                    time_until_next_cycle = (cycle_length - self.env.now % cycle_length) % cycle_length
                    if time_until_next_cycle == 0:
                        time_until_next_cycle = cycle_length
                    yield self.env.timeout(time_until_next_cycle)

