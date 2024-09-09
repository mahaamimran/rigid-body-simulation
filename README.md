# Rigid Body Rotation Simulator

This Python project simulates the rigid body rotation using Euler's equations. The program calculates the behavior of a rigid body under the influence of torques, based on angular velocities and moments of inertia.

## Features

- Simulates rigid body rotation using Euler's equations
- Input fields for setting moments of inertia and initial angular velocities
- Plots angular velocities over time using Matplotlib

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rigid-body-simulator.git
cd rigid-body-simulator
```

### 2. Install dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Simulation

To start the simulation, simply run the `rigid_body_simulation.py` file:

```bash
python rigid_body_simulation.py
```

## Features and Inputs

This program uses Euler's equations to calculate the angular velocity of a rigid body over time, given the moments of inertia and initial angular velocities.

- **Moments of inertia (I_x, I_y, I_z):** Define how mass is distributed relative to each axis of rotation.
- **Initial angular velocities (omega_x, omega_y, omega_z):** Initial conditions for angular velocity along the x, y, and z axes.
