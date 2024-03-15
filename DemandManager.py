class DemandManager:
    def __init__(self, port_activities):
        self.port_activities = port_activities

    def get_demands_for_port(self, port):
        demands = self.port_activities.get(port, {}).get('demands', [])
        return demands[:]