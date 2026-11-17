# Student Study Assistant

## Project topic
**Student Study Assistant** — a simple virtual assistant that supports students with study tips, time management, exam preparation, motivation, basic programming guidance, and date/time information.

## Features
- Chat-style user interface
- Responds to common student questions
- Provides study and exam preparation tips
- Offers time-management suggestions
- Gives basic programming-learning guidance
- Displays the device's current date and time
- Clear-chat button

## Technologies
- Python 3.9+
- Streamlit

## Run the project locally

1. Install Python.
2. Extract this project folder.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL shown in the terminal (usually `http://localhost:8501`).

## How it works
The `get_reply()` function checks the user's message for keywords and returns a suitable predefined response. Streamlit displays the conversation in a chat interface. This is a beginner-friendly, rule-based assistant; it does not use an external AI API.

## Suggested GitHub repository name
`student-study-assistant`

## GitHub upload
1. Sign in to GitHub and create a new public repository named `student-study-assistant`.
2. Upload `app.py`, `requirements.txt`, `topic.txt`, and `README.md` (or upload the extracted folder contents).
3. Commit the files.
4. Copy the repository URL and submit that URL with your assignment.

## Future improvements
- Add voice input and text-to-speech.
- Add a notes and reminders feature.
- Connect a trusted AI API for more flexible answers.
