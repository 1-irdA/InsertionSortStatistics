from FileUtils import *
from Stats import *
from tkinter import messagebox
import tkinter as tk

"""
    Tkinter app
"""
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()
        self.results = None
        self.stats = None

    """
        Put widgets
    """
    def create_widgets(self):
        self.geometry('600x600')
        self.resizable(height=None, width=None)
        self.maxsize(width=600, height=600)
        self.iconbitmap('growth.ico')
        self.title("Statistiques tri par insertion")

        # title
        tk.Label(self, 
                text="Statistiques",
                font=('Helvetica', 25)).place(x=220, y=20)

        #  number of tests
        tk.Label(self, 
                text="Nombre de tests",
                font=('Helvetica', 12)).place(x=80, y=100)
        self.entry_tests = tk.Entry(self, width=20)
        self.entry_tests.place(x=250, y=103)

        # arrays size
        tk.Label(self, 
                text="Taille des tableaux\n(0 = aléatoire)",
                font=('Helvetica', 12)).place(x=80, y=150)
        self.entry_size = tk.Entry(self, width=20)
        self.entry_size.place(x=250, y=160)

        # export path
        tk.Label(self, 
                text="Nom du fichier",
                font=('Helvetica', 12)).place(x=85, y=220)
        self.entry_path = tk.Entry(self, width=20)
        self.entry_path.insert(1, 'stats.csv')
        self.entry_path.place(x=250, y=220)

        # button to generate
        tk.Button(self, 
                text="Générer", 
                width=20,
                height=2,
                bg="#60a832",
                fg="white",
                command=lambda: self.generate(self.entry_tests.get(), 
                                            self.entry_size.get())).place(x=60, y=260)

        # button to generate
        tk.Button(self, 
                text="Exporter", 
                width=20,
                height=2,
                bg="#4287f5",
                fg="#fff",
                command=lambda: self.export(self.entry_path.get())).place(x=220, y=260)

        # charts buttons
        tk.Button(self, 
                text="Graphiques", 
                width=20,
                height=2,
                bg="#fc7703",
                fg="#fff",
                command=lambda: self.display_charts()).place(x=380, y=260)

        self.label_results = tk.Label(self, font=22, anchor='n')
        self.label_results.place(y=380, relheight=0.6, relwidth=1)

    """
        Generate stats and charts
    """
    def generate(self, nb_tests, array_size):
        if nb_tests and array_size:
            tests = int(nb_tests)
            size = int(array_size)
            if isinstance(tests, int) and isinstance(size, int):
                self.stats = Stats(tests, size)
                self.stats.init_stats()
                self.stats.make_stats()
                self.results = self.stats.get_all_time()
                self.label_results['text'] = self.stats.informations()
                tk.messagebox.showinfo(title="Génération terminée", message="Génération terminée.")
        else:
            tk.messagebox.showerror(title="Erreur de saisie", message="Saisie invalide.")

    """
        Write file
    """
    def export(self, path):
        if path and self.results:
            file = FileUtils(path, 'a')
            file.write_file(self.results)
            tk.messagebox.showinfo(title="Confirmation", message="Données exportées avec succés !")
        else:
            tk.messagebox.showerror(title="Erreur", message="Impossible d'exporter les données.")

    """
        Display charts
    """
    def display_charts(self):
        if self.stats:
            self.stats.make_charts()
        else:
            tk.messagebox.showerror(title="Erreur", message="Impossible d'afficher les graphiques.")