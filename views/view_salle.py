import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle


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

    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            int(self.entry_capacite.get())
        )

        ok, message = self.service_salle.ajouter_salle(salle)
        print(message)

    def modifier_salle(self):
        pass

    def supprimer_salle(self):
        pass

    def rechercher_salle(self):
        pass
