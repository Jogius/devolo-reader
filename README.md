# devolo-reader

> A small python script that fetches data from MyDevolo Smart Home devices

## Running the script
Copy the ``.env.example`` file to ``.env`` and add the values associated with the keys (MyDevolo username, password).
Then run the script (``python3 src/main.py <device_id> <sensor_type>``), where ``device_id`` is in the format hdm:ZWave:XXXXXXXX/XX and ``sensor_type`` can be e.g. ``temperature`` or ``light``.
