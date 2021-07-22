import json
import requests
import redis
import websocket
import time
import csv

ws=websocket.WebSocket()

urldev = 'ws://localhost:8000/ws/polData/'
urlprod = ''

ws.connect('ws://localhost:8000/ws/polData/')


with open("djangoHiring/data.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        time.sleep(0.01)
        ws.send(json.dumps({'value':row}))
