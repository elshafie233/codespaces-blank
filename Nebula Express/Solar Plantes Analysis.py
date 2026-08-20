import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42) 

PLANETS = ["Mercuria", "Venusia", "Earthos", "Marsford", "Jupitran", "Saturnyx"]

def generate_pilot_names(n):
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"]
    return [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(n)]


class delivery:
    def __init__(self, delivery_id, origin, destination, distance_ly, weight_kg, pilot):
        self.delivery_id = delivery_id
        self.origin = origin
        self.destination = destination
        self.distance_ly = distance_ly
        self.weight_kg = weight_kg
        self.pilot = pilot

    def base_cost(self):
        return self.distance_ly * 120 + self.weight_kg * 8

n = 200
origins = np.random.choice(PLANETS, size=n)
destinations = np.random.choice(PLANETS, size=n)
distances = np.round(np.random.exponential(scale=15, size=n) + 1, 2)
weights = np.round(np.random.uniform(0.5, 50, size=n), 2)
pilots = generate_pilot_names(n)

deliveries = [delivery(i, origins[i], destinations[i], distances[i], weights[i], pilots[i]) for i in range(n)]

if origins[0] == destinations[0]:
    print(f"Warning: Delivery {deliveries[0].delivery_id} has the same origin and destination.")

costs = np.array([d.base_cost() for d in deliveries])
noise = np.random.normal(0, 15, size=len(costs)) 
final_costs = np.round(np.clip(costs + noise, 20, None), 2)

delivery_days = np.random.randint(1, 15, size=n)
on_time = np.random.choice([True, False], size=n, p=[0.85, 0.15])

df = pd.DataFrame({
    "delivery_id": [dl.delivery_id for dl in deliveries],
    "origin": [dl.origin for dl in deliveries],
    "destination": [dl.destination for dl in deliveries],
    "pilot": [dl.pilot for dl in deliveries],
    "distance_ly": [dl.distance_ly for dl in deliveries],
    "weight_kg": [dl.weight_kg for dl in deliveries],
    "cost": final_costs,
    "delivery_days": delivery_days,
    "on_time": on_time,
})

route_stats = df.groupby(["origin", "destination"]).agg(
    total_deliveries=pd.NamedAgg(column="delivery_id", aggfunc="count"),
    average_cost=pd.NamedAgg(column="cost", aggfunc="mean"),
    average_delivery_days=pd.NamedAgg(column="delivery_days", aggfunc="mean"),
    on_time_percentage=pd.NamedAgg(column="on_time", aggfunc=lambda x: np.mean(x) * 100)
).reset_index()


planet_stats = df.groupby("origin").agg(
    average_cost=pd.NamedAgg(column="cost", aggfunc="mean")
).sort_values("average_cost", ascending=False)

on_time_rate = df["on_time"].mean() * 100
print(f"Overall on-time delivery rate: {on_time_rate:.2f}%")

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

planet_stats["average_cost"].plot(kind="bar", ax=axes[0, 0], color="slateblue")
axes[0, 0].set_title("Average Cost by Origin Planet")
axes[0, 0].set_ylabel("Cost (credits)")

axes[0, 1].scatter(df["distance_ly"], df["cost"], alpha=0.5, c=df["on_time"], cmap="coolwarm")
axes[0, 1].set_title("Distance vs Cost")
axes[0, 1].set_xlabel("Distance (light years)")

axes[1, 0].hist(df["delivery_days"], bins=20, color="teal", edgecolor="black")
axes[1, 0].set_title("Delivery Time Distribution")

pilot_avg = df.groupby("pilot")["cost"].mean().sort_values(ascending=False).head(6)
pilot_avg.plot(kind="barh", ax=axes[1, 1], color="darkorange")
axes[1, 1].set_title("Top Pilots by Avg Delivery Cost")

plt.tight_layout()
plt.savefig("delivery_analysis.png", dpi=150)
plt.show()