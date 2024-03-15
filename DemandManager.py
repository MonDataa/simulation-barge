class DemandManager:
    def __init__(self, port_activities):
        self.port_activities = port_activities

    def get_demands_for_port(self, port):
        # Cloner la liste des demandes pour le port spécifié pour éviter la modification des données originales
        demands = self.port_activities.get(port, {}).get('demands', [])
        return demands[:]  # Retourne une copie de la liste