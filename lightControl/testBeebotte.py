#!/usr/bin/python3
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json

import config

HOSTNAME = "mqtt.beebotte.com"
#PORT = 8883
PORT = 1883
TOKEN = config.TOKEN
TOPIC = config.TOPIC
CACERT = config.CACERT

def on_connect(client, userdata, flags, respons_code):
    print('status {}'.format(respons_code))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print('msg.topic')
    print(msg.topic + " " + str(msg.payload))
    data = json.loads(msg.payload.decode("utf-8"))["data"]
    print(data)
    print(type(data))

def main():
    client = mqtt.Client()
    client.username_pw_set("token:%s"%TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message
    #client.tls_set(CACERT)
    client.connect(HOSTNAME, port=PORT, keepalive=60)
    client.loop_forever()

if __name__ == '__main__':
    main()