import serial

ser = serial.Serial('COM3')
ser.write(b'line1line2line3line4line5line6line7line8 ')

