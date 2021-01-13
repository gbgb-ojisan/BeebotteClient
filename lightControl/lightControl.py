#!/usr/bin/python3
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import subprocess
import time
import ssl

import config

HOSTNAME = "mqtt.beebotte.com"
#PORT = 8883
PORT = 1883
TOKEN = config.TOKEN
TOPIC = config.TOPIC
CACERT = config.CACERT

def execIrrp(action):
    if action == 'on':
        CODE = 'light:on'
        Ncmd = 1
    elif action == 'off':
        CODE = 'light:off'
        Ncmd = 1
    else:
        raise ValueError('Undefined action specified.')
    cmd = ['python3','irrp.py','-p', '-g17','-f','codes',CODE]
    for ir in range(Ncmd):
        subprocess.run(cmd)
        time.sleep(1)

def on_connect(client, userdata, flags, respons_code):
    print('status {}'.format(respons_code))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode("utf-8"))["data"]
    try:
        execIrrp(data)
    except ValueError as e:
        print(e)

def main():
    client = mqtt.Client()
    client.username_pw_set("token:%s"%TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message
    #client.tls_set(CACERT)
    #client.tls_insecure_set(True)
    client.connect(HOSTNAME, port=PORT, keepalive=60)
    client.loop_forever()

if __name__ == '__main__':
    main()