# audio-Voice-Detector
 Audio Voice Detector
A simple Python-based Audio Voice Detector that captures audio input from the microphone and detects the presence of voice using sound thresholding. It can be used for voice activity detection, audio-triggered automation, or basic audio surveillance applications.
 Features
Detects the presence of voice in real-time using microphone input

Supports threshold-based voice activity detection

Records segments of audio when voice is detected

Saves recorded audio to WAV files (optional)

Easy to configure and extend

Requirements
Install the required libraries using pip:

bash
Copy
Edit
pip install pyaudio numpy scipy
Note: You may need to install portaudio on some systems for pyaudio to work.

For macOS:

bash
Copy
Edit
brew install portaudio
pip install pyaudio
For Windows:
Download the correct .whl file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

How It Works
Continuously listens through the microphone.

Measures sound energy levels.

If the volume exceeds a set threshold, it's considered "voice detected".

Optionally records the detected voice to a .wav file.

 How to Use
bash
Copy
Edit
python voice_detector.py
Make sure your microphone is connected and set as the default input device.

 Configuration
You can modify the following parameters in the script:

python
Copy
Edit
THRESHOLD = 500      # Sound level threshold for detecting voice
CHUNK = 1024         # Number of audio samples per frame
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100         # Sampling rate in Hz
RECORD_SECONDS = 5   # Optional: duration of voice recording
📝 Example Output
bash
Copy
Edit
Listening for voice...
Voice detected! Recording started...
Recording saved to output_01.wav
Listening for voice...
File Structure
css
Copy
Edit
audio-voice-detector/
├── voice_detector.py
├── recordings/
│   └── output_01.wav
└── README.md
 To Do
Add GUI interface using Tkinter or PyQt

Add background noise suppression

Integrate speech-to-text for transcription

Add email/SMS alerts for voice detection
