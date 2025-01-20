# Video Transcription and Translation Tool

This Python program transcribes and translates video files into text documents. It supports multiple languages and handles various video formats.

## Features
- Transcribes video files to text
- Translates text to desired language
- Saves output as text files
- Supports common video formats (MP4, AVI, MOV, etc.)
- Includes error handling and retry logic

## Requirements
- Python 3.7+
- FFmpeg (system-wide installation required)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/umairalamchaudhry/Video-Transcriber.git
   cd Video-Transcriber
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install FFmpeg (Windows):
   a. Download FFmpeg from https://www.gyan.dev/ffmpeg/builds/
   b. Choose the "ffmpeg-release-full.7z" file
   c. Extract the downloaded file to C:\ffmpeg
   d. Add FFmpeg to system PATH:
      - Open Start Menu and search for "Environment Variables"
      - Click "Edit the system environment variables"
      - Click "Environment Variables" button
      - In System variables, find Path and click Edit
      - Click New and add: C:\ffmpeg\bin
      - Click OK to save changes
   e. Verify installation:
      - Open Command Prompt
      - Run: ffmpeg -version
      - You should see FFmpeg version information

## Usage

1. Place your video file in the project directory
2. Run the program:
   ```bash
   python transcriber.py
   ```
3. Follow the prompts:
   - Enter video file name
   - Choose target language code
   - Enter output file name

The program will:
- Convert video to audio
- Transcribe audio to text
- Translate text to target language
- Save transcription as text file
- Show preview in terminal

## Code Overview

### Main Components

1. **Audio Conversion**
   - Uses pydub and FFmpeg to convert video to WAV format
   - Handles various video formats

2. **Speech Recognition**
   - Uses SpeechRecognition library
   - Implements Google Web Speech API
   - Includes retry logic for API calls

3. **Translation**
   - Uses deep-translator library
   - Supports multiple languages
   - Handles API errors gracefully

4. **File Handling**
   - Saves transcriptions as UTF-8 encoded text files
   - Cleans up temporary files

### Error Handling
- Checks for file existence
- Handles API errors with retries
- Provides meaningful error messages

## Supported Languages
The program supports translation to any language supported by Google Translate. Common codes:
- English: en
- Spanish: es
- French: fr
- Hindi: hi
- Urdu: ur

## Troubleshooting

### FFmpeg Issues
- Ensure FFmpeg is installed and in PATH
- Verify installation with `ffmpeg -version`

### API Errors
- Check internet connection
- Try again later if API quota exceeded

## License
MIT License

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss proposed changes.

## Acknowledgments
- pydub for audio processing
- SpeechRecognition for transcription
- deep-translator for translation