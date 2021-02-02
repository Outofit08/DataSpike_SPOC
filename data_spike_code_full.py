import tkinter as tk
import tkinter.ttk as ttk
import os

class DataSpikeUiApp:
    def __init__(self, master=None):
        # build ui
        self.main_window = ttk.Frame(master)

        self.username_label = ttk.Label(self.main_window, class_='username')
        self.username_label.configure(anchor='w', cursor='arrow', justify='left', padding='10')
        self.username_label.configure(takefocus=False, text='Username')
        self.username_label.grid()
        self.user_entry = ttk.Entry(self.main_window, class_='username')
        self.user_entry.configure(justify='left', validate='key')
        self.user_entry.grid(column='2', pady='20', row='0', sticky='n')
        self.username_button = ttk.Button(self.main_window, class_='username')
        self.username_button.configure(style='Toolbutton', takefocus=True, text='Search')
        self.username_button.grid(column='3', padx='10', row='0')

        self.email_label = ttk.Label(self.main_window, class_='email')
        self.email_label.configure(justify='left', padding='10', text='Email')
        self.email_label.grid()
        self.email_entry = ttk.Entry(self.main_window, class_='email')
        self.email_entry.configure(validate='key')
        self.email_entry.grid(column='2', pady='20', row='1')
        self.email_button = ttk.Button(self.main_window, class_='email')
        self.email_button.configure(state='normal', style='Toolbutton', text='Search')
        self.email_button.grid(column='3', padx='10', row='1')

        self.phone_label = ttk.Label(self.main_window, class_='phone')
        self.phone_label.configure(justify='left', padding='10', text='Phone Number')
        self.phone_label.grid()
        self.phoneNumber_entry = ttk.Entry(self.main_window, class_='phone')
        self.phoneNumber_entry.configure(justify='center')
        self.phoneNumber_entry.grid(column='2', pady='20', row='2')
        self.phone_button = ttk.Button(self.main_window, class_='phone')
        self.phone_button.configure(state='normal', style='Toolbutton', text='Search')
        self.phone_button.grid(column='3', padx='10', pady='10', row='2')

        self.ip_label = ttk.Label(self.main_window, class_='ipAddress')
        self.ip_label.configure(font='TkDefaultFont', justify='left', padding='10', takefocus=False)
        self.ip_label.configure(text='IP Address')
        self.ip_label.grid()
        self.ip_entry = ttk.Entry(self.main_window, class_='ipAddress')
        self.ip_entry.configure(exportselection='true', justify='left', takefocus=False)
        self.ip_entry.grid(column='2', pady='20', row='3')
        self.ip_button = ttk.Button(self.main_window, class_='ipAddress')
        self.ip_button.configure(state='normal', style='Toolbutton', text='Search')
        self.ip_button.grid(column='3', padx='10', row='3')

        self.url_label = ttk.Label(self.main_window)
        self.url_label.configure(justify='left', padding='10', takefocus=False, text='URL')
        self.url_label.grid()
        self.url_entry = ttk.Entry(self.main_window)
        self.url_entry.configure(justify='left')
        self.url_entry.delete('0', 'end')
        self.url_entry.grid(column='2', pady='20', row='4')
        self.url_button = ttk.Button(self.main_window, class_='url')
        self.url_button.configure(state='normal', style='Toolbutton', text='Search')
        self.url_button.grid(column='3', padx='10', pady='10', row='4')

        self.domain_label = ttk.Label(self.main_window)
        self.domain_label.configure(justify='left', padding='10', text='Domain')
        self.domain_label.grid()
        self.domain_entry = ttk.Entry(self.main_window, class_='domain')
        self.domain_entry.configure(justify='left')
        self.domain_entry.grid(column='2', pady='20', row='5')
        self.domain_button = ttk.Button(self.main_window, class_='domain')
        self.domain_button.configure(state='normal', style='Toolbutton', text='Search')
        self.domain_button.grid(column='3', padx='10', row='5')

        self.main_window.configure(borderwidth='5', height='200', padding='10', relief='groove')
        self.main_window.configure(width='200')
        self.main_window.pack(side='top')

        # Main widget
        self.mainwindow = self.main_window

    def execute_Sherlock(self, user_entry):
        input_name = user_entry.get()
        user_entry.delete(0, 'end')
        varSource = "python3 sherlock " + input_name
        os.chdir("C:/Users/Owner/PycharmProjects/DataSpike_SPOC/sherlock")
        os.system(varSource)

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = DataSpikeUiApp(root)
    app.run()

