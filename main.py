from tkinter import *
from tkinter import messagebox
from tkinter import  ttk
from datetime import datetime
import json
from variables import allWorker, employee_id_counter



window = Tk()
window.geometry("960x610")
window.title('My Company')
window.config(bg='gray')
window.resizable(0, 0)

label_main_page = Label(window, text='Welcome to Azer Business House',
                        fg='white', bg='#303e4d', font=("Charlesworth", 35, "bold"))
label_main_page.place(relx=0.1, rely=0.09, relwidth=0.8, relheight=0.1)

btnLogin = Button(window, text="Login", bg='#303e4d', font=("Charlesworth", 17, "bold"), command=lambda: login())
btnLogin.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.08)

import json

            # Function to save worker data to a JSON file
def save_worker_data(file_name, allWorker):
    try:
        # Attempt to open the file and read existing data
        with open(file_name, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or contains invalid JSON, create an empty dictionary
        data = {}

    # Add the allWorker dictionary data
    data.update(allWorker)

    # Write the updated data back to the file
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)  # Pretty print the JSON data

    print(f"All worker data saved to {file_name}")

global mainpage
mainpage = PhotoImage(file='images/mainpg.gif')
imageLabel = Label(window, image=mainpage)
imageLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

label_main_page.lift()
btnLogin.lift()

frame_login = None
admin_panel = None
employeeAdding_panel = None
editEmployeeInfo_panel = None
deleteEmployee_panel = None
allEmployees_panel = None


def clear_frames():
    global frame_login, admin_panel, employeeAdding_panel, editEmployeeInfo_panel, deleteEmployee_panel, allEmployees_panel
    if frame_login:
        frame_login.destroy()
        frame_login = None
    if admin_panel:
        admin_panel.destroy()
        admin_panel = None
    if employeeAdding_panel:
        employeeAdding_panel.destroy()
        employeeAdding_panel = None
    if editEmployeeInfo_panel:
        editEmployeeInfo_panel.destroy()
        editEmployeeInfo_panel = None
    if deleteEmployee_panel:
        deleteEmployee_panel.destroy()
        deleteEmployee_panel = None
    if allEmployees_panel:
        allEmployees_panel.destroy()
        allEmployees_panel = None


def validate_credentials():
    email = email_entry.get()
    password = password_entry.get()

    if email == 'adminbusiness@gmail.com' and password == 'hormetliolasan':
        adminPanel()
    else:
        messagebox.showerror("Login Error", "Wrong credentials")


def login():
    clear_frames()  # Clear any other frames before showing login frame
    global frame_login, email_entry, password_entry
    frame_login = Frame(window, bg='#141f2b')
    frame_login.pack(expand=True, fill=BOTH)

    label_email = Label(frame_login, text='Email:', fg='white', bg='#141f2b', font=("Charlesworth", 14, "bold"))
    label_email.place(relx=0.3, rely=0.35)

    email_entry = Entry(frame_login, font=("Charlesworth", 14, "bold"))
    email_entry.place(relx=0.44, rely=0.35, relwidth=0.42, relheight=0.05)

    label_password = Label(frame_login, text='Password:', fg='white', bg='#141f2b', font=("Charlesworth", 14, "bold"))
    label_password.place(relx=0.3, rely=0.43)

    password_entry = Entry(frame_login, font=("Charlesworth", 14, "bold"), show='*')
    password_entry.place(relx=0.44, rely=0.43, relwidth=0.42, relheight=0.05)

    global showPassword
    showPassword = PhotoImage(file='images/showpassword.png')
    shwP_button = Button(frame_login, image=showPassword, bd=0, bg='#141f2b', command=lambda: showPassword_f())
    shwP_button.place(relx=0.87, rely=0.43, relwidth=0.05, relheight=0.05)

    def showPassword_f():
        if password_entry.cget('show') == '*':
            password_entry.config(show='')
        else:
            password_entry.config(show='*')

    submit_button = Button(frame_login, text='Submit', bg='black', fg='white',
                           font=("Charlesworth", 14, "bold"), command=validate_credentials)
    submit_button.place(relx=0.55, rely=0.53, relheight=0.08, relwidth=0.15)

    label_main_page = Label(frame_login, text='Azer Business House',
                            fg='white', bg='#141f2b', font=("Charlesworth", 35, "bold"))
    label_main_page.place(relx=0.3, rely=0.09, relwidth=0.5, relheight=0.1)

    global business
    business = PhotoImage(file='images/business.png')
    imageLabel = Label(frame_login, image=business, bd=0, bg='#141f2b')
    imageLabel.place(relx=0.0, rely=0.3, relwidth=0.3, relheight=0.35)

    quote_label = Label(frame_login, text="-----Don't wait for opportunity. Create it-----",
                        fg='white', bg='#141f2b', font=("Charlesworth", 25, "bold"))
    quote_label.place(relx=0.0, rely=0.9, relwidth=1, relheight=0.08)

    global backPhotoLogin
    backPhotoLogin = PhotoImage(file='images/back_icon.png')
    back_button = Button(frame_login, image=backPhotoLogin, bd=0, bg='#141f2b', command=lambda: goToMainPage())
    back_button.place(relx=0.06, rely=0.02, relheight=0.09, relwidth=0.07)


def adminPanel():
    clear_frames()  # Clear any other frames before showing admin panel
    global admin_panel

    admin_panel = Frame(window, bg='#141f2b')
    admin_panel.pack(expand=True, fill=BOTH)

    admin_panel_settings = Frame(admin_panel, bg='#81a3a0').place(relx=0.0, rely=0.0, relwidth=0.28, relheight=1)
    admin_panel_page = Frame(admin_panel, bg='#539dad').place(relx=0.28, rely=0.0, relwidth=0.72, relheight=1)

    settings_label = Label(admin_panel_settings, text='Settings:',
                           fg='white', bg='black',
                           font=("Charlesworth", 14, "bold"))
    settings_label.place(relx=0.01, rely=0.03, relheight=0.08, relwidth=0.23)

    add_employee_button = Button(admin_panel_settings, text='Add new worker', bg='black', fg='white',
                                 font=("Charlesworth", 14, "bold"), command=lambda: add_employee())
    add_employee_button.place(relx=0.01, rely=0.14, relheight=0.08, relwidth=0.23)

    def adminChangePanel():
        clear_frames()  # Clear any other frames before showing admin panel
        global admin_panel

        admin_panel = Frame(window, bg='#141f2b')
        admin_panel.pack(expand=True, fill=BOTH)

        admin_panel_settings = Frame(admin_panel, bg='#81a3a0')
        admin_panel_settings.place(relx=0.0, rely=0.0, relwidth=0.28, relheight=1)
        admin_panel_page = Frame(admin_panel, bg='#539dad')
        admin_panel_page.place(relx=0.28, rely=0.0, relwidth=0.72, relheight=1)

        add_employee_button = Button(admin_panel_settings, text='Add new worker', bg='black', fg='white',
                                     font=("Charlesworth", 14, "bold"), command=lambda: add_employee())
        add_employee_button.place(relx=0.01, rely=0.14, relheight=0.08, relwidth=0.23)

    def validate_letters(char):
        return char.isalpha() or char == ''

    def add_employee():
        clear_frames()  # Clear frames before switching to add employee page
        global employeeAdding_panel
        employeeAdding_panel = Frame(window, bg='#141f2b')  # Separate employee panel
        employeeAdding_panel.pack(expand=True, fill=BOTH)

        def on_back_button_click():
            response = messagebox.askyesno("Confirm",
                                           "Are you sure you want to go back to the login panel? Unsaved changes may be lost.")
            if response:
                goToAdminPage()

        back_button = Button(employeeAdding_panel, image=backPhotoLogin, bd=0, bg='#141f2b',
                             command=on_back_button_click)
        back_button.place(relx=0.002, rely=0.01, relheight=0.09, relwidth=0.07)

        def capitalize_first_letter(event, entry):
            content = entry.get()
            entry.delete(0, END)
            entry.insert(0, content.title())

        vcmd = (window.register(validate_letters), '%S')

        employeeName_label = Label(employeeAdding_panel, text='Name:', fg='white', bg='#141f2b',
                                   font=("Charlesworth", 13, "bold"))
        employeeName_label.place(relx=0.08, rely=0.05)
        employeeName_entry = Entry(employeeAdding_panel, font=("Charlesworth", 13, "bold"), validate="key", validatecommand=vcmd)
        employeeName_entry.place(relx=0.14, rely=0.0487, relwidth=0.16, relheight=0.04)
        employeeName_entry.bind("<KeyRelease>", lambda event: capitalize_first_letter(event, employeeName_entry))

        employeeSurname_label = Label(employeeAdding_panel, text='Surname:', fg='white', bg='#141f2b',
                                      font=("Charlesworth", 13, "bold"))
        employeeSurname_label.place(relx=0.35, rely=0.05)
        employeeSurname_entry = Entry(employeeAdding_panel, font=("Charlesworth", 13, "bold"), validate="key", validatecommand=vcmd)
        employeeSurname_entry.place(relx=0.44, rely=0.0487, relwidth=0.18, relheight=0.04)
        employeeSurname_entry.bind("<KeyRelease>", lambda event: capitalize_first_letter(event, employeeSurname_entry))

        employeePatronymic_label = Label(employeeAdding_panel, text='Patronymic:', fg='white', bg='#141f2b',
                                         font=("Charlesworth", 13, "bold"))
        employeePatronymic_label.place(relx=0.67, rely=0.05)
        employeePatronymic_entry = Entry(employeeAdding_panel, font=("Charlesworth", 13, "bold"), validate="key", validatecommand=vcmd)
        employeePatronymic_entry.place(relx=0.78, rely=0.0487, relwidth=0.18, relheight=0.04)
        employeePatronymic_entry.bind("<KeyRelease>",
                                      lambda event: capitalize_first_letter(event, employeePatronymic_entry))

        birthDate_label = Label(employeeAdding_panel, text='Birth date:', fg='white', bg='#141f2b',
                                font=("Charlesworth", 13, "bold"))
        birthDate_label.place(relx=0.08, rely=0.18)

        def update_days(*args):
            month = comboMonths.get()
            year = int(comboYears.get()) if comboYears.get() else 0
            days_in_month = {
                'January': 31,
                'February': 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28,
                'March': 31,
                'April': 30,
                'May': 31,
                'June': 30,
                'July': 31,
                'August': 31,
                'September': 30,
                'October': 31,
                'November': 30,
                'December': 31
            }
            days = days_in_month.get(month, 31)
            comboDays['values'] = [str(i) for i in range(1, days + 1)]
            if comboint_days.get() > days:
                comboint_days.set(days)

        comboint_days = IntVar()
        comboDays = ttk.Combobox(employeeAdding_panel, values=[str(i) for i in range(1, 32)],
                                 textvariable=comboint_days, font=("Charlesworth", 13, "bold"),
                                 state='readonly')
        comboDays.place(relx=0.18, rely=0.18, relwidth=0.08)

        day_label = Label(employeeAdding_panel, text='days', fg='white', bg='#141f2b',
                          font=("Charlesworth", 12, "italic"))
        day_label.place(relx=0.20, rely=0.13)

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October',
                  'November', 'December']
        combostring_months = StringVar()
        comboMonths = ttk.Combobox(employeeAdding_panel, values=months, textvariable=combostring_months,
                                   font=("Charlesworth", 13, "bold"), state='readonly')
        comboMonths.set('months')
        comboMonths.place(relx=0.28, rely=0.18, relwidth=0.13)
        comboMonths.bind("<<ComboboxSelected>>", update_days)
        months_label = Label(employeeAdding_panel, text='months', fg='white', bg='#141f2b',
                             font=("Charlesworth", 12, "italic"))
        months_label.place(relx=0.32, rely=0.13)

        comboint_years = IntVar()
        comboYears = ttk.Combobox(employeeAdding_panel, values=[str(i) for i in range(1959, 2006)],
                                  textvariable=comboint_years, font=("Charlesworth", 13, "bold"), state='readonly')
        comboYears.set('years')
        comboYears.place(relx=0.43, rely=0.18, relwidth=0.092)
        comboYears.bind("<<ComboboxSelected>>", update_days)
        years_label = Label(employeeAdding_panel, text='years', fg='white', bg='#141f2b',
                            font=("Charlesworth", 12, "italic"))
        years_label.place(relx=0.45, rely=0.13)

        label_gender = Label(employeeAdding_panel, text='Gender:', bg='#141f2b', fg='white',
                             font=("Charlesworth", 13, "bold"))
        label_gender.place(relx=0.6, rely=0.18)
        gender_var = StringVar()
        rbtn_male = Radiobutton(employeeAdding_panel, text='Male', variable=gender_var, value='male',
                                bg='#141f2b', fg='deepskyblue', font=("Charlesworth", 13, "bold"))
        rbtn_male.place(relx=0.7, rely=0.178)
        rbtn_female = Radiobutton(employeeAdding_panel, text='Female', variable=gender_var, value='female',
                                  bg='#141f2b', fg='deepskyblue', font=("Charlesworth", 13, "bold"))
        rbtn_female.place(relx=0.8, rely=0.178)

        position_label = Label(employeeAdding_panel, text='Selected position:', fg='white', bg='#141f2b',
                               font=("Charlesworth", 13, "bold"))
        position_label.place(relx=0.08, rely=0.31)
        from variables import positions

        combostring_positions = StringVar()
        comboPositions = ttk.Combobox(employeeAdding_panel, values=positions, textvariable=combostring_positions,
                                      font=("Charlesworth", 13, "bold"), state='readonly')
        comboPositions.place(relx=0.24, rely=0.31, relwidth=0.32)

        experience_label = Label(employeeAdding_panel, text='Work experience:', fg='white', bg='#141f2b',
                                 font=("Charlesworth", 13, "bold"))
        experience_label.place(relx=0.60, rely=0.31)
        experience = ['None', '< 1 years', '1-3 years', '> 3 years']
        combostring_experience = StringVar()
        comboExperience = ttk.Combobox(employeeAdding_panel, values=experience, textvariable=combostring_experience,
                                       font=("Charlesworth", 13, "bold"), state='readonly')
        comboExperience.place(relx=0.76, rely=0.31, relwidth=0.13)

        city_label = Label(employeeAdding_panel, text='City:', fg='white', bg='#141f2b',
                           font=("Charlesworth", 13, "bold"))
        city_label.place(relx=0.08, rely=0.43)

        from variables import city
        city_sorted = sorted(city)

        combostring_city = StringVar()
        comboCities = ttk.Combobox(employeeAdding_panel, values=city_sorted, textvariable=combostring_city,
                                   font=("Charlesworth", 13, "bold"), state='readonly')
        comboCities.place(relx=0.15, rely=0.43, relwidth=0.15)

        address_label = Label(employeeAdding_panel, text='Address:', fg='white', bg='#141f2b',
                              font=("Charlesworth", 13, "bold"))
        address_label.place(relx=0.32, rely=0.43)
        address_entry = Entry(employeeAdding_panel, font=("Charlesworth", 13, "bold"))
        address_entry.place(relx=0.41, rely=0.43, relwidth=0.58, relheight=0.04)

        about_label = Label(employeeAdding_panel, text='About:', fg='white', bg='#141f2b',
                            font=("Charlesworth", 13, "bold"))
        about_label.place(relx=0.08, rely=0.51)

        def check_word_limit(event):
            content = text_about.get("1.0", END).strip()
            words = content.split()

            word_count = len(words)
            if word_count > 100:
                truncated_content = ' '.join(words[:100])
                text_about.delete("1.0", END)
                text_about.insert(END, truncated_content)

            elif word_count < 10:
                text_about.config(bg="lightyellow")
            else:
                text_about.config(bg="white")  # Reset background when valid

        text_about = Text(employeeAdding_panel)
        text_about.place(relx=0.16, rely=0.51, relwidth=0.83, relheight=0.35)

        text_about.bind("<KeyRelease>", check_word_limit)

        submitEmployee_button = Button(employeeAdding_panel, text='Submit', bg='black', fg='white',
                                       font=("Charlesworth", 14, "bold"), command=lambda: submitEmployee())
        submitEmployee_button.place(relx=0.5, rely=0.9, relheight=0.07, relwidth=0.15)

        def submitEmployee():
            name = employeeName_entry.get()
            surname = employeeSurname_entry.get()
            patronymic = employeePatronymic_entry.get()
            birth_day = comboDays.get()
            birth_month = comboMonths.get()
            birth_year = comboYears.get()
            gender = gender_var.get()
            position = combostring_positions.get()
            experience = combostring_experience.get()
            city = combostring_city.get()
            address = address_entry.get()
            about = text_about.get("1.0", "end-1c")

            # Validation checks
            if len(name) < 3:
                messagebox.showerror("Error", "Name must be more than 3 characters.")
                return

            if len(surname) < 3:
                messagebox.showerror("Error", "Surname must be more than 3 characters.")
                return

            if len(patronymic) < 3:
                messagebox.showerror("Error", "Patronymic must be more than 3 characters.")
                return

            if not birth_day or not birth_month or not birth_year:
                messagebox.showerror("Error", "Please select a complete birth date.")
                return

            if not gender:
                messagebox.showerror("Error", "Please select a gender.")
                return

            if not position:
                messagebox.showerror("Error", "Please select a position.")
                return

            if not experience:
                messagebox.showerror("Error", "Please select your work experience.")
                return

            if not city:
                messagebox.showerror("Error", "Please select a city.")
                return

            if not address:
                messagebox.showerror("Error", "Address cannot be empty.")
                return

            if not about:
                messagebox.showerror("Error", "About field cannot be empty.")
                return
            word_count = len(about.split())
            if word_count < 10:
                messagebox.showerror("Error", "The 'About' section must contain at least 20 words.")
                return

            # Check for duplicate employees
            for emp_id, emp_info in allWorker.items():
                if (emp_info['name'] == name and emp_info['surname'] == surname and
                        emp_info['patronymic'] == patronymic and emp_info['position'] == position):
                    messagebox.showerror("Error", f"{name} {surname} {patronymic} is already registered.")
                    return

            # Compute age
            current_year = datetime.now().year
            age = current_year - int(birth_year)

            # Find the next available employee ID
            global employee_id_counter
            while employee_id_counter in allWorker:
                employee_id_counter += 1

            # Add employee to the allWorker dictionary
            allWorker[employee_id_counter] = {
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'birthDate': [int(birth_day), birth_month, int(birth_year)],
                'age': age,
                'gender': gender,
                'position': position,
                'experience': experience,
                'city': city,
                'address': address,
                'about': about
            }

            messagebox.showinfo("Success", f"Employee {name} added successfully.")

            # Reset fields after successful submission
            employeeName_entry.delete(0, END)
            employeeSurname_entry.delete(0, END)
            employeePatronymic_entry.delete(0, END)
            comboDays.set('')  # or the default day
            comboMonths.set('')  # or the default month
            comboYears.set('')  # or the default year
            gender_var.set('')  # Clear gender selection
            combostring_positions.set('')  # Clear position selection
            combostring_experience.set('')  # Clear experience selection
            combostring_city.set('')  # Clear city selection
            address_entry.delete(0, END)
            text_about.delete('1.0', END)


    editWorkerInfo_button = Button(admin_panel_settings, text='Edit worker info', bg='black', fg='white',
                                   font=("Charlesworth", 14, "bold"), command=lambda: editEmployeeInfo())
    editWorkerInfo_button.place(relx=0.01, rely=0.25, relheight=0.08, relwidth=0.23)

    def editEmployeeInfo():
        global editEmployeeInfo_panel
        global combostring_edit_positions, combostring_experience_edit, combostring_edit_city, address_edit
        global employee_id

        def capitalize_first_letter(event):
            value = event.widget.get()
            if value:
                value = value.title()  # Capitalize first letter of each word
                event.widget.delete(0, END)
                event.widget.insert(0, value)

        clear_frames()
        editEmployeeInfo_panel = Frame(window, bg='#141f2b')
        editEmployeeInfo_panel.pack(expand=True, fill=BOTH)

        # UI elements
        back_button = Button(editEmployeeInfo_panel, image=backPhotoLogin, bd=0, bg='#141f2b',
                             command=lambda: confirmBack())
        back_button.place(relx=0.002, rely=0.01, relheight=0.09, relwidth=0.07)

        infoMessage_label = Label(editEmployeeInfo_panel, text='Please enter name, surname, and father name to edit:',
                                  fg='white', bg='#141f2b',
                                  font=("Charlesworth", 14, "bold"))
        infoMessage_label.place(relx=0.28, rely=0.05)

        def validate_letters(char):
            return char.isalpha() or char == ''

        vcmd = (window.register(validate_letters), '%S')

        name_edit_label = Label(editEmployeeInfo_panel, text='Name:', fg='white', bg='#141f2b',
                                font=("Charlesworth", 13, "bold"))
        name_edit_label.place(relx=0.08, rely=0.15)
        name_edit_entry = Entry(editEmployeeInfo_panel, font=("Charlesworth", 13, "bold"), validate="key", validatecommand=vcmd)
        name_edit_entry.place(relx=0.14, rely=0.1487, relwidth=0.16, relheight=0.04)
        name_edit_entry.bind("<KeyRelease>", capitalize_first_letter)

        surname_edit_label = Label(editEmployeeInfo_panel, text='Surname:', fg='white', bg='#141f2b',
                                   font=("Charlesworth", 13, "bold"))
        surname_edit_label.place(relx=0.35, rely=0.15)
        surname_edit_entry = Entry(editEmployeeInfo_panel, font=("Charlesworth", 13, "bold"), validate="key", validatecommand=vcmd)
        surname_edit_entry.place(relx=0.44, rely=0.1487, relwidth=0.18, relheight=0.04)
        surname_edit_entry.bind("<KeyRelease>", capitalize_first_letter)

        fname_edit_label = Label(editEmployeeInfo_panel, text='Patronymic:', fg='white', bg='#141f2b',
                                 font=("Charlesworth", 13, "bold"))
        fname_edit_label.place(relx=0.67, rely=0.15)
        fname_edit_entry = Entry(editEmployeeInfo_panel, font=("Charlesworth", 13, "bold"), validate="key", validatecommand=vcmd)
        fname_edit_entry.place(relx=0.78, rely=0.1487, relwidth=0.18, relheight=0.04)
        fname_edit_entry.bind("<KeyRelease>", capitalize_first_letter)

        submitEmployeeInfo_button = Button(editEmployeeInfo_panel, text='Check', bg='black', fg='white',
                                           font=("Charlesworth", 14, "bold"), command=lambda: checkEmployeeInfo())
        submitEmployeeInfo_button.place(relx=0.4, rely=0.24, relheight=0.06, relwidth=0.12)

        # Initialize image labels
        global edit, employee
        edit = PhotoImage(file='images/edit.png')
        imageLabel = Label(editEmployeeInfo_panel, image=edit, bd=0, bg='#141f2b')
        imageLabel.place(relx=0.0, rely=0.8, relwidth=0.2, relheight=0.2)

        employee = PhotoImage(file='images/employee.png')
        imageLabel = Label(editEmployeeInfo_panel, image=employee, bd=0, bg='#141f2b')
        imageLabel.place(relx=0.78, rely=0.8, relwidth=0.2, relheight=0.2)

        def checkEmployeeInfo():
            global employee_id
            name = name_edit_entry.get().strip()
            surname = surname_edit_entry.get().strip()
            patronymic = fname_edit_entry.get().strip()

            employee_id = None
            for emp_id, emp_data in allWorker.items():
                if (emp_data['name'], emp_data['surname'], emp_data['patronymic']) == (name, surname, patronymic):
                    employee_id = emp_id
                    break

            if employee_id:
                show_edit_fields()
            else:
                messagebox.showerror("Error", "Employee does not exist")

        def show_edit_fields():
            global combostring_edit_positions, combostring_experience_edit, combostring_edit_city, address_edit

            infoMessage2_label = Label(editEmployeeInfo_panel, text='Below you can edit employee info:',
                                       fg='white', bg='#141f2b',
                                       font=("Charlesworth", 14, "bold"))
            infoMessage2_label.place(relx=0.28, rely=0.35)

            position_edit_label = Label(editEmployeeInfo_panel, text='Selected position:', fg='white', bg='#141f2b',
                                        font=("Charlesworth", 13, "bold"))
            position_edit_label.place(relx=0.08, rely=0.45)
            from variables import positions

            combostring_edit_positions = StringVar()
            comboPositions_edit = ttk.Combobox(editEmployeeInfo_panel, values=positions,
                                               textvariable=combostring_edit_positions,
                                               font=("Charlesworth", 13, "bold"), state='readonly')
            comboPositions_edit.place(relx=0.24, rely=0.45, relwidth=0.32)

            experience_edit_label = Label(editEmployeeInfo_panel, text='Work experience:', fg='white', bg='#141f2b',
                                          font=("Charlesworth", 13, "bold"))
            experience_edit_label.place(relx=0.60, rely=0.45)
            experience_edit = ['None', '< 1 years', '1-3 years', '> 3 years']
            combostring_experience_edit = StringVar()
            comboExperience_Edit = ttk.Combobox(editEmployeeInfo_panel, values=experience_edit,
                                                textvariable=combostring_experience_edit,
                                                font=("Charlesworth", 13, "bold"), state='readonly')
            comboExperience_Edit.place(relx=0.76, rely=0.45, relwidth=0.13)

            cityEdit_label = Label(editEmployeeInfo_panel, text='City:', fg='white', bg='#141f2b',
                                   font=("Charlesworth", 13, "bold"))
            cityEdit_label.place(relx=0.08, rely=0.55)

            from variables import cityEdit
            cityEdit.sort()  # Sort cities alphabetically
            combostring_edit_city = StringVar()
            comboCity_edit = ttk.Combobox(editEmployeeInfo_panel, values=cityEdit,
                                          textvariable=combostring_edit_city,
                                          font=("Charlesworth", 13, "bold"), state='readonly')
            comboCity_edit.place(relx=0.14, rely=0.55, relwidth=0.28)

            address_edit_label = Label(editEmployeeInfo_panel, text='Address:', fg='white', bg='#141f2b',
                                       font=("Charlesworth", 13, "bold"))
            address_edit_label.place(relx=0.60, rely=0.55)
            address_edit = Entry(editEmployeeInfo_panel, font=("Charlesworth", 13, "bold"))
            address_edit.place(relx=0.76, rely=0.55, relwidth=0.18, relheight=0.04)

            update_button = Button(editEmployeeInfo_panel, text='Update', bg='black', fg='white',
                                   font=("Charlesworth", 14, "bold"), command=confirmUpdate)
            update_button.place(relx=0.4, rely=0.7, relheight=0.06, relwidth=0.12)

        def confirmUpdate():
            answer = messagebox.askyesno("Confirmation", "Are you sure you want to change data?")
            if answer:
                updateEmployee()

        def confirmBack():
            answer = messagebox.askyesno("Confirmation", "Are you sure you want to go back?")
            if answer:
                goToAdminPage()

        def updateEmployee():
            global allWorker
            if employee_id:
                allWorker[employee_id]['position'] = combostring_edit_positions.get()
                allWorker[employee_id]['experience'] = combostring_experience_edit.get()
                allWorker[employee_id]['city'] = combostring_edit_city.get()
                allWorker[employee_id]['address'] = address_edit.get()

                # Save the updated worker data to JSON file
                save_worker_data(file_name='allWorker.json', allWorker=allWorker)

                # Clear fields after update
                name_edit_entry.delete(0, END)
                surname_edit_entry.delete(0, END)
                fname_edit_entry.delete(0, END)
                combostring_edit_positions.set('')
                combostring_experience_edit.set('')
                combostring_edit_city.set('')
                address_edit.delete(0, END)

                messagebox.showinfo("Success", "Employee information updated successfully")
            else:
                messagebox.showerror("Error", "No employee selected for update")

        return editEmployeeInfo_panel

    deleteWorker_button = Button(admin_panel_settings, text='Delete worker', bg='black', fg='white',
                                 font=("Charlesworth", 14, "bold"), command=lambda: deleteWorker())
    deleteWorker_button.place(relx=0.01, rely=0.36, relheight=0.08, relwidth=0.23)

    def deleteWorker():
        clear_frames()  # Assuming you have a clear_frames() function to clear the window
        global deleteEmployee_panel
        deleteEmployee_panel = Frame(window, bg='#141f2b')
        deleteEmployee_panel.pack(expand=True, fill=BOTH)

        def confirm_back():
            if messagebox.askyesno("Confirmation", "Are you sure you want to go back?"):
                goToAdminPage()

        back_button = Button(deleteEmployee_panel, image=backPhotoLogin, bd=0, bg='#141f2b',
                             command=confirm_back)
        back_button.place(relx=0.002, rely=0.01, relheight=0.09, relwidth=0.07)

        global lossworker
        lossworker = PhotoImage(file='images/loss.png')
        imageLabel = Label(deleteEmployee_panel, image=lossworker, bd=0, bg='#141f2b')
        imageLabel.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.4)

        employeeLose_label = Label(deleteEmployee_panel,
                                   text='When a good employee walks out the door, they take their loyalty, expertise, and commitment with them.',
                                   fg='white', bg='#141f2b',
                                   font=("Charlesworth", 14, "bold"))
        employeeLose_label.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)

        infoMessageDelete_label = Label(deleteEmployee_panel,
                                        text='Please enter name, surname and patronymic to delete:',
                                        fg='white', bg='#141f2b',
                                        font=("Charlesworth", 14, "bold"))
        infoMessageDelete_label.place(relx=0.28, rely=0.05)

        def capitalize_first_letter(event):
            value = event.widget.get()
            if value:
                value = value.capitalize()  # Capitalize only the first letter
                event.widget.delete(0, END)
                event.widget.insert(0, value)

        def validate_letters(char):
            return char.isalpha() or char == ''

        vcmd = (window.register(validate_letters), '%S')

        # Name input
        name_delete_label = Label(deleteEmployee_panel, text='Name:', fg='white', bg='#141f2b',
                                  font=("Charlesworth", 13, "bold"))
        name_delete_label.place(relx=0.08, rely=0.15)
        name_delete_entry = Entry(deleteEmployee_panel, font=("Charlesworth", 13, "bold"), validate="key",
                                  validatecommand=vcmd)
        name_delete_entry.place(relx=0.14, rely=0.1487, relwidth=0.16, relheight=0.04)
        name_delete_entry.bind("<KeyRelease>", capitalize_first_letter)

        # Surname input
        surname_delete_label = Label(deleteEmployee_panel, text='Surname:', fg='white', bg='#141f2b',
                                     font=("Charlesworth", 13, "bold"))
        surname_delete_label.place(relx=0.35, rely=0.15)
        surname_delete_entry = Entry(deleteEmployee_panel, font=("Charlesworth", 13, "bold"), validate="key",
                                     validatecommand=vcmd)
        surname_delete_entry.place(relx=0.44, rely=0.1487, relwidth=0.18, relheight=0.04)
        surname_delete_entry.bind("<KeyRelease>", capitalize_first_letter)

        # Patronymic input
        fname_delete_label = Label(deleteEmployee_panel, text='Patronymic:', fg='white', bg='#141f2b',
                                   font=("Charlesworth", 13, "bold"))
        fname_delete_label.place(relx=0.67, rely=0.15)
        fname_delete_entry = Entry(deleteEmployee_panel, font=("Charlesworth", 13, "bold"), validate="key",
                                   validatecommand=vcmd)
        fname_delete_entry.place(relx=0.78, rely=0.1487, relwidth=0.18, relheight=0.04)
        fname_delete_entry.bind("<KeyRelease>", capitalize_first_letter)

        # Delete button
        employeeDelete_button = Button(deleteEmployee_panel, text='Delete', bg='black', fg='white',
                                       font=("Charlesworth", 14, "bold"), command=lambda: deleteEmployeeInfo())
        employeeDelete_button.place(relx=0.4, rely=0.24, relheight=0.06, relwidth=0.12)

        def deleteEmployeeInfo():
            name = name_delete_entry.get().strip()
            surname = surname_delete_entry.get().strip()
            patronymic = fname_delete_entry.get().strip()

            # Check if the employee exists in the allWorker dictionary
            employee_found = None
            for employee_id, info in allWorker.items():
                if info['name'] == name and info['surname'] == surname and info['patronymic'] == patronymic:
                    employee_found = employee_id
                    break

            if employee_found:
                # Ask for confirmation to delete the employee
                confirm = messagebox.askyesno("Confirmation",
                                              f"Are you sure you want to delete {name} {surname} {patronymic} from the system?")

                if confirm:
                    # Delete the employee from allWorker
                    del allWorker[employee_found]
                    messagebox.showinfo("Deleted", f"{name} {surname} {patronymic} has been deleted from the system.")
                    # Clear the input fields after deletion
                    name_delete_entry.delete(0, 'end')
                    surname_delete_entry.delete(0, 'end')
                    fname_delete_entry.delete(0, 'end')
                else:
                    # Stay on the page if the user cancels the deletion
                    messagebox.showinfo("Cancelled", "Employee deletion cancelled.")
            else:
                # Employee does not exist, show an error message
                messagebox.showerror("Error", f"{name} {surname} {patronymic} is not in our database.")
            save_worker_data(file_name='allWorker.json', allWorker=allWorker)

    listAllWorkers_button = Button(admin_panel_settings, text='List of all employees', bg='black', fg='white',
                                   font=("Charlesworth", 14, "bold"), command=lambda: allEmployees())
    listAllWorkers_button.place(relx=0.01, rely=0.47, relheight=0.08, relwidth=0.23)

    def allEmployees():
        clear_frames()
        global allEmployees_panel
        allEmployees_panel = Frame(window, bg='#141f2b')
        allEmployees_panel.pack(expand=True, fill=BOTH)

        def on_back_button_click():
            if messagebox.askyesno("Confirm", "Are you sure you want to go back to the admin page?"):
                goToAdminPage()

        back_button = Button(allEmployees_panel, image=backPhotoLogin, bd=0, bg='#141f2b',
                             command=on_back_button_click)
        back_button.place(relx=0.002, rely=0.01, relheight=0.09, relwidth=0.07)

        ourEmployees_label = Label(allEmployees_panel, text='Our employees:',
                                   fg='white', bg='#141f2b',
                                   font=("Charlesworth", 14, "bold"))
        ourEmployees_label.place(relx=0.4, rely=0.05)

        global bosslogo
        bosslogo = PhotoImage(file='images/boss.png')
        imageLabel = Label(allEmployees_panel, image=bosslogo, bd=0, bg='#141f2b')
        imageLabel.place(relx=0.8, rely=0.02, relwidth=0.2, relheight=0.22)

        filter_label = Label(allEmployees_panel, text='Filter employees by position:',
                             fg='white', bg='#141f2b',
                             font=("Charlesworth", 14, "bold"))
        filter_label.place(relx=0.02, rely=0.15)

        from variables import positions_filter

        combostring_filter_positions = StringVar()
        comboPositions_filter = ttk.Combobox(allEmployees_panel, values=positions_filter,
                                             textvariable=combostring_filter_positions,
                                             font=("Charlesworth", 13, "bold"), state='readonly')
        comboPositions_filter.place(relx=0.32, rely=0.15, relwidth=0.32)

        # Create a canvas for scrolling
        canvas = Canvas(allEmployees_panel, bg='#141f2b')
        canvas.place(relx=0.02, rely=0.25, relwidth=0.76, relheight=0.65)

        # Create a scrollbar linked to the canvas
        scrollbar = Scrollbar(allEmployees_panel, orient='vertical', command=canvas.yview)
        scrollbar.place(relx=0.78, rely=0.25, relheight=0.65)

        # Create a frame inside the canvas for the employee labels
        global employees_frame
        employees_frame = Frame(canvas, bg='#141f2b')

        # Create a window in the canvas to contain the employees_frame
        canvas.create_window((0, 0), window=employees_frame, anchor='nw')

        # Configure scrollbar and canvas
        employees_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.config(command=canvas.yview)

        def display_employees(position_filter=None):
            # Clear previous employee labels
            for widget in employees_frame.winfo_children():
                if isinstance(widget, Label):
                    widget.destroy()

            # Display employees
            y_position = 0  # Starting vertical position for the first employee
            employees_found = False

            for employee_id, employee_data in allWorker.items():
                # Apply filter if specified
                if position_filter and employee_data['position'] != position_filter:
                    continue

                name = employee_data['name']
                surname = employee_data['surname']
                patronymic = employee_data['patronymic']
                position = employee_data['position']
                experience = employee_data['experience']

                # Format employee display text
                display_text = f"{name} {surname} {patronymic} --- {position} ({experience})"

                employee_label = Label(employees_frame, text=display_text,
                                       fg='white', bg='#141f2b', font=("Charlesworth", 18))
                employee_label.pack(anchor='w', pady=2)  # Use pack for better scrolling integration
                employees_found = True

            # Show no employees found message if none found
            if not employees_found:
                no_employees_label = Label(employees_frame,
                                           text="We don't have any employees found for the selected position",
                                           fg='white', bg='#141f2b', font=("Charlesworth", 16, "italic"))
                no_employees_label.pack(anchor='w', pady=10)

        def filter_employees_by_position(event):
            position_filter = combostring_filter_positions.get()
            display_employees(position_filter)

        # Bind the combobox selection to the filter function
        comboPositions_filter.bind('<<ComboboxSelected>>', filter_employees_by_position)

        # Display all employees initially
        display_employees()

    global settings
    settings = PhotoImage(file='images/settings.png')
    imageLabel = Label(admin_panel_settings, image=settings, bd=0, bg='#81a3a0')
    imageLabel.place(relx=0.0, rely=0.56, relwidth=0.28, relheight=0.45)

    def on_back_button_click():
        response = messagebox.askyesno("Confirm", "Are you sure you want to go back to the login panel?")
        if response:
            goToLoginPage()

    back_button = Button(admin_panel_page, image=backPhotoLogin, bd=0, bg='#141f2b',
                         command=on_back_button_click)
    back_button.place(relx=0.9, rely=0.9, relheight=0.09, relwidth=0.07)

    global employeesAdmin
    employeesAdmin = PhotoImage(file='images/employees.png')
    back_button = Label(admin_panel_page, image=employeesAdmin, bd=0, bg='#141f2b')
    back_button.place(relx=0.29, rely=0.1, relheight=0.7, relwidth=0.7)


def goToLoginPage():
    clear_frames()
    login()


def goToAdminPage():
    clear_frames()
    adminPanel()


def goToMainPage():
    clear_frames()  # Clear any other frames before showing the main window elements

    # Reload the main window background image and label
    global imageLabel, mainpage
    if imageLabel:
        imageLabel.destroy()  # Remove the background image from previous frames
    mainpage = PhotoImage(file='images/mainpg.gif')  # Reload the main page background image
    imageLabel = Label(window, image=mainpage)
    imageLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Bring back the main window elements on top of the background image
    label_main_page.lift()
    btnLogin.lift()

window.mainloop()

for employee_id, values in allWorker.items():
    print(f"Employee {employee_id}:")
    print(f"Name       : {values['name']}")
    print(f"Surname    : {values['surname']}")
    print(f"Patronymic : {values['patronymic']}")
    print(f"Birth Date : {values['birthDate'][0]} {values['birthDate'][1]} {values['birthDate'][2]}")
    print(f"Age        : {values['age']}")
    print(f"Gender     : {values['gender']}")
    print(f"Position   : {values['position']}")
    print(f"Experience : {values['experience']}")
    print(f"City       : {values['city']}")
    print(f"Address    : {values['address']}")
    print(f"About      : {values['about']}")
    print("----------------------")