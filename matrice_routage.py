import pandas as pd
from import_data_env import service_schedules_df

ports = ['A', 'B', 'C', 'D']

routing_matrix = pd.DataFrame('?', index=ports, columns=ports)

for port in ports:
    routing_matrix.at[port, port] = 'X'

for _, row in service_schedules_df.iterrows():
    from_port = row['From']
    to_port = row['To']
    service = row['Service']
    if from_port in ports and to_port in ports:
        routing_matrix.at[from_port, to_port] = service

print(routing_matrix)