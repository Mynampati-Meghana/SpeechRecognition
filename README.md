# Speech Recognition Voice Assistant

A Python-based multilingual voice assistant that uses speech recognition and text-to-speech to interact with the user.

## Features

- Select a language before each conversation
- Supports English, Hindi, Telugu, Tamil, and Marathi
- Converts speech into text
- Displays recognized speech in the terminal
- Saves recognized speech to an output file
- Records the date and time of each speech input
- Records the selected language
- Text-to-speech responses from the assistant
- Allows the user to continue or stop the conversation
- Starts a new language-selection session when the user chooses to continue

## Supported Languages

| Language | Code |
|----------|------|
| English | en-IN |
| Hindi | hi-IN |
| Telugu | te-IN |
| Tamil | ta-IN |
| Marathi | mr-IN |

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAudio

## Project Structure

```text
SpeechRecognition/
│
├── assistant.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore