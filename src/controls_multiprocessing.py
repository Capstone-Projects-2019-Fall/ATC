import serial
from time import sleep
import multiprocessing
ser = serial.Serial('/dev/ttyACM0', 9600)
all_processes = []

def send_inputs(number):
    while True:
        if number == 4:
            ser.write(b'4')
            sleep(0.1)
        elif number == 5:
            ser.write(b'5')
            sleep(0.1)            
        elif number == 6:
            ser.write(b'6')
            sleep(0.1)            
        elif number == 7:
            ser.write(b'7')
            sleep(0.1)            
        elif number == 0:
            ser.write(b'0')
            sleep(0.1)            


# while True:
#     '''ser.write(b'4')
#     ser.write(b'5')'''
#     user_input = input("please put in a number to start driving")
#     if user_input == 4:
#         ser.write(b'4')
#     elif user_input ==5:
#         ser.write(b'5')
#     elif user_input == 6:
#         ser.write(b'6')
#     elif user_input == 7:
#         ser.write(b'7')
#     elif user_input == 0:
#         ser.write(b'0')
#     sleep(0.1)

def main():
    while True:
        user_input = input("Input a number: ")
        if user_input == "":
            continue
        if int(user_input) == 4:
            if len(all_processes) > 0:
                for process in all_processes:
                    process.terminate()
                    print("Process is alive status: ", process.is_alive())
                all_processes.clear()
            t1 = multiprocessing.Process(target=send_inputs, args=(4,))
            print("starting a new process")
            t1.start()
            all_processes.append(t1)
        elif int(user_input) == 5:
            if len(all_processes) > 0:
                for process in all_processes:
                    process.terminate()
                    print("Process is alive status: ", process.is_alive())                    
                all_processes.clear()
            t1 = multiprocessing.Process(target=send_inputs, args=(5,))
            print("starting a new process")            
            t1.start()
            all_processes.append(t1)
        elif int(user_input) == 6:
            if len(all_processes) > 0:
                for process in all_processes:
                    process.terminate()
                    print("Process is alive status: ", process.is_alive())                    
                all_processes.clear()
            t1 = multiprocessing.Process(target=send_inputs, args=(6,))
            print("starting a new process")            
            t1.start()
            all_processes.append(t1)
        elif int(user_input) == 7:
            if len(all_processes) > 0:
                for process in all_processes:
                    process.terminate()
                    print("Process is alive status: ", process.is_alive())                    
                all_processes.clear()
            t1 = multiprocessing.Process(target=send_inputs, args=(7,))
            print("starting a new process")            
            t1.start()
            all_processes.append(t1)            
        elif int(user_input) == 0:
            if len(all_processes) > 0:
                for process in all_processes:
                    process.terminate()
                    print("Process is alive status: ", process.is_alive())                    
                all_processes.clear()
            t1 = multiprocessing.Process(target=send_inputs, args=(0,))
            print("starting a new process")            
            t1.start()
            all_processes.append(t1)            
    
if __name__ == '__main__':
    main()
