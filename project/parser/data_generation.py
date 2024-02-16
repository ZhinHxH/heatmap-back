import random
import mysql.connector


def generate_data():
    data = []
    for i in range(100):
        longitude = random.uniform(-77.2, -76.8)  # Coordenadas aproximadas de longitud de Lima
        lat = random.uniform(-12.3, -11.9)  # Coordenadas aproximadas de latitud de Lima
        meter_serial = str(i + 1)  # Convertir a string
        efectivity = random.randint(50, 100)
        data.append((longitude, lat, meter_serial, efectivity))
    return data


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="p1"
)
cursor = connection.cursor()

random_data = generate_data()
cursor.executemany('''
INSERT INTO project_water_meter_ubication (longitude, latitude, meter_serial, efectivity)
VALUES (%s, %s, %s, %s)
''', random_data)

connection.commit()
connection.close()
