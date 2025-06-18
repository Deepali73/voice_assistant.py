# 🎙️ Voice Assistant Launcher (Streamlit + Speech Recognition + Multithreading)

This is a simple yet powerful **desktop voice assistant app** built with **Streamlit**, **speech recognition**, **text-to-speech (TTS)**, and **multithreading** in Python. It enables users to launch common Windows applications using **voice commands** or **manual input** with a responsive interface.

---

## ⚙️ Features

- 🎤 Recognizes voice input using your system microphone
- 📢 Text-to-speech engine gives verbal feedback
- 🖥️ Launches desktop applications via voice or text input
- 🚀 Uses **multi-threading** to keep the Streamlit UI responsive
- 📝 Option to type commands as an alternative to speaking

---

## 🧠 Why Multithreading?

This app uses Python's `threading.Thread` to:

- Run the TTS engine in the background (non-blocking)
- Launch system applications without freezing the UI
- Maintain a **smooth and responsive experience** in Streamlit

---

## 🖥️ Supported Voice/Text Commands

You can say or type:

- `Launch Notepad`
- `Open Firefox`
- `Play VLC Player`
- `Start Calculator`
- `Open Command Prompt` or `Start CMD`
- `Start Virtual Box`
- `Open Paint`

