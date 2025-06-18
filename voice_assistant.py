import streamlit as st
import pyttsx3
import speech_recognition as sr
import os
import threading

# ===================== Text-to-Speech Setup =====================
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

# ===================== Voice Recognition =====================
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("🎤 Listening for your command.")
        st.info("🎙️ Listening... Please speak now.")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        st.success(f"🗣️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("❌ Sorry, I could not recognize your voice. Please try again.")
        st.error("Could not understand. Please try again.")
        return ""
    except sr.RequestError:
        speak("🚫 Speech recognition service is unavailable right now.")
        st.error("Recognition service error.")
        return ""

# ===================== Application Launcher =====================
def launch_app(command):
    if "notepad" in command:
        speak("Launching Notepad")
        os.system("start notepad")
    elif "firefox" in command:
        speak("Launching Firefox")
        os.system("start firefox")
    elif "vlc" in command:
        speak("Launching VLC Player")
        os.system("start vlc")
    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("start calc")
    elif "command prompt" in command or "cmd" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")
    elif "virtual box" in command:
        speak("Opening VirtualBox")
        os.system("start VirtualBox")
    elif "paint" in command:
        speak("Opening Paint")
        os.system("start mspaint")
    else:
        speak("Sorry, that application is not available.")
        st.warning("❌ Command not recognized.")

# ===================== Streamlit UI =====================
st.set_page_config(page_title="Voice Assistant", page_icon="🎙️")
st.title("🗣️ Voice Assistant Launcher")
st.markdown("Use your **voice or type** to launch commonly used applications on your system.")

with st.expander("📋 Available Voice Commands"):
    st.markdown("""
    **You can say or type any of these commands:**
    - `Launch Notepad`
    - `Open Firefox`
    - `Play VLC Player`
    - `Start Calculator`
    - `Open Command Prompt` or `Start CMD`
    - `Start Virtual Box`
    - `Open Paint`
    """)

# ========== Voice Button ==========
if st.button("🎤 Speak Command"):
    command = listen_command()
    if command:
        threading.Thread(target=launch_app, args=(command,)).start()

# ========== Text Input Option ==========
st.markdown("Or type your command below 👇")
typed_command = st.text_input("Enter Command:")
if st.button("🚀 Run Typed Command"):
    if typed_command.strip():
        threading.Thread(target=launch_app, args=(typed_command.lower(),)).start()
    else:
        st.warning("Please enter a command to run.")
