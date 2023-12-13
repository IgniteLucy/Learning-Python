import simpleaudio.functionchecks as fc
import simpleaudio as sa
import os 
import time
from pydub import AudioSegment
 # fc.LeftRightCheck.run() first check if audio works
 # https://pypi.org/project/simpleaudio/ -- documentation starter -- 

# script dir path
script_dir = os.path.dirname(os.path.abspath(__file__))

#Sounds directory
sounds_dir = os.path.join(script_dir,'..', 'Sounds')

#Define audio path
sounds_files = [f for f in os.listdir(sounds_dir) if os.path.isfile(os.path.join(sounds_dir,f))]

#alphabetically sorted
sounds_files.sort()



#Group by extension
grouped_files = {}
for file in sounds_files:
    _, extension = os.path.splitext(file)
    grouped_files.setdefault(extension, []).append(file)


#Display numbered list of files 
print("Select a file to play")


extensions = ['.mp3', '.wav']

i = 1  # Initialize file counter

for extension in extensions:
    if extension in grouped_files:
        extension_files = sorted(grouped_files[extension])
        for file in extension_files:
            print(f"{i}) {file} ({extension[1:]})")
            i += 1

#Now we wanna check if the file already exists in wav. form
try:
    choice = int(input("Enter the number of the file you want to play: "))
    selected_file = [file for extension, files in grouped_files.items() for file in files][choice - 1]

    if selected_file.lower().endswith(".wav"):
        audio_file_path = os.path.join(sounds_dir, selected_file)
    else:
        #check if there is a wav file available
        wav_variant = os.path.splitext(selected_file)[0] + '.wav'
        wav_path = os.path.join(sounds_dir,wav_variant)
        if os.path.isfile(wav_path):
            audio_file_path = wav_path
        else:
            #convert mp3 to wav
            mp3_path = os.path.join(sounds_dir,selected_file)
            wav_path = os.path.join(sounds_dir,os.path.splitext(selected_file)[0] + '.wav')
            sound =  AudioSegment.from_mp3(mp3_path)
            sound.export(wav_path, format="wav")
            audio_file_path = wav_path
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



