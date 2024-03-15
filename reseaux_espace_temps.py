import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from simulation_event  import services
from matplotlib.lines import Line2D

ports_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
simulation_time = 30

activity_markers = {
    'loading': '^',  # Triangle up for loading
    'unloading': 'v',  # Triangle down for unloading
    'traveling to': '>',  # Triangle right for traveling
    'delivering': 's',  # Square for delivering
    'unloading at': 'x'  # X for unloading at
}
colors = plt.cm.get_cmap('tab10', len(services))
service_colors = {service.name: colors(i) for i, service in enumerate(services)}

fig, ax = plt.subplots(figsize=(9, 7))

def init():
    """Initialize the animation background."""
    for port, idx in ports_mapping.items():
        ax.hlines(y=idx, xmin=0, xmax=simulation_time, color='gray', linestyle='--')
    ax.set_xlabel('Time (days)')
    ax.set_ylabel('Port')
    ax.set_title('Space-Time Diagram for Port Services')
    ax.set_yticks(list(ports_mapping.values()))
    ax.set_yticklabels(list(ports_mapping.keys()))
    ax.grid(True)
    legend_elements = [Line2D([0], [0], marker=marker, color='w', label=activity,
                              markerfacecolor='black', markersize=10)
                       for activity, marker in activity_markers.items()]
    ax.legend(handles=legend_elements, title="Activity Types")
    return ax,

def update(frame):
    """Animate the state of services over time with distinct activities and lines."""
    ax.clear()
    init()
    for service in services:
        color = service_colors[service.name]
        path_data = [] 
        for entry in [e for e in service.activity_log if e[0] <= frame]:
            time, activity_type, *details = entry
            port = details[0] if details else None
            if port in ports_mapping:
                y_value = ports_mapping[port]
                path_data.append((time, y_value))  
                marker = activity_markers.get(activity_type, 'o') 
                ax.scatter(time, y_value, marker=marker, color=color, s=50)
        if path_data:
            times, y_values = zip(*path_data)
            ax.plot(times, y_values, color=color, linestyle='-', linewidth=1, alpha=0.5)

ani = FuncAnimation(fig, update, frames=np.linspace(0, simulation_time, num=int(simulation_time*10)), init_func=init, blit=False, repeat=False)

plt.show()


