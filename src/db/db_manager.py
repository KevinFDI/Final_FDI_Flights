import csv
from src.models.dietary_restrictions import DietaryRestrictions


def load_data_restrictions():
    data = []
    with open(r'C:\Users\khtat\PycharmProjects\kevin_harnan_fdi_final_21_07_2022\src\db\dietary_restrictions.csv', 'r') as file:
        # Accede a una posición donde se encuentra el archivo y va agregando bloques de datos de código.
        rows = csv.DictReader(file)

        for row in rows:
            data.append(
                DietaryRestrictions(
                    row['id'],
                    row['restriction']
                )
            )

        return data

def save_dietary_restriction(data_dietary):
    with open(r'C:/Users/khtat/PycharmProjects/kevin_harnan_fdi_final_21_07_2022\src\db\dietary_restrictions_ids.csv', 'a') as file:
    # El renglón de arriba le delega la responsabilidad a Python de hacer cosas de manera responsable.
        header = ['user_id', 'flight_id', 'dietary_restriction_ids']
        writer = csv.DictWriter(file, fieldnames=header)

        if file.tell() == 0:
            # Función que sirve para que si existe una línea en el csv (los headers) no los vuelva a escribir.
            writer.writeheader()

        writer.writerow(data_dietary)