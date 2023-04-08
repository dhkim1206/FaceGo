import serial

ser = serial.Serial('COM4', 9600, timeout=1) # 시리얼 포트와 통신 속도 설정

while True:
    value = input("보낼 값 입력: ") # 보낼 값을 입력 받음
    ser.write(value.encode()) # 시리얼 포트를 통해 보낼 값을 아두이노로 전송g

    line = ser.readline().decode("utf-8")
    print(line);