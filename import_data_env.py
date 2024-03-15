import pandas as pd
import pandas as pd
import json
import requests

port_activities_url = 'https://raw.githubusercontent.com/MonDataa/simulation-barge/main/port_activities.json'
service_schedules_url = 'https://raw.githubusercontent.com/MonDataa/simulation-barge/main/service_schedules.json'

response = requests.get(port_activities_url)
port_activities_data = response.json()
port_activities_df = pd.DataFrame.from_dict(port_activities_data, orient='index')

response = requests.get(service_schedules_url)
service_schedules_data = response.json()
service_schedules_list = [(service, path[0], path[1]) for service, paths in service_schedules_data.items() for path in paths]
service_schedules_df = pd.DataFrame(service_schedules_list, columns=['Service', 'From', 'To'])
