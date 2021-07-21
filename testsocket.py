import json
import requests
import redis
import websocket
import random,time
import csv

ws=websocket.WebSocket()
ws.connect('ws://localhost:8000/ws/polData/')

# for i in range(1000):
#     time.sleep(0.3)
#     randomlist = random.sample(range(1, 100), 5)
#     ws.send(json.dumps({'value':randomlist}))

with open("django-hiring-main/data.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        time.sleep(0.3)
        ws.send(json.dumps({'value':row}))
