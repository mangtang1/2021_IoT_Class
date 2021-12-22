import pyaudio
import wave

SAMPLE_RATE = 44100
FORMAT = pyaudio.paInt16
CHANNELS = 1
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=SAMPLE_RATE,input=True,frames_per_buffer=CHUNK)

print('start recording')

frames = []

for i in range(0,int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print('stop recording')

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.opn('output.wav','wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(SAMPLE_RATE)
wf.writeframes(b'',join(frames))
wf.close()