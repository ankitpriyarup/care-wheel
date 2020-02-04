import serial, requests, time, re
from threading import Thread, Event
ser = serial.Serial('/dev/ttyACM0', 115200)

bpm = "None"
dist = "None"
first = False
second = False
if __name__ == "__main__":
    while True:
        data = str(ser.readline())
        cur = re.findall("M: \d+\.*\d+", data)
        if len(cur) > 0:
            bpm = str(cur[0])[3:]
        cur = re.findall("e: \d+\.*\d+", data)
        if len(cur) > 0:
            dist = str(cur[0])[3:]
        if "ER!" in data:
            if "NO" not in data:
                if first is False:
                    first = True
                elif second is False:
                    second = True
                else:
                    print("DANGER!")
            else:
                first = False
                second = False


        cur = re.findall("e: \d+\.*\d+", data)
        print("BPM: " + str(bpm) + ", Distance: " + str(dist))