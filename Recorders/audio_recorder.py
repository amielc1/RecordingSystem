import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

try:
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    write('output.wav', fs, myrecording)  # Save as WAV file
    sd.wait()  # Wait until recording is finished
except:
    print("Error with starting sound recorder ")
