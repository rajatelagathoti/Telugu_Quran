import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="PDF & Text Reader")

st.title("PDF Download and Text-to-Speech")

# PDF download
with open("sample.pdf", "rb") as pdf_file:
    st.download_button(
        label="Download PDF",
        data=pdf_file,
        file_name="sample.pdf",
        mime="application/pdf",
    )

# Text-to-Speech
text = st.text_area("Enter text to read aloud:")

if st.button("Generate Speech") and text.strip():
    tts = gTTS(text=text, lang="en")
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    st.audio(audio_buffer.getvalue(), format="audio/mp3")
