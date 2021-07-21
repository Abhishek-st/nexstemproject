import json
import requests
import redis
import websocket
import random,time

ws=websocket.WebSocket()
ws.connect('ws://localhost:8000/ws/polData/')

for i in range(1000):
    time.sleep(3)
    ws.send(json.dumps({'value':random.randint(1,100)}))


# import asyncio
# import websockets

# async def hello():
#     uri = "ws://localhost:8000/ws/polData/"
#     async with websockets.connect(uri) as ws:
#         for i in range(1000):
#             time.sleep(3)
#             ws.send(json.dumps({'value':random.randint(1,100)}))

# asyncio.get_event_loop().run_until_complete(hello())