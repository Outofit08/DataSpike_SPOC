import tkinter as tk
import tkinter.ttk as ttk
import os

class DataSpikeUiApp:
    def __init__(self, master):
        # build ui
        self.main_window = ttk.Frame(master)

        self.sherlock_label = ttk.Label(self.main_window)
        self.sherlock_label.configure(anchor='w', cursor='arrow', justify='left', padding='10')
        self.sherlock_label.configure(takefocus=False, text='Username')
        self.sherlock_label.grid()
        self.sherlock_entry = ttk.Entry(self.main_window)
        self.sherlock_entry.configure(justify='left', validate='key')
        self.sherlock_entry.grid(column='2', pady='20', row='0', sticky='n')
        self.sherlock_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_sherlockSearch())
        self.sherlock_button.configure(style='Toolbutton', text='Sherlock')
        self.sherlock_button.grid(column='3', padx='10', row='0')

        self.instaloader = ttk.Label(self.main_window)
        self.instaloader.configure(justify='left', padding='10', text='Username')
        self.instaloader.grid(column='0', row='1')
        self.insta_entry = ttk.Entry(self.main_window)
        self.insta_entry.grid(column='2', row='1')
        self.insta_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_instaSearch())
        self.insta_button.configure(style='Toolbutton', text='Instaloader')
        self.insta_button.grid(column='3', padx='10', pady='10', row='1')

        self.twint = ttk.Label(self.main_window)
        self.twint.configure(justify='left', padding='10', text='Username')
        self.twint.grid(column='0', row='2')
        self.twint_entry = ttk.Entry(self.main_window)
        self.twint_entry.configure(justify='left')
        self.twint_entry.grid(column='2', row='2')
        self.twint_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_twintSearch())
        self.twint_button.configure(style='Toolbutton', text='Twint')
        self.twint_button.grid(column='3', padx='10', pady='10', row='2')

        self.email_label = ttk.Label(self.main_window)
        self.email_label.configure(justify='left', padding='10', text='Email')
        self.email_label.grid(row='3')
        self.email_entry = ttk.Entry(self.main_window)
        self.email_entry.configure(justify='left')
        self.email_entry.grid(column='2', pady='20', row='3')
        self.email_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_h8mail())
        self.email_button.configure(state='normal', style='Toolbutton', text='H8mail')
        self.email_button.grid(column='3', padx='10', row='3')

        self.phone_label = ttk.Label(self.main_window, class_='phone')
        self.phone_label.configure(justify='left', padding='10', text='Phone Number (with country code)')
        self.phone_label.grid(row='4')
        self.phoneNumber_entry = ttk.Entry(self.main_window)
        self.phoneNumber_entry.configure(justify='left')
        self.phoneNumber_entry.grid(column='2', pady='20', row='4')
        self.phone_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_phone())
        self.phone_button.configure(state='normal', style='Toolbutton', text='Phoneinfoga')
        self.phone_button.grid(column='3', padx='10', pady='10', row='4')

        self.ip_label = ttk.Label(self.main_window, class_='ipAddress')
        self.ip_label.configure(font='TkDefaultFont', justify='left', padding='10', takefocus=False)
        self.ip_label.configure(text='Username')
        self.ip_label.grid(row='5')
        self.ip_entry = ttk.Entry(self.main_window)
        self.ip_entry.configure(justify='left')
        self.ip_entry.grid(column='2', pady='20', row='5')
        self.ip_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_ipSearch())
        self.ip_button.configure(state='normal', style='Toolbutton', text='Whatsmyname')
        self.ip_button.grid(column='3', padx='10', row='5')

        self.url_label = ttk.Label(self.main_window)
        self.url_label.configure(justify='left', padding='10', takefocus=False, text='URL (http:// or https://)')
        self.url_label.grid(row='6')
        self.url_entry = ttk.Entry(self.main_window)
        self.url_entry.configure(justify='left')
        self.url_entry.delete('0', 'end')
        self.url_entry.grid(column='2', pady='20', row='6')
        self.url_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_url())
        self.url_button.configure(state='normal', style='Toolbutton', text='finalrecon')
        self.url_button.grid(column='3', padx='10', pady='10', row='6')

        self.domain_label = ttk.Label(self.main_window)
        self.domain_label.configure(justify='left', padding='10', text='Domain')
        self.domain_label.grid(row='7')
        self.domain_entry = ttk.Entry(self.main_window)
        self.domain_entry.configure(justify='left')
        self.domain_entry.grid(column='2', pady='20', row='7')
        self.domain_button = ttk.Button(self.main_window, command=lambda
            button=self.main_window: self.execute_domain())
        self.domain_button.configure(state='normal', style='Toolbutton', text='theHarvester')
        self.domain_button.grid(column='3', padx='10', row='7')
        self.main_window.configure(borderwidth='5', height='200', padding='10', relief='groove')
        self.main_window.configure(width='200')
        self.main_window.pack(side='top')

        # Main widget
        self.mainwindow = self.main_window




    def run(self):
        self.mainwindow.mainloop()

    def execute_sherlockSearch(self):
        input_name = self.sherlock_entry.get()
        self.sherlock_entry.delete(0, 'end')
        varSource = "sherlock --csv " + input_name
        os.system(varSource)

    def execute_instaSearch(self):
        input_name = self.insta_entry.get()
        self.insta_entry.delete(0, 'end')
        varSource = "instaloader profile [+input_name]"
        os.system(varSource)

    def execute_twintSearch(self):
        input_name = self.twint_entry.get()
        self.twint_entry.delete(0, 'end')
        varSource = "twint -u " + input_name +" -o twint_results.csv --csv"
        os.system(varSource)

    def execute_h8mail(self):
        input_name = self.email_entry.get()
        self.email_entry.delete(0, 'end')
        varSource = "h8mail -t " + input_name + " -o h8mail_results.csv --loose"
        os.system(varSource)

    def execute_phone(self):
        input_name = self.phoneNumber_entry.get()
        self.phoneNumber_entry.delete(0, 'end')
        varSource = "phoneinfoga scan -n " + input_name
        os.system(varSource)

    def execute_ipSearch(self):
        input_name = self.ip_entry.get()
        self.ip_entry.delete(0, 'end')
        varSource = "whatsmyname -u " + input_name
        os.system(varSource)

    def execute_url(self):
        input_name = self.url_entry.get()
        self.url_entry.delete(0, 'end')
        varSource = "finalrecon --whois " + input_name + " -o csv"
        os.system(varSource)

    def execute_domain(self):
        input_name = self.domain_entry.get()
        self.domain_entry.delete(0, 'end')
        varSource = "theHarvester -d " + input_name + " -l 500 -b all -f harvest_results.html"
        os.system(varSource)

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title("DataSpike")
    app = DataSpikeUiApp(root)
    app.run()

