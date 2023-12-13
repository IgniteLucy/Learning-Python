import simpleaudio.functionchecks as fc
import simpleaudio as sa
import os 
import time
 # fc.LeftRightCheck.run() first check if audio works
 # https://pypi.org/project/simpleaudio/ -- documentation starter -- 

# script dir path
script_dir = os.path.dirname(os.path.abspath(__file__))

#Define audio path
audio_file_path_mp3 = os.path.join(script_dir, '..', 'Sounds', 'You_so_port.mp3')
audio_file_path_wav = os.path.join(script_dir, '..', 'Sounds', 'You_so_port.wav')



try:
    print("Playing audio in 3....")
    time.sleep(1)
    print("Playing audio in 2....")
    time.sleep(1)
    print("Playing audio in 1....")
    time.sleep(1)
    wav_obj = sa.WaveObject.from_wave_file(audio_file_path_mp3)
except Exception:
    print("Hmm, seems we have to switch")
    time.sleep(1)
    print("Seems that the program did not like using the mp3 file")
    time.sleep(0.5)
    print("Lets use a wav file now")
    time.sleep(0.5)
    print("Playing audio in 3....")
    time.sleep(1)
    print("Playing audio in 2....")
    time.sleep(1)
    print("Playing audio in 1....")
    time.sleep(1)
    wav_obj = sa.WaveObject.from_wave_file(audio_file_path_wav)




play_obj = wav_obj.play()
print("Kitty! what u doing out here")
time.sleep(1.5)
print("Did i not see u here before?")
time.sleep(1.2)
print("MEOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOW")
time.sleep(1.5)
print("HO")
time.sleep(0.2)
print("HA")
time.sleep(0.15)
print("HA")
time.sleep(0.2)
print("HO")
time.sleep(0.1)
print("HA")
time.sleep(0.2)
print("HA")
time.sleep(0.1)
print("you are so portuguse :3")
play_obj.wait_done()


#without the try except state
#wav_obj = sa.WaveObject.from_wave_file(audio_file_path)
#play_obj = wav_obj.play()
#play_obj.wait_done()



