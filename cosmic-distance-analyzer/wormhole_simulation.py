import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_3d_distance(p1, p2):
    """Calculates the standard 3D Euclidean distance in Light Years."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

def calculate_wormhole_time(throat_length_km, speed_percentage):
    """Calculates time taken to exit a wormhole in minutes."""
    speed_of_light_kms = 299792
    ship_speed = (speed_percentage / 100.0) * speed_of_light_kms
    time_seconds = throat_length_km / ship_speed
    return time_seconds / 60

# --- Parameters ---
EARTH = (0, 0, 0)
TARGET_SECTOR = (150, 300, 500)
WORMHOLE_SHORTCUT_KM = 200000000
SHIP_SPEED_PCT = 75

# --- Calculations ---
normal_distance = calculate_3d_distance(EARTH, TARGET_SECTOR)
travel_time_mins = calculate_wormhole_time(WORMHOLE_SHORTCUT_KM, SHIP_SPEED_PCT)

# 1 Light Year crossing time at 75% c in minutes
normal_travel_time_mins = (normal_distance / (SHIP_SPEED_PCT / 100.0)) * 525960

# --- Console Output ---
print("COSMIC WORMHOLE ANALYTICS LOG")

print(f"Standard 3D Space Distance: {normal_distance:.2f} Light Years")
print(f"Wormhole Throat Length:     {WORMHOLE_SHORTCUT_KM:,} km")
print(f"Estimated Transit Time:     {travel_time_mins:.2f} Minutes")

# --- VISUALIZATION GRAPH ---
fig = plt.figure(figsize=(14, 6))
fig.suptitle('The Vastness Paradox: Normal 3D Space vs Wormhole Shortcut', fontsize=16, fontweight='bold')

# Subplot 1: 3D Celestial Map
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot([EARTH[0], TARGET_SECTOR[0]], [EARTH[1], TARGET_SECTOR[1]], [EARTH[2], TARGET_SECTOR[2]], 
         label='Normal 3D Space Path', color='red', linestyle='--', linewidth=2)
ax1.scatter(*EARTH, color='blue', s=100, label='Earth (0,0,0)')
ax1.scatter(*TARGET_SECTOR, color='green', s=100, label=f'Target Sector\n({normal_distance:.1f} LY)')

ax1.set_title('3D Geometric Distance (Light Years)')
ax1.set_xlabel('X (LY)')
ax1.set_ylabel('Y (LY)')
ax1.set_zlabel('Z (LY)')
ax1.legend()
ax1.grid(True)

# Subplot 2: Comparison of Travel Time
ax2 = fig.add_subplot(122)
categories = ['Normal 3D Travel', 'Wormhole Transit']
times = [normal_travel_time_mins, travel_time_mins]

bars = ax2.bar(categories, times, color=['#d9534f', '#5cb85c'], width=0.4)
ax2.set_yscale('log')
ax2.set_title('Time Taken to Destination (Minutes - Log Scale)')
ax2.set_ylabel('Time (Minutes)')

for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:,.1f} mins', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()
