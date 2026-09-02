## EV Battery Degradation Simulator

A lightweight Python tool built to simulate, calculate, and visualize the long-term State of Health (SOH) of electric vehicle batteries under different operational and environmental conditions. 

This project applies Object-Oriented Programming (OOP) principles and data visualization to model how steady cycling wear interacts with accelerated thermal damage to impact battery longevity.

### Core Concepts & Simulation Physics

Real-world lithium-ion batteries do not degrade linearly. This script implements a discrete degradation model based on two primary physical factors:
1. **Base Cycle Damage:** Standard operational wear (`0.005%` capacity loss) that accumulates linearly with every charge/discharge cycle.
2. **Thermal Accelerated Degradation:** A conditional multiplier (`0.015%` extra damage) triggered when the ambient temperature exceeds **35°C**, simulating real-world battery cell stress under harsh climates.

The simulation loops through daily environment updates, accumulates damage parameters, and enforces a strict lower bound boundary where the battery SOH cannot drop below `0.0%`.

### Features
* **Object-Oriented Design:** Structured around a clean `EVBattery` class that manages states, daily metrics, and internal logic.
* **Environmental Tracking:** Dynamic updates of the active battery temperature array based on user input.
* **Matplotlib Visualizations:** Automatically plots a clear, production-ready degradation curve mapping SOH (%) over custom time horizons.
* **Interactive CLI:** Prompt-driven simulation parameters allowing you to test specific days and localized climate scenarios on the fly.

### Tech Stack
* **Language:** Python 3.x
* **Data Visualization:** Matplotlib

### File Structure & Methods

* `EVBattery.__init__()`: Sets up the base state (SOH at 100%, 60 kWh capacity, counters, and history lists for data tracking).
* `EVBattery.update_env()`: Updates the internal temperature state depending on external ambient conditions.
* `EVBattery.degrade()`: Handles the math behind capacity fading and checks boundary conditions (`max(0.0, self.soh)`).
* `EVBattery.drive_and_charge()`: Iterates through the full time-loop to simulate daily operational degradation and append historical records for plotting.

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Install dependencies:**
   Ensure you have the required visualization library installed:
   ```bash
   pip install matplotlib
   ```

3. **Run the script:**
   ```bash
   python battery_sim.py
   ```

4. **Example Simulation:**
   ```text
   Enter number of days: 365
   Enter temperature (°C): 38
   
   After 365 days:
   SOH: 92.70%
   Total Cycles: 365
   Recorded Days Count: 365
   ```
