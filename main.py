import sounddevice as sd
import socket

# Настройки
SERVER_IP = '0.0.0.0'  # IP сервера, измените на IP вашего сервера
PORT = 59010  # Порт для приема звука
CHUNK_SIZE = 2048  # Размер аудиоблока
RATE = 48000  # Частота дискретизации
CHANNELS = 1  # Количество каналов

# Настройка UDP-клиента
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))  # Привязываем сокет к порту

print(f"Клиент запущен, ожидание аудиоданных от сервера на {SERVER_IP}:{PORT}...")

# Функция для воспроизведения аудиоблоков
def callback(outdata, frames, time, status):
    if status:
        print(f"Статус: {status}", flush=True)
    
    # Получаем аудиоблоки из сокета
    data, addr = sock.recvfrom(CHUNK_SIZE * CHANNELS * 2)  # 2 байта на выборку для int16
    outdata[:len(data)] = data  # Воспроизводим полученные данные

# Запускаем поток для воспроизведения
with sd.OutputStream(samplerate=RATE, channels=CHANNELS, dtype='int16', callback=callback):
    print("Воспроизведение аудиоданных запущено.")
    while True:
        pass  # Продолжаем слушать и воспроизводить данные