import tkinter as tk
import os

class ToolSelect(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        HarvestBtn = tk.Button(self, text="launch Harvester",
                                   command=self.Havest_launcher)
        HarvestBtn.pack(side="top", padx=20, pady=20)

        SherlockBtn = tk.Button(self, text="launch Sherlock",
                               command=self.Sherlock_launcher)
        SherlockBtn.pack(side="top", padx=20, pady=20)

    def Havest_launcher(self):
        top = tk.Toplevel(self)
        label = tk.Label(top, text="Harvester Launching")
        os.system("git clone https://github.com/laramies/theHarvester")
        os.chdir("C:/Users/Owner/PycharmProjects/DataSpike_SPOC/theHarvester")
        os.system("python -m pip install -r requirements/base.txt")
        #os.system("python theHarvester.py -h")
        b = tk.Button(top, text="Destroy me",
                      command=lambda win=top: win.destroy())
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        b.pack(side="bottom")

    def Sherlock_launcher(self):
        top = tk.Toplevel(self)
        top.title("Sherlock")
        top.geometry("400x200")

        def execute_Sherlock():
            input_name = entry1.get()
            entry1.delete(0, 'end')
            varSource = "python3 sherlock " + input_name
            os.chdir("C:/Users/Owner/PycharmProjects/DataSpike_SPOC/sherlock")
            os.system(varSource)

        def execute_csv():
            input_name = entry1.get()
            entry1.delete(0, 'end')
            varSource2 = "python3 sherlock " + input_name + " --print-found --csv"
            os.chdir("C:/Users/Owner/PycharmProjects/DataSpike_SPOC/sherlock")
            os.system(varSource2)

        label = tk.Label(top, text="Sherlock Launcher")
        entry1 = tk.Entry(top)
        entry1.pack()
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        delete_b = tk.Button(top, text="Destroy me",
                      command=lambda win=top: win.destroy())
        delete_b.pack(side="bottom")

        csv = tk.Button(top, text="save to csv",
                      command=execute_csv)
        csv.pack(side="bottom")

        os.system("git clone https://github.com/sherlock-project/sherlock.git")
        os.chdir("C:/Users/Owner/PycharmProjects/DataSpike_SPOC/sherlock")
        os.system("python3 -m pip install -r requirements.txt")
        top.bind('<Return>', execute_Sherlock)




    def get_dir(self):
        tmp = tk.askdirectory(mustexist=1, title="Please select a destination")
        tmp = tmp.replace("/", "\\")

        self.xbPath.delete(0, END)
        self.xbPath.insert(0, tmp)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("DataSpike")
    root.geometry("400x200")
    ToolSelect(root).pack(fill="both", expand=True)
    root.mainloop()