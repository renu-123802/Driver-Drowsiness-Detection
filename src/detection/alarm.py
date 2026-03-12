import pygame
import os

# Initialize mixer once at the start
pygame.mixer.init()

alarm_playing = False

def play_alarm():
    global alarm_playing
    if not alarm_playing:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        alarm_file = r'C:\Users\renub\OneDrive\Desktop\DriveAlert\src\alarm\alarm.mp3'
        if not os.path.exists(alarm_file):
            print(f"Error: Could not find {alarm_file}")
            return

        try:
            pygame.mixer.music.load(alarm_file)
            pygame.mixer.music.play(-1)
            alarm_playing = True
        except Exception as e:
            print(f"Failed to play alarm: {e}")

def stop_alarm():
    global alarm_playing
    if alarm_playing:
        pygame.mixer.music.stop()
        alarm_playing = False
