import glob
import os
import requests
import sys
import serial

def serial_ports_list():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

try:
    # This gets the user input COM Port from docker
    comport = os.environ["COM_PORT"]
    webhook = os.environ["WEBHOOK_URL"]
except:
    # comport = '/dev/tty.usbmodem4201'
    # webhook = 'https://hanr.tfoote.net/pyscan'
    print("Unable to automatically set comport or webhook. Please set COM_PORT and WEBHOOK_URL as environment variables.")
    print("Unable to continue")
    print("Here is list of available COM Ports:")
    print(serial_ports_list())
    exit()

ser = serial.Serial(comport)
while True:
    if ser.in_waiting > 0:
        data = {
            "raw": ser.readline()
        }

        data['reader_id'] = data['raw'][0:2]
        data['data'] = data['raw'][2:-2]
        
        requests.post(webhook, data = data)