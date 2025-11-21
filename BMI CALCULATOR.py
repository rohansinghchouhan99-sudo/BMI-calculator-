import tkinter as tk
from tkinter import messagebox
from math import pow

def calculate_bmi():
    try:
        # Get input values from the Entry widgets
        weight_kg = float(weight_entry.get())
        height_cm = float(height_entry.get())
        
        # Input validation
        if weight_kg <= 0 or height_cm <= 0:
            messagebox.showerror("Input Error", "Weight and Height must be positive numbers.")
            return

        # Convert height from cm to meters
        height_m = height_cm / 100.0
        
        # BMI Formula: weight (kg) / height (m)^2
        bmi_value = weight_kg / pow(height_m, 2)
        
        # Determine the BMI category
        category = ""
        if bmi_value < 18.5:
            category = "Underweight"
            color = "#3498db"  # Blue
        elif 18.5 <= bmi_value < 25.0:
            category = "Normal Weight"
            color = "#2ecc71"  # Green
        elif 25.0 <= bmi_value < 30.0:
            category = "Overweight"
            color = "#f39c12"  # Orange
        else:
            category = "Obesity"
            color = "#e74c3c"  # Red

        # Update the result label with the calculated BMI and category
        result_text = f"BMI: {bmi_value:.2f}\nCategory: {category}"        #check bmi upto 2 decimal places
        result_label.config(text=result_text, fg=color, font=('Arial', 16, 'bold'))    # updates gui 

    except ValueError:
        # Handles errors if the user enters non-numeric text
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")
    except Exception as e:
        # General error handling
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# --- 1. Setup the main window ---
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.config(bg="#ecf0f1") # Light gray background for a clean look

# Define consistent styling for labels and entries
FONT_STYLE = ('Arial', 12)
PAD_Y = 10

# --- 2. Title Label ---
title_label = tk.Label(root, text="Body Mass Index Calculator", font=('Arial', 18, 'bold'), bg="#ecf0f1", fg="#2c3e50")
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="n")

# --- 3. Weight Input (Kilograms) ---
weight_label = tk.Label(root, text="Weight (kg):", font=FONT_STYLE, bg="#ecf0f1", fg="#34495e")
weight_label.grid(row=1, column=0, padx=10, pady=PAD_Y, sticky="w")

weight_entry = tk.Entry(root, font=FONT_STYLE, width=15, bd=2, relief=tk.FLAT)
weight_entry.grid(row=1, column=1, padx=10, pady=PAD_Y, sticky="e")

# --- 4. Height Input (Centimeters) ---
height_label = tk.Label(root, text="Height (cm):", font=FONT_STYLE, bg="#ecf0f1", fg="#34495e")
height_label.grid(row=2, column=0, padx=10, pady=PAD_Y, sticky="w")

height_entry = tk.Entry(root, font=FONT_STYLE, width=15, bd=2, relief=tk.FLAT)
height_entry.grid(row=2, column=1, padx=10, pady=PAD_Y, sticky="e")

# --- 5. Calculate Button ---
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    font=('Arial', 14, 'bold'),
    bg="#16a085",  # Teal color
    fg="white",
    activebackground="#1abc9c",
    activeforeground="white",
    relief=tk.RAISED,
    bd=0,
    padx=20,
    pady=10,
    command=calculate_bmi # Link to the function
)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# --- 6. Result Display Label ---
result_label = tk.Label(
    root,
    text="Enter values and click 'Calculate'",
    font=('Arial', 14),
    bg="#ecf0f1",
    fg="#34495e",
    justify=tk.LEFT
)
result_label.grid(row=4, column=0, columnspan=2, pady=(10, 20))

# Configure the grid columns to center the content
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# --- 7. Run the Tkinter main loop ---
root.mainloop()
