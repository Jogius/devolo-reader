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

  device = homecontrol.devices.get(homecontrol.device_names.get(os.getenv("DEVOLO_DEVICE_NAME")))
  sensor = device.get_property("multi_level_sensor")
  for s in sensor:
    if s.sensor_type == os.getenv("DEVOLO_SENSOR_TYPE"):
      print(s.value)
