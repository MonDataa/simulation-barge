import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation_event  import services
from simulation_event import port_activities

port_b_container_quantities = {}
for service in services:
    for log_entry in service.activity_log:
        if log_entry[1] == 'delivering' and log_entry[3] == 'B':
            container_id = log_entry[2]
            quantity = next((demand['Quantity'] for demand in port_activities['B']['demands'] if demand['ContainerID'] == container_id), 0)
            
            day = log_entry[0]
            if day in port_b_container_quantities:
                port_b_container_quantities[day] += quantity
            else:
                port_b_container_quantities[day] = quantity

port_b_container_quantities

port_b_container_quantities

days = list(port_b_container_quantities.keys())
container_counts = [port_b_container_quantities[day] for day in days]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Quantity of Containers Delivered to Port B Over Time')
ax.set_xlabel('Day')
ax.set_ylabel('Sum(Quantity) of Containers')
ax.grid(True)

ax.set_xlim(min(days), max(days))
ax.set_ylim(min(container_counts), max(container_counts) + 5)

line, = ax.plot([], [], marker='o', linestyle='-', color='b')

def animate(i):
    day = days[:i+1]
    count = container_counts[:i+1]
    line.set_data(day, count)
    return line,

ani = FuncAnimation(fig, animate, frames=len(days), interval=500, blit=True)

plt.show()
