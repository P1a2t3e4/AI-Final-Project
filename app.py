import streamlit as st
import urllib.parse
import os
import assemblyai as aai

# Set the environment variable for Google Cloud Storage credentials
key_path = os.path.abspath(r"C:\Users\NANA\OneDrive\Desktop\AI Final Project\ai-final-project-406013-de6f0227d24d.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

aai.settings.api_key = f"2e1a0f6f18d64f81af1402321dc51367"

# Function to transcribe audio from Google Cloud Storage
def transcribe_audio(audio_url):
    """Transcribes audio from a user-provided URL."""
    # URL-encode the filename
    parsed_url = urllib.parse.urlparse(audio_url)
    bucket_name = parsed_url.netloc
    gcs_file_name = parsed_url.path[1:]

    # Configure the transcription
    config = aai.TranscriptionConfig(speaker_labels=True)

    # Perform the transcription
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_url, config)

    # Print the transcription
    st.write("Transcription:")
    st.write(transcript.text)

    # Print speaker labels and utterances
    for utterance in transcript.utterances:
        st.write(f"Speaker {utterance.speaker}: {utterance.text}")
    
    return transcript

# Function to generate a condensed summary of the audio content
def condensed_summary(audio_url):
    """Generate a condensed summary of the audio content."""
     # Configure auto-chapters
    config = aai.TranscriptionConfig(auto_chapters=True)

    # Perform transcription with auto-chapters
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_url, config)

    # Print auto-chapters
    st.write("Summary:")
    for chapter in transcript.chapters:
        st.write(f"{chapter.start}-{chapter.end}: {chapter.headline}")

# Streamlit app
def main():
    st.title("Audio Transcriber and Summarizer")

    # Input for Google Cloud Storage audio URL
    audio_url = st.text_input("Enter Google Cloud Storage Audio URL:")

    # Button to trigger transcription
    if st.button("Transcribe Audio"):
        st.write("Transcribing audio...")
        transcript = transcribe_audio(audio_url)

        # Button for Condensed Summary
    if st.button("Condensed Summary"):
        st.write("Generating Condensed Summary...")
        condensed_summary(audio_url)

if __name__ == "__main__":
    main()