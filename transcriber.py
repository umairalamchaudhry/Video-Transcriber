import os
import sys
import time
import speech_recognition as sr
from deep_translator import GoogleTranslator

os.environ["PATH"] += os.pathsep + "C:\\ffmpeg\\bin"
from pydub import AudioSegment


def main():
    print("Video Transcriber")
    print("-----------------")
    video_file = input("Enter video file name (must be in current directory): ")

    if not os.path.exists(video_file):
        print(f"Error: File '{video_file}' not found in current directory")
        return

    print("\nCommon language codes:")
    print("English: en, Spanish: es, French: fr")
    print("Hindi: hi, Urdu: ur")
    language = input("\nEnter target language code: ")

    print("Processing video...")
    text = transcribe_audio(video_file)

    print("Translating text...")
    translated_text = translate_text(text, language)

    print("\nTranscription complete!")

    # Get output file name
    output_file = input("\nEnter output file name (without extension): ") + ".txt"

    # Save transcription to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translated_text)

    print(f"\nTranscription saved to {output_file}")
    print("\nPreview of transcription:")
    print(translated_text[:500] + ("..." if len(translated_text) > 500 else ""))


def transcribe_audio(video_file):
    try:
        # Convert video to WAV
        sound = AudioSegment.from_file(video_file)
        wav_file = "audio.wav"
        sound.export(wav_file, format="wav")

        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_file) as source:
            audio = recognizer.record(source)

        # Try Google Web Speech API with retries
        max_retries = 3
        for attempt in range(max_retries):
            try:
                text = recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                if attempt == max_retries - 1:
                    return "Could not understand audio"
            except sr.RequestError as e:
                if attempt == max_retries - 1:
                    print(f"Google Speech Recognition error: {str(e)}")
                    # Try alternative API if available
                    try:
                        text = recognizer.recognize_whisper(audio)
                        return text
                    except:
                        return "API unavailable"
            # Wait before retrying
            time.sleep(1)

        return "Transcription failed after multiple attempts"
    finally:
        # Clean up WAV file
        if os.path.exists(wav_file):
            os.remove(wav_file)


def translate_text(text, dest_language):
    translation = GoogleTranslator(source="auto", target=dest_language).translate(text)
    return translation


if __name__ == "__main__":
    main()
