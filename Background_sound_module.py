import sounddevice
import soundfile


def start_bg_sound():
    sound_array, fs = soundfile.read('Sounds/Background_sound.wav')
    sounddevice.play(sound_array, fs, loop=True, blocking=False)


def stop_bg_sound():
    sounddevice.stop()









