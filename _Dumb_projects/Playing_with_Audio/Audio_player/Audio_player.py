import simpleaudio.functionchecks as fc
import simpleaudio as sa
import os 
import time
 # fc.LeftRightCheck.run() first check if audio works
 # https://pypi.org/project/simpleaudio/ -- documentation starter -- 

# script dir path
script_dir = os.path.dirname(os.path.abspath(__file__))

#Sounds directory
sounds_dir = os.path.join(script_dir,'..', 'Sounds')

#Define audio path
sounds_files = [f for f in os.listdir(sounds_dir) if os.path.isfile(os.path.join(sounds_dir,f))]


#Display numbered list of files 
print("Select a file to play")
for i , file in enumerate(sounds_files, start=1):
    print(f"{i}) {file}")

try:
    choice = int(input("Enter the number of the file you want to play: "))
    selected_file = sounds_files[choice - 1]
    audio_file_path = os.path.join(sounds_dir, selected_file)
except (ValueError, IndexError):
    print("Invalid choice. Exiting.")
    exit()



try:
    print("Playing audio in 3....")
    time.sleep(1)
    print("Playing audio in 2....")
    time.sleep(1)
    print("Playing audio in 1....")
    time.sleep(1)
    print(f"Playing audio file: {selected_file}")
    wav_obj = sa.WaveObject.from_wave_file(audio_file_path)
except Exception as e:
    print("Hmm, seems we have extension issue, switch it!")
    time.sleep(1)
    print("Seems that the program did not like using the mp3 file")
    time.sleep(0.5)
    print("please consider first converting the file into a wav file, thankyou")
    time.sleep(0.5)
    print(f"Error loading audio file: {e}")
    exit()



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



