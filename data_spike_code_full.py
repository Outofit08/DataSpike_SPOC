import tkinter as tk
import tkinter.ttk as ttk
import os

class DataSpikeUiApp:
    def __init__(self, master):
        # build ui
        self.main_window = ttk.Frame(master)

        self.username_label = ttk.Label(self.main_window)
        self.username_label.configure(anchor='w', cursor='arrow', justify='left', padding='10')
        self.username_label.configure(takefocus=False, text='Username')
        self.username_label.grid()
        self.user_entry = ttk.Entry(self.main_window)
        self.user_entry.configure(justify='left', validate='key')
        self.user_entry.grid(column='2', pady='20', row='0', sticky='n')
        self.username_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_usernameSearch())
        self.username_button.configure(style='Toolbutton', text='Search')
        self.username_button.grid(column='3', padx='10', row='0')


        self.email_label = ttk.Label(self.main_window)
        self.email_label.configure(justify='left', padding='10', text='Email')
        self.email_label.grid()
        self.email_entry = ttk.Entry(self.main_window)
        self.email_entry.configure(justify='left')
        self.email_entry.grid(column='2', pady='20', row='1')
        self.email_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_h8mail())
        self.email_button.configure(state='normal', style='Toolbutton', text='Search')
        self.email_button.grid(column='3', padx='10', row='1')

        self.phone_label = ttk.Label(self.main_window, class_='phone')
        self.phone_label.configure(justify='left', padding='10', text='Phone Number')
        self.phone_label.grid()
        self.phoneNumber_entry = ttk.Entry(self.main_window)
        self.phoneNumber_entry.configure(justify='left')
        self.phoneNumber_entry.grid(column='2', pady='20', row='2')
        self.phone_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_phone())
        self.phone_button.configure(state='normal', style='Toolbutton', text='Search')
        self.phone_button.grid(column='3', padx='10', pady='10', row='2')

        self.ip_label = ttk.Label(self.main_window, class_='ipAddress')
        self.ip_label.configure(font='TkDefaultFont', justify='left', padding='10', takefocus=False)
        self.ip_label.configure(text='IP Address')
        self.ip_label.grid()
        self.ip_entry = ttk.Entry(self.main_window)
        self.ip_entry.configure(justify='left')
        self.ip_entry.grid(column='2', pady='20', row='3')
        self.ip_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_ipSearch())
        self.ip_button.configure(state='normal', style='Toolbutton', text='Search')
        self.ip_button.grid(column='3', padx='10', row='3')

        self.url_label = ttk.Label(self.main_window)
        self.url_label.configure(justify='left', padding='10', takefocus=False, text='URL')
        self.url_label.grid()
        self.url_entry = ttk.Entry(self.main_window)
        self.url_entry.configure(justify='left')
        self.url_entry.delete('0', 'end')
        self.url_entry.grid(column='2', pady='20', row='4')
        self.url_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_url())
        self.url_button.configure(state='normal', style='Toolbutton', text='Search')
        self.url_button.grid(column='3', padx='10', pady='10', row='4')

        self.domain_label = ttk.Label(self.main_window)
        self.domain_label.configure(justify='left', padding='10', text='Domain')
        self.domain_label.grid()
        self.domain_entry = ttk.Entry(self.main_window)
        self.domain_entry.configure(justify='left')
        self.domain_entry.grid(column='2', pady='20', row='5')
        self.domain_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_domain())
        self.domain_button.configure(state='normal', style='Toolbutton', text='Search')
        self.domain_button.grid(column='3', padx='10', row='5')
        self.main_window.configure(borderwidth='5', height='200', padding='10', relief='groove')
        self.main_window.configure(width='200')
        self.main_window.pack(side='top')

        # Main widget
        self.mainwindow = self.main_window




    def run(self):
        self.mainwindow.mainloop()

    def execute_usernameSearch(self):
        input_name = self.user_entry.get()
        self.user_entry.delete(0, 'end')
        varSource = "sherlock --folderoutput SherlockResults --csv " + input_name
        varSource2 = "instaloader target[" +input_name+"]"
        varSource3 = "twint -u " + input_name +" -o twint_results.csv --csv"
        os.system(varSource)
        os.system(varSource2)
        os.system(varSource3)

    def execute_h8mail(self):
        input_name = self.email_entry.get()
        self.email_entry.delete(0, 'end')
        varSource = "h8mail - t " + input_name + " -o h8mail_results.csv"
        print(varSource)
        os.system(varSource)

    def execute_phone(self):
        input_name = self.phoneNumber_entry.get()
        self.phoneNumber_entry.delete(0, 'end')
        varSource = "phoneinfoga scan -n " + input_name
        print(varSource)
        os.system(varSource)

    def execute_ipSearch(self):
        input_name = self.ip_entry.get()
        self.ip_entry.delete(0, 'end')
        varSource = input_name
        print(varSource)
        os.system(varSource)

    def execute_url(self):
        input_name = self.url_entry.get()
        self.url_entry.delete(0, 'end')
        varSource = "finalrecon --whois " + input_name + " -o csv"
        print(varSource)
        os.system(varSource)

    def execute_domain(self):
        input_name = self.domain_entry.get()
        self.domain_entry.delete(0, 'end')
        varSource = "theHarvester -d " + input_name + " -l 500 -b all -output $domain_results"
        print(varSource)
        os.system(varSource)

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title("DataSpike")
    app = DataSpikeUiApp(root)
    app.run()

