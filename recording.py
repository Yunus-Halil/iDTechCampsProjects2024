import wavio as wv
import sounddevice as sd
from scipy.io.wavfile import write

def record():
    freq = 44100
    duration = 5
    record = sd.rec((freq*duration),samplerate=freq,channels=2)
    print('start talking')
    sd.wait()
    wv.write('audio.wav',record,freq, sampwidth=2)
record()