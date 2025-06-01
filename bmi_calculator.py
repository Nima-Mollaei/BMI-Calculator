import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height_cm = float(entry_height.get())
        weight_kg = float(entry_weight.get())

        if height_cm <= 0 or weight_kg <= 0:
            raise ValueError

        height_m = height_cm / 100
        bmi = round(weight_kg / (height_m ** 2), 2)

        if bmi < 18.5:
            status = "Underweight"
            color = "#ffb74d"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
            color = "#81c784"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
            color = "#ffca28"
        else:
            status = "Obese"
            color = "#e57373"

        result_label.config(text=f"BMI: {bmi} — {status}", fg=color)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# --------- Modern Themed UI ---------
window = tk.Tk()
window.title("🌟 BMI Calculator")
window.geometry("400x350")
window.configure(bg="#f4f6f8")

FONT = ("Segoe UI", 12)

frame = tk.Frame(window, bg="white", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=305)

tk.Label(frame, text="BMI Calculator", font=("Segoe UI", 16, "bold"), bg="white", fg="#2c3e50").pack(pady=10)

tk.Label(frame, text="Weight (kg):", font=FONT, bg="white", anchor="w").pack(pady=(5, 0))
entry_weight = tk.Entry(frame, font=FONT, bg="#f1f1f1", justify="center", relief="solid")
entry_weight.pack(pady=5)

tk.Label(frame, text="Height (cm):", font=FONT, bg="white", anchor="w").pack(pady=(10, 0))
entry_height = tk.Entry(frame, font=FONT, bg="#f1f1f1", justify="center", relief="solid")
entry_height.pack(pady=5)

tk.Button(frame, text="💡 Calculate", font=FONT, bg="#2196f3", fg="white", relief="flat", command=calculate_bmi).pack(pady=15)

result_label = tk.Label(frame, text="", font=("Segoe UI", 13, "bold"), bg="white")
result_label.pack()

window.mainloop()
