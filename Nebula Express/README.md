🚀 Nebula Express Interstellar Logistics Simulator
Hey! This is a clean, straightforward Python workflow I set up to simulate interstellar logistics and shipping transactions across a fictional star system. 

It handles custom Object-Oriented Programming (OOP) data creation, feature engineering with random noise variations, data grouping, and wraps everything up with a polished, 4-panel matplotlib dashboard.

🚀 What the Script Does
* Generates Synthetic Star Data: It builds a structured space shipping list of 200 items using customized NumPy probability distributions and automated random pilot name lists.
* Object-Oriented Math: It utilizes a custom `delivery` class structure to automatically map distances and weight tiers straight into base operational shipping credits.
* Grouping & Statistics: It groups your shipping records into dual tables (`route_stats` and `planet_stats`) to instantly extract aggregate averages for costs, transit days, and route-specific delays.
* Generates a Multi-Panel Plot: It outputs a high-resolution, 4-panel data dashboard image (`delivery_analysis.png`) displaying delivery cost distributions, performance scatter charts, and operational bar rankings side-by-side.

🛠️ Requirements & Run Instructions
To get this running, make sure you have the standard data stack installed:

pip install numpy pandas matplotlib

Run the main file directly from your terminal workspace:

python delivery_analysis.py

📂 Script Processing Structure
The script relies entirely on structured in-memory pandas workflows rather than local external spreadsheets to remain completely independent and lightweight:

* Class Setup ➡️ Defines underlying transactional criteria and baseline cost multipliers.
* Data Matrix ➡️ Assembles raw data arrays securely into a uniform `df` DataFrame matrix.
* Aggregation ➡️ Splits multi-planet tracking arrays into distinct, easy-to-read route groups.
* Export Phase ➡️ Batches the final matplotlib visual objects straight into your local workspace.

📊 Reading the Visual Output
When the final graphic pops up:

* The Bar Graph: Tracks the total cost differences across varying originating planets.
* The Scatter Plot: Maps shipping costs against light-year distances, shaded sequentially to flag on-time metrics.
* The Histogram: Groups delivery timelines together so you can pinpoint common shipping delay clusters.
* Horizontal Profiles: Ranks individual transit pilots to reveal which ones maintain the highest operational cost values.
