import pygame
from pygame.locals import QUIT
from datetime import datetime, time
import os
import subprocess
import signal

# Set the time range for checking phone connection 
start_time = time(22, 0)
end_time = time(23, 0)

# Path to the alarm sound file (replace with your own sound file)
alarm_sound_file = "/home/cheat/Documents/mayabono.wav"

def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(alarm_sound_file)
    pygame.mixer.music.play()
    print("2")
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        print("3")
        if check_phone_connection():
            print("4")
            pygame.mixer.music.stop()
            break

def check_phone_connection():
        # Run lsusb command to list USB devices
        lsusb_output = subprocess.check_output(["lsusb"]).decode("utf-8")
        print(lsusb_output)

        # Check if your phone is connected by searching for its identifier (adjust as needed)
        if "18d1:4ee1" in lsusb_output:
            return True
        else:
            return False

def main():
    pygame.init()

    try:
        while True:
            current_time = datetime.now().time()
            #print("1")

            if start_time <= current_time <= end_time:
                print("Monitoring USB events. Press Ctrl+C to exit.")
                while True:
                    if not check_phone_connection():
                        print("Phone not connected. Playing alarm sound.")
                        play_alarm_sound()
                        pygame.time.delay(1000)  # Delay for 1 second
                    else:
                        print(f"Phone connected at {datetime.now()}")
    except KeyboardInterrupt:
        pass
    finally:
            pygame.quit()

if __name__ == "__main__":
    main()

