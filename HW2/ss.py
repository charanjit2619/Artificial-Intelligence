import pandas as pd
import numpy as np
import os
import websocket
import json
import time
import traceback

ws = websocket.WebSocket()
print("Connecting to Tobii Glasses 3...")
try:
    ws.connect("ws://192.168.75.51/websocket", subprotocols=["g3api"])
    print("Connection successful!")
except Exception as e:
    print(e)
    print("Connection unsuccessful - please see exception for reason. Terminating program.")
    exit()

ws.send(json.dumps({"path":"system.recording-unit-serial", "id":1, "method":"GET", "body": None}))
a = ws.recv()
print(a)