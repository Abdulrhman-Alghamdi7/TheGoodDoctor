from tkinter import *
from tkinter import messagebox

def create_integer_entry(parent, placeholder):
    def on_validate_input(value):
        if value == "" or value.isdigit():
            return True
        return False

    entry = Entry(parent, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11),
                  validate="key", validatecommand=(on_validate_input, "%P"))
    entry.insert(0, placeholder)
    return entry

def save_2():
    # Get the values from the entry fields
    global age_value , hight_value , weight_value , bloodpresure_value
    try:
        age_value = int(age_entry.get())

        hight_value = int(hight_entry.get())

        if str(hight_value)[1] != ".":
            hight_value = float(hight_value) / 100

        weight_value = int(weight_entry.get())

        bloodpresure_value = int(bloodpresure_entry.get())

        bmi_value = int((float(weight_value)/float(hight_value)**2))
    except ValueError:
        verror = Label(my_frame, text="الرجاء كتابة ارقام فقط", bg="#2c2f33", fg="#ffffff", font=("inherit", 23, "bold"))
        verror.place(x=10, y=5)
        return
        
    # Store the data in a dictionary
    user_data = {
        "Age": age_value,
        "Height": hight_value,
        "Weight": weight_value,
        "Blood Pressure": bloodpresure_value,
        "BMI": bmi_value
    }

    # Display the data in a message box
    result_text = "\n".join([f"{key}: {value}" for key, value in user_data.items()])
    messagebox.showinfo("Results", result_text)

root = Tk()
root.title("Login")
root.geometry("350x550")
root.configure(bg="#2c2f33")
root.resizable(True, True)

my_frame = Frame(root, width=1000, height=1000, bg="#2c2f33")
my_frame.place(x=75, y=50)

heading = Label(my_frame, text="الرجاء تعبئة البيانات", bg="#2c2f33", fg="#ffffff", font=("inherit", 23, "bold"))
heading.place(x=10, y=5)

# Create entry widgets with integer validation
age_entry = create_integer_entry(my_frame, "العمر")
age_entry.place(x=10, y=80)

hight_entry = create_integer_entry(my_frame, "الطول")
hight_entry.place(x=10, y=150)

weight_entry = create_integer_entry(my_frame, "الوزن")
weight_entry.place(x=10, y=220)

bloodpresure_entry = create_integer_entry(my_frame, "الضغط")
bloodpresure_entry.place(x=10, y=290)

Frame(my_frame, width=295, height=2, bg="black").place(x=25, y=177)

# Create a button to trigger the calculation or further actions
Button(my_frame, width=20, pady=7, text='اكمل', bg='#57a1f8', fg='white', border=0, command=save_2).place(x=30, y=350)

root.mainloop()
