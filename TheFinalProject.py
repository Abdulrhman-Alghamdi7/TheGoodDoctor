import customtkinter
from customtkinter import *
import tkinter as tk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("350x550")
root.title('الطبيب الطيب')

def save_2():
    global name, id
    
    name = str(entry1.get())
    id = str(entry2.get())
    if name == '' or id == '' or len(id)!=10 or (len(name.split(' ')) < 3):
        verror = customtkinter.CTkLabel(frame2, text="الرجاء ادخال المعلومات صحيحة وكاملة", font=("inherit", 10, "bold"),text_color='red')
        verror.pack(pady=12, padx=10)
    else:
        frame2.pack_forget()
        frame3.pack(pady=20, padx=60, fill="both", expand=True)
        frame4.pack_forget()

def save_3():
    global age_value, height_value, weight_value, blood_pressure_value, user_data
    try:
        age_value = int(age_entry.get())
        height_value = int(height_entry.get())
        if str(height_value)[1] != "":
            height_value = float(height_value) / 100
        weight_value = int(weight_entry.get())
        blood_pressure_value = str(blood_pressure_entry.get())
        if blood_pressure_value == '0':
            diastolic = None
            systolic_pressure = None
        else:
            if '/' in blood_pressure_value:
                blood_pressure_value = (''.join(blood_pressure_value.split(' '))).split('/')
                if len(blood_pressure_value) == 2:
                    diastolic = int(blood_pressure_value[0])
                    systolic_pressure = int(blood_pressure_value[1])
                else:
                    verror = customtkinter.CTkLabel(frame3, text="الرجاء ادخال ضغط الدم بشكل صحيح", font=("inherit", 13, "bold"),text_color='red')
                    
                    verror.pack(pady=12, padx=10)
            else:
                verror = customtkinter.CTkLabel(frame3, text="الرجاء ادخال ضغط الدم بشكل صحيح", font=("inherit", 13, "bold"),text_color='red')
                verror.pack(pady=12, padx=10)

        bmi_value = int((float(weight_value) / float(height_value) ** 2))
        heat_value = int(heat_entry.get())
        if heat_value == 0:
            heat_value = None
        else:
            if heat_value>42:
                heat_value = (heat_value-32)/1.8
    except ValueError:
         verror = customtkinter.CTkLabel(frame3, text="الرجاء كتابة ارقام فقط", font=("inherit", 13, "bold"),text_color='red')
         aerror = customtkinter.CTkLabel(frame3, text="'في حالة عدم وجود اي من\n القيم الاختيارية اكتب '0'", font=("inherit", 15, "bold"),text_color='red')
         aerror.pack(pady=12, padx=10)      
         verror.pack(pady=12, padx=10)
    else:
        # Store the data in a dictionary
        user_data = {
            'ID':id,
            'Name': name,
            "Age": age_value,
            "Height": height_value,
            "Weight": weight_value,
            "Diastolic": diastolic,
            'Systolic Pressure' : systolic_pressure,
            "BMI" : bmi_value,
            'Heat' : heat_value
        }
        frame3.pack_forget()
        frame4.pack(pady=20, padx=60, fill="both", expand=True)

# def save_4():
    

frame2 = customtkinter.CTkFrame(master=root)
frame3 = customtkinter.CTkFrame(master=root)
frame4 = customtkinter.CTkFrame(master=root)

label1 = customtkinter.CTkLabel(master=frame2, text="المعلومات الشخصية", font=("Roboto", 24))
label1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame2, placeholder_text="الاسم الثلاثي")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame2, placeholder_text="الهوية الوطنية او الاقامة")
entry2.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame2,text="تفضل", command=save_2)
button1.pack(pady=12, padx=10)

heading = customtkinter.CTkLabel(frame3, text="الرجاء تعبئة البيانات", font=("inherit", 23, "bold"))
heading.pack(pady=5, padx=10)

# Create entry widgets with integer validation
age_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="العمر")
age_entry.pack(pady=12, padx=10)

height_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="الطول")
height_entry.pack(pady=12, padx=10)

weight_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="الوزن")
weight_entry.pack(pady=12, padx=10)

bplable = customtkinter.CTkLabel(frame3, text="الانبساطي / الانقباضي 'من اليسار الى اليمين'", font=("inherit", 10, "bold"))
bplable.pack()
#  
blood_pressure_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="ضغط الدم (اختياري)")
blood_pressure_entry.pack(pady=12, padx=10)

heat_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="درجة الحرارة (اختياري)")
heat_entry.pack(pady=12, padx=10)
# Create a button to trigger the calculation or further actions
button2 = customtkinter.CTkButton(master=frame3,text="اكمل", command=save_3)
button2.pack(pady=12)

frame2.pack(pady=20, padx=12)
heading.pack(pady=5, padx=10)


my_frame = customtkinter.CTkFrame(master=frame4)

heading = customtkinter.CTkLabel(master=frame4, text="اكتب جميع الاعراض \nالتي تعاني منها بدقة", font=("inherit", 23, "bold"))
heading.pack(pady=10, padx=10)

symptoms = customtkinter.CTkEntry(master=frame4)
symptoms.pack(pady=10, padx=10)
# Create a button to trigger the calculation or further actions
button3 = customtkinter.CTkButton(master=frame4,text="اكمل")#, command=save_4)
button3.pack(pady=12)

root.mainloop()
