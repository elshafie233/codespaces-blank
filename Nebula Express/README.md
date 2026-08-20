
Install with:

```bash
pip install numpy pandas matplotlib
```

## Usage

Run the script directly:

```bash
python delivery_analysis.py
```

This will:
- Print the overall on-time delivery rate to the console
- Save a chart image as `delivery_analysis.png`
- Open the chart in a window (via `plt.show()`)

## Project structure

Everything lives in a single script for simplicity:

| Section | What it covers |
|---|---|
| `generate_pilot_names()` | Builds random pilot names using f-strings and list comprehensions |
| `class delivery` | Stores one delivery's data and computes its base cost |
| Data generation | Uses `numpy` to generate 200 random deliveries |
| `df` (DataFrame) | Combines everything into a single `pandas` table |
| `route_stats` | Grouped stats per origin→destination route |
| `planet_stats` | Grouped stats per origin planet (feeds the bar chart) |
| Plotting section | Builds the 4-panel `matplotlib` figure |

## Known simplifications

- `on_time` and `delivery_days` are generated independently of `distance_ly`, so there's no real correlation between distance and lateness in this version — that's a good next thing to change if you want more realistic data.
- Random seed is fixed (`np.random.seed(42)`) so results are reproducible between runs.

## Ideas to extend

- Make `delivery_days` and `on_time` actually depend on `distance_ly` (e.g. longer distance → higher chance of delay).
- Add a `pivot_table` comparing cost across every origin × destination pair.
- Try `df.query()` instead of boolean indexing for filtering.
- Add a simple linear regression to predict `cost` from `distance_ly` and `weight_kg`.
- Wrap the DataFrame creation in a `try/except` block for practice with error handling.