# BeebotteClient > lightControl
## Overview

This is a sample of room light control using irrp and Beebotte.

The diagram is as below:
```
            IR signal                           MQTT
Room light <---------- irrp.py <- lightControl.py <---- Beebotte
```

## Prerequisites

- Python3
    - paho-mqtt
- pem file
    - You can get from Beebotte.
- codes
    - Generated from irrp.py
- config.py
    - See the details in section [config.py](#config.py)

## config.py
The sample of config.py is as follows:
```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
TOKEN = "token_xxx"
TOPIC = "lightControl/voice"
CACERT = "beebotte.pem"
```

**Be careful to this file because it has a secret key!!**