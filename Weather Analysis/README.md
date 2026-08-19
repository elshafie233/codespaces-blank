# Weather Anomaly Detection Dashboard

Hey there! This project is a quick Python-based tool that simulates historical weather data, hunts down extreme temperature anomalies (outliers), and plots them onto a clean, easy-to-read dashboard. 

It uses a classic statistical approach (the 3-Standard-Deviation rule) to separate normal seasonal weather shifts from genuine extreme events.

## 🚀 What This Script Does

1. **Simulates Realistic Weather:** It creates a 1,000-day dataset. To make it feel real, it uses a sine wave to mimic yearly seasons, throws in some random daily noise, and injects three major weather spikes (extreme heat and extreme cold).
2. **Saves Raw Data:** The generated data automatically exports to a file called `Real_Weather.csv`.
3. **Calculates the "Normal" Range:** It calculates the average temperature and standard deviation, then flags anything that wanders outside 3 standard deviations from the norm.
4. **Builds a Dashboard:** It generates and saves a polished chart (`Weather_Anomalies_Dashboard.png`) that maps out the timeline and marks the anomalies in bright red.

---

## 🛠️ Getting Started

### Prerequisites
You will need Python installed on your machine along with `pandas`, `numpy`, and `matplotlib`. If you don't have them yet, grab them all at once via terminal:

```bash
pip install pandas numpy matplotlib
```

### Running the Code
1. Paste the script into a file named something like `weather_tracker.py`.
2. Uncomment the line `# anomalies = df[...]` in your code so the script actually runs the filter! 
3. Run it in your terminal:

```bash
python weather_tracker.py
```

---

## 📊 Reading the Dashboard Chart

When the plot pops up, here is what you are looking at:
* **The Blue Line:** Your everyday temperature baseline moving up and down with the changing seasons.
* **The Red Dots:** The rule-breakers. These are the extreme weather events that broke past our statistical thresholds. 

The console will also give you a quick printout of the exact number of anomalies caught during the run.

---

## 💡 Quick Dev Note
The code uses `np.random.seed(10)`. This means the random noise generated will be exactly the same every single time you run it, making it perfect for testing and debugging without the data moving under your feet!
