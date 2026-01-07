# Asana RL Seed Data Simulation
This repository contains an enterprise-scale simulation of an Asana workspace, designed to generate high-quality seed data for evaluating and training reinforcement learning (RL) agents on computer-use tasks.

The dataset and schema are modeled to closely reflect how real B2B SaaS organizations use Asana, with an emphasis on realistic structure, distributions, and temporal behavior.


# Setup Instructions
1. Clone the repository
   git clone https://github.com/hiranmayi05/Asana-simulation.git
   cd asana-simulation

3. Create and activate a virtual environment (recommended)

Windows

python -m venv venv

venv\Scripts\Activate.ps1


macOS / Linux

python3 -m venv venv
 source venv/bin/activate

3. Install dependencies
   
    pip install -r requirements.txt

5. Configure environment variables

Copy the example file:

 cp .env.example .env


# Edit .env if needed

 EMPLOYEE_COUNT=7500
 
This controls the scale of the generated dataset.

▶️ Running the Data Generator

Before running, ensure no existing database is locked or open.

python src/main.py

Recommended - Delete existing database before regenerating

Run sequence:

del output\asana_simulation.sqlite

python src/main.py

After execution, the generated database will be available at:

output/asana_simulation.sqlite
