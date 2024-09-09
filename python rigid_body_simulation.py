import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Define Euler's equations of motion
def euler_eqs(omega, t, I_x, I_y, I_z, tau_x, tau_y, tau_z):
    omega_x, omega_y, omega_z = omega
    
    # Euler's equations of motion
    omega_dot_x = (tau_x - (I_z - I_y) * omega_y * omega_z) / I_x
    omega_dot_y = (tau_y - (I_x - I_z) * omega_z * omega_x) / I_y
    omega_dot_z = (tau_z - (I_y - I_x) * omega_x * omega_y) / I_z
    
    return [omega_dot_x, omega_dot_y, omega_dot_z]

# Function to run the simulation
def run_simulation():
    try:
        # Get input values
        I_x = float(inertia_x.get())
        I_y = float(inertia_y.get())
        I_z = float(inertia_z.get())
        tau_x = float(torque_x.get())
        tau_y = float(torque_y.get())
        tau_z = float(torque_z.get())
        
        # Initial conditions for angular velocities (omega_x, omega_y, omega_z)
        initial_conditions = [1.0, 0.5, 0.0]

        # Time points to simulate
        time_points = np.linspace(0, 10, 1000)

        # Solve the system of ODEs
        omega_solution = odeint(euler_eqs, initial_conditions, time_points, args=(I_x, I_y, I_z, tau_x, tau_y, tau_z))

        # Extract solutions for each angular velocity component
        omega_x_solution = omega_solution[:, 0]
        omega_y_solution = omega_solution[:, 1]
        omega_z_solution = omega_solution[:, 2]

        # Plot the results
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, omega_x_solution, label=r'$\omega_x$', color='r')
        plt.plot(time_points, omega_y_solution, label=r'$\omega_y$', color='g')
        plt.plot(time_points, omega_z_solution, label=r'$\omega_z$', color='b')
        plt.title('Rigid Body Rotation - Euler\'s Equations')
        plt.xlabel('Time')
        plt.ylabel('Angular Velocity')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError:
        print("Please enter valid numbers for all inputs.")

# Create the main window
root = tk.Tk()
root.title("Rigid Body Rotation Simulation")

# Create and arrange input fields for moments of inertia and torques
ttk.Label(root, text="Moment of Inertia I_x:").grid(column=0, row=0, padx=10, pady=5)
inertia_x = ttk.Entry(root)
inertia_x.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Moment of Inertia I_y:").grid(column=0, row=1, padx=10, pady=5)
inertia_y = ttk.Entry(root)
inertia_y.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Moment of Inertia I_z:").grid(column=0, row=2, padx=10, pady=5)
inertia_z = ttk.Entry(root)
inertia_z.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(root, text="Torque τ_x:").grid(column=0, row=3, padx=10, pady=5)
torque_x = ttk.Entry(root)
torque_x.grid(column=1, row=3, padx=10, pady=5)

ttk.Label(root, text="Torque τ_y:").grid(column=0, row=4, padx=10, pady=5)
torque_y = ttk.Entry(root)
torque_y.grid(column=1, row=4, padx=10, pady=5)

ttk.Label(root, text="Torque τ_z:").grid(column=0, row=5, padx=10, pady=5)
torque_z = ttk.Entry(root)
torque_z.grid(column=1, row=5, padx=10, pady=5)

# Create the "Run Simulation" button
ttk.Button(root, text="Run Simulation", command=run_simulation).grid(column=0, row=6, columnspan=2, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
