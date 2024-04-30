import sqlite3

class MedicalDatabase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                condition TEXT,
                                treatment TEXT
                            )''')
        self.connection.commit()

    def add_patient(self, name, condition, treatment):
        self.cursor.execute("INSERT INTO patients (name, condition, treatment) VALUES (?, ?, ?)", (name, condition, treatment))
        self.connection.commit()

    def get_patient_data(self, patient_id):
        self.cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
        return self.cursor.fetchone()

# Exemple d'utilisation
db = MedicalDatabase('medical_data.db')
db.add_patient('Alice', 'Hypertension', 'Beta blockers')
db.add_patient('Bob', 'Diabetes', 'Insulin')

# Simuler une requête malveillante
patient_id = 1
data = db.get_patient_data(patient_id)
print("Données du patient avec l'ID", patient_id, ":", data)
