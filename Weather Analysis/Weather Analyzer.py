import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dates = pd.date_range(start="2023-01-01", periods=1000)
np.random.seed(10)
temps = 24 + 10 * np.sin(np.arange(1000) * (2 * np.pi / 365)) + np.random.normal(0, 3, 1000)

temps[150] = 47.8  
temps[450] = -2.5  
temps[750] = 49.1  


df_create = pd.DataFrame({'Date': dates, 'Temp': temps})
df_create.to_csv('Real_Weather.csv', index=False)

df = pd.read_csv('Real_Weather.csv')

mean_temp = np.mean(df['Temp'])
std_temp = np.std(df['Temp'])

upper_limit = mean_temp + (3 * std_temp)
lower_limit = mean_temp - (3 * std_temp)

#
anomalies = df[(df['Temp'] > upper_limit) | (df['Temp'] < lower_limit)]

print(f"Number of anomalies found: {len(anomalies)}")


plt.figure(figsize=(12, 6))

plt.plot(pd.to_datetime(df['Date']), df['Temp'], label='Daily Temperature', color='blue', alpha=0.6)

plt.scatter(pd.to_datetime(anomalies['Date']), anomalies['Temp'], color='red', s=50, label='Weather Anomalies (Outliers)')


plt.title('Weather Patterns & Extreme Temperature Anomalies', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('Weather_Anomalies_Dashboard.png', dpi=300)
plt.show()