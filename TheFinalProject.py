import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def save_2():
    # Get the values from the entry fields
    global age_value, height_value, weight_value, blood_pressure_value, user_data
    try:
        age_value = int(age_entry.get())
        height_value = int(height_entry.get())
        if str(height_value)[1] != ".":
            height_value = float(height_value) / 100
        weight_value = int(weight_entry.get())
        blood_pressure_value = int(blood_pressure_entry.get())
        bmi_value = int((float(weight_value) / float(height_value) ** 2))
    except ValueError:
        verror = customtkinter.CTkLabel(my_frame, text="الرجاء كتابة ارقام فقط", font=("inherit", 13, "bold"),text_color='red')
        verror.pack(pady=12, padx=10)
        return

    # Store the data in a dictionary
    user_data = {
        "Age": age_value,
        "Height": height_value,
        "Weight": weight_value,
        "Blood Pressure": blood_pressure_value,
        "BMI": bmi_value
    }


root = customtkinter.CTk()
root.title("الطبيب الطيب")
root.geometry("350x550")

my_frame = customtkinter.CTkFrame(master=root)
my_frame.pack(pady=20, padx=60, fill="both", expand=True)

heading = customtkinter.CTkLabel(my_frame, text="الرجاء تعبئة البيانات", font=("inherit", 23, "bold"))
heading.pack(pady=5, padx=10)

# Create entry widgets with integer validation
age_entry = customtkinter.CTkEntry(master=my_frame, placeholder_text="العمر")
age_entry.pack(pady=12, padx=10)

height_entry = customtkinter.CTkEntry(master=my_frame, placeholder_text="الطول")
height_entry.pack(pady=12, padx=10)

weight_entry = customtkinter.CTkEntry(master=my_frame, placeholder_text="الوزن")
weight_entry.pack(pady=12, padx=10)

blood_pressure_entry = customtkinter.CTkEntry(master=my_frame, placeholder_text="ضغط الدم")
blood_pressure_entry.pack(pady=12, padx=10)

# Create a button to trigger the calculation or further actions
button = customtkinter.CTkButton(master=my_frame, text="اكمل", command=save_2)
button.pack(pady=12)


root.mainloop()
