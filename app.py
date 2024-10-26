from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    # Get the audio file from the request
    audio_file = request.files['audio']
    audio_path = os.path.join("uploads", "recording.mp3")
    os.makedirs("uploads", exist_ok=True)
    audio_file.save(audio_path)
    print(audio_path)


    # IMPLEMENT WHEN BACKEND LOGIC COMPLETE os.remove(audio_path)
    
    return "Audio received successfully!"

if __name__ == '__main__':
    app.run(debug=True)
