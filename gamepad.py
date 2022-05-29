from tkinter import Y
import vgamepad as pd
import serial

X_ID = 15
Y_ID = 14

arduino = serial.Serial();

gamepad = pd.VX360Gamepad()

def process_data(data):
    slices = data.split(";")
    out = {}
    for slice in slices:
        parts = slice.split("=")
        if len(parts) != 2 :
            continue
        out[int(parts[0])] = int(parts[1])
    return out

def byte2float(number):
    if number is None:
        return 0
    tmp = float(number) / 255.0 
    tmp = tmp * (-2);
    return tmp + 1


arduino.baudrate = 115200
arduino.port = "COM8"
arduino.open()
while 1:
    data = arduino.readline()
    try:
        print(X_ID)
        input_data = data.decode().replace("\n", "");
        obj = process_data(input_data)
        print(obj)
        gamepad.right_joystick_float(x_value_float=byte2float(obj.get(X_ID)), y_value_float=byte2float(obj.get(Y_ID)))
        gamepad.update();

    except ValueError:
        pass
arduino.close()
