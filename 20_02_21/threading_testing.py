import threading
import os
import time
import datetime
from multiprocessing import Process

def func_1(a, b):
    print('Start func_1')
    time.sleep(7)
    print(a+b)
    time.sleep(3)
    print('End of func_1')

class Song:
    def __init__(self, duration, name):
        self.duration = duration
        self.name = name

    def __play(self):
        print(f'Song starts to play {self.name}')
        print(datetime.datetime.now())
        time.sleep(self.duration)
        self.stop(from_process=True)

    def play(self):
        self.process = Process(target=self.__play)
        self.process.start()

    def stop(self, from_process=False):
        if not from_process:
            self.process.terminate()
        print('Srong stoped')
        print(datetime.datetime.now())

FILE_PATH = './test_thread.txt'

def file_creation():
    print("Start file processing")
    print(datetime.datetime.now())
    time.sleep(10)
    with open(FILE_PATH, 'w') as f:
        f.write('Text')
    print("Ends file processing")


if __name__ == '__main__':
    thread_1 = threading.Thread(target=func_1, args=(1, 4), daemon=True)
    print('Starting main function!')
    thread_1.start()
    time.sleep(8)
    thread_1.join()
    print('Main after thread started.')

    song_1 = Song(10, 'song_1')
    song_2 = Song(11, 'song_2')
    song_2.play()
    song_1.play()
    time.sleep(7)
    song_2.stop()

    process = Process(target=file_creation)
    process.start()
    input_string = input('Test Input: ')
    process.join(2)
    print(datetime.datetime.now())
    with open(FILE_PATH, 'r') as f:
        print(f.readline())




