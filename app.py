from koradserial import KoradSerial
import time
import sys
if len(sys.argv) != 3:
  print("Usage: app.py serial_port output file")
  sys.exit(-1)
with KoradSerial(sys.argv[1]) as power_supply:
  with open(sys.argv[2], 'w') as f:
    f.write("time,voltage,current\n")
    while True:
      f.write("{0},{1},{2}\n".format(time.time(), power_supply.channels[0].output_voltage, power_supply.channels[0].output_current))
      time.sleep(1)
