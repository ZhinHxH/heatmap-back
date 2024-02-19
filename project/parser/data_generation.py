import random
import mysql.connector


def generate_data():
    data = []
    for i in range(200):
        longitude = random.uniform(-76.5707, -76.5044)  # Coordenadas aproximadas de longitud de Lima
        lat = random.uniform(3.3951, 3.4625)  # Coordenadas aproximadas de latitud de Lima
        meter_serial = str(i + 1)  # Convertir a string
        efectivity = random.randint(50, 100)
        data.append((longitude, lat, meter_serial, efectivity))
    return data


connection = mysql.connector.connect(
    host="viewshine-heatmap-database.cuureygem86m.us-east-1.rds.amazonaws.com",
    user="root",
    password="viewshine-heatmap-database-pass",
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
