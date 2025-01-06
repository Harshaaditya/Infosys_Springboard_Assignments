from assignment_02 import audio_record,text_to_speech
from assignment_03 import text_response
from Milestone_02 import analyze_audio

def main():
    print("\n🛒 **Welcome to the Real-Time AI Sales Assistant!** 🛒")
    print("Say 'exit' to end the chat.\n")

    while True:
        print("You: ")
        print("Listening for your input...")
        transcribed_text,audio_document= audio_record()
        summary= analyze_audio(audio_document)
        print(summary)

        if "exit" in transcribed_text.lower():
            transcribed_text = "Goodbye! Have a great day! 👋"
            print(transcribed_text)
            text_to_speech(transcribed_text)
            break
        ai_response = text_response(transcribed_text,summary)
        print("\nAI Sales Assistant:", ai_response, "\n")

        text_to_speech(ai_response)

if __name__ == "__main__":
    main()