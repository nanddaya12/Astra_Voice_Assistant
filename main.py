from ears import listen
from brain import process_command
from voice import speak
import time

WAKE_WORD = "astra"

def main():
    speak("Initializing Nand's assistant.............. Ready for commands")
    while True:
        try:
            text = listen()
            print(f"Heard: {text}")  # Debug: show what was recognized
            if WAKE_WORD in text.lower():
                # process command
                command = text.lower().replace(WAKE_WORD, "").strip()
                print(f"Command: {command}")  # Debug: show extracted command
                response = process_command(command)
                print(f"Response: {response}")  # Debug: show response
                speak(response)
                time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()