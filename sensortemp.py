import PySimpleGUI as sg
from influxdb import InfluxDBClient
import datetime

client = InfluxDBClient(host="localhost", port=8086)
client.switch_database("sensortemp")
client.get_list_measurements()
results1 = client.query('SELECT max("temperature_F"), min("temperature_F") FROM "Acurite-606TX" GROUP BY time(24h)')
points1 = results1.get_points(measurement="Acurite-606TX")

points1 = list(points1)

sg.theme('LightBlue')

layout = [[sg.Text("Date registered"), sg.Text(" Max Temp"), sg.Text("     Min Tem")],
				[sg.Text(" ------------------------------------------------------------")],
				[[sg.Text("    " + point1['time'][0:10] + "     "), sg.Text(" " + str(point1['max'])[0:4] + " F    ", text_color='red' ),
				sg.Text("      " + str(point1['min'])[0:4] + " F  ", text_color='blue' )] for point1 in points1] ]
window = sg.Window('Sensortemp', layout, margins = (200, 20, 0, 0))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
window.close()