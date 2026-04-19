import json
import mysql.connector
from models.salle import Salle


class DataSalle:

    def get_connection(self):
        with open("Data/config.json", "r") as f:
            config = json.load(f)

        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return connexion

    def insert_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)

        curseur.execute(requete, valeurs)
        connexion.commit()

        curseur.close()
        connexion.close()

    def update_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)

        curseur.execute(requete, valeurs)
        connexion.commit()

        curseur.close()
        connexion.close()