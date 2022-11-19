from flask import Flask, request, render_template
import sounddevice as sd
from time import sleep
from scipy.io.wavfile import write


def shock_me():
    '''Function that shock user (not completed) '''
    fs = 44100  # Sample rate
    seconds = 6  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sleep(1)
    print('shock')
    sd.wait()


    sd.play(myrecording, fs)
    sd.wait()
    write('static/output.wav', fs, myrecording)

def wait():
    '''Simulate a shock by waiting and'''
    print('Shock')
    sleep(5)


app = Flask(__name__)

@app.route('/')
def main_page():
    '''Main page'''
    return render_template('index.html')

@app.route('/button')
def button():
    '''Button page which show the button that is link to audio_output page'''
    return render_template('button.html')

@app.route('/audio_output', methods=['GET', 'POST'])
def audio_output():
    '''The end page which show the audio output'''
    if request.method == 'POST':
        wait()
    return render_template('audio_output.html')

app.run()
