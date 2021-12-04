from sys import argv

if len(argv) < 3:
  exit(1)

device_id = argv[1]
sensor_type = argv[2]

import logging
import os
from dotenv import load_dotenv

from devolo_home_control_api.homecontrol import HomeControl
from devolo_home_control_api.mydevolo import Mydevolo

load_dotenv()

logging.disable()

mydevolo = Mydevolo()
mydevolo.user = os.getenv("DEVOLO_USER")
mydevolo.password = os.getenv("DEVOLO_PASSWORD")

gateway_id = mydevolo.get_gateway_ids()[0]
with HomeControl(gateway_id=gateway_id, mydevolo_instance=mydevolo) as homecontrol :

  if device_id not in homecontrol.devices:
    exit(1)

  device = homecontrol.devices.get(device_id)
  
  sensor = device.get_property("multi_level_sensor")
  for s in sensor:
    if s.sensor_type == sensor_type:
      print(s.value)
