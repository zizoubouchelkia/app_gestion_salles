import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
from tkinter import ttk


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()
        self.cadreInfo = ctk.CTkFrame(self)
        self.cadreInfo.pack(pady=10)

        self.entry_code = ctk.CTkEntry(self.cadreInfo, placeholder_text="Code")
        self.entry_code.pack(pady=5)

        self.entry_libelle = ctk.CTkEntry(self.cadreInfo, placeholder_text="Libelle")
        self.entry_libelle.pack(pady=5)

        self.entry_type = ctk.CTkEntry(self.cadreInfo, placeholder_text="Type")
        self.entry_type.pack(pady=5)

        self.entry_capacite = ctk.CTkEntry(self.cadreInfo, placeholder_text="Capacite")
        self.entry_capacite.pack(pady=5)

        self.cadreActions = ctk.CTkFrame(self)
        self.cadreActions.pack(pady=10)

        ctk.CTkButton(self.cadreActions, text="Ajouter", command=self.ajouter_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.cadreActions, text="Modifier", command=self.modifier_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.cadreActions, text="Supprimer", command=self.supprimer_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.cadreActions, text="Rechercher", command=self.rechercher_salle).pack(side="left", padx=5)

        self.tree = ttk.Treeview(self, columns=("code", "libelle", "type", "capacite"), show="headings")

        self.tree.heading("code", text="CODE")
        self.tree.heading("libelle", text="LIBELLE")
        self.tree.heading("type", text="TYPE")
        self.tree.heading("capacite", text="CAPACITE")

        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.column("code", width=100)
        self.tree.column("libelle", width=200)
        self.tree.column("type", width=150)
        self.tree.column("capacite", width=100)

        self.lister_salles()

    def lister_salles(self):
        self.tree.delete(*self.tree.get_children())

        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.tree.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))

    def ajouter_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_libelle.get(),
                self.entry_type.get(),
                int(self.entry_capacite.get())
            )

            ok, message = self.service_salle.ajouter_salle(salle)
            print(message)

            if ok:
                self.lister_salles()
                self.vider_champs()
        except ValueError:
            print("La capacité doit être un nombre")

    def modifier_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_libelle.get(),
                self.entry_type.get(),
                int(self.entry_capacite.get())
            )

            ok, message = self.service_salle.modifier_salle(salle)
            print(message)

            if ok:
                self.lister_salles()
                self.vider_champs()
        except ValueError:
            print("La capacité doit être un nombre")

    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service_salle.supprimer_salle(code)
        print("Salle supprimée")
        self.lister_salles()

    def rechercher_salle(self):
        code = self.entry_code.get()
        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_libelle.delete(0, "end")
            self.entry_libelle.insert(0, salle.libelle)

            self.entry_type.delete(0, "end")
            self.entry_type.insert(0, salle.type)

            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, str(salle.capacite))
        else:
            print("Salle non trouvée")

    def vider_champs(self):
        self.entry_code.delete(0, "end")
        self.entry_libelle.delete(0, "end")
        self.entry_type.delete(0, "end")
        self.entry_capacite.delete(0, "end")
