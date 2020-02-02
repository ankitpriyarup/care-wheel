import serial
import requests
import time
import threading
ser = serial.Serial('/dev/ttyACM0', 115200)

bpm = 0.0
dis = 0.0
def perform():
    while True:
        bpm_bin = ser.readline()
        dis_bin = ser.readline()
        cur_bpm = (bpm_bin.decode('ascii'))[5:-2]
        cur_dis = (dis_bin.decode('ascii'))[10:-2]
        if cur_bpm.isdigit():
            bpm = cur_bpm
        if cur_dis.isdigit():
            dis = cur_dis


if __name__ == "__main__":
    commands = threading.Timer(10.0, perform)
    commands.start()
    while True:
        if bpm > 50 and bpm < 200:
            print("bpm: " + str(bpm))
            requests.post('http://127.0.0.1:5000/api/post_update/bb411a9c5f6631634a342779b28cc612',
                          json={"username": "ankitpriyarup", "key": "qazwsxedc", "hr": bpm})
        print("dis: " + str(dis))
        requests.post('http://127.0.0.1:5000/api/post_update/bb411a9c5f6631634a342779b28cc612',
                      json={"username": "ankitpriyarup", "key": "qazwsxedc", "distance": dis})
        time.sleep(5)