from flask import Flask, request, jsonify, send_file, render_template
from assignment_02 import audio_record, text_to_speech
from assignment_03 import text_response
from Milestone_02 import analyze_audio

app = Flask(__name__)

# Route to serve the HTML webpage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_audio():
    audio_file = request.files['audio']
    audio_path = "./temp_recording.wav"
    audio_file.save(audio_path)

    # Process audio
    transcribed_text, _ = audio_record(audio_path)
    analysis = analyze_audio(audio_path)
    ai_response = text_response(transcribed_text, analysis)
    text_to_speech(ai_response)

    return jsonify({
        "transcription": transcribed_text,
        "sentiment": analysis.get("sentiment"),
        "tone": analysis.get("tone"),
        "intent": analysis.get("intent"),
        "response": ai_response,
    })

@app.route('/response-audio')
def get_response_audio():
    return send_file("./output_audio.wav", mimetype="audio/wav")

if __name__ == '__main__':
    app.run(debug=True)
