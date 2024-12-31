# PRODIGY_NT4
# Simple Keylogger
A basic keylogger program that records and logs keystrokes, saving them to a file. Developed as part of my internship at Prodigy InfoTech.

# Features
Logs keystrokes in real-time.
Saves recorded keystrokes to a text file.

# Explanation of the code:
Key Press Logging:

The on_press function is called every time a key is pressed. It checks if the key is a regular key (like letters or numbers) or a special key (like Shift, Space, Enter, etc.). The key is then logged into a file called keylog.txt.
Handling Special Keys:

The try block handles regular characters, while the except block handles special keys (e.g., Shift, Ctrl, Esc).
Stopping the Keylogger:

The on_release function stops the keylogger when the Esc key is pressed. This is done by returning False to the listener, which ends the program.
Logging the Keystrokes:

Keystrokes are logged in real-time to the keylog.txt file in the same directory where the script is run.

# Ethical Considerations
This tool is intended for educational purposes only. Use it responsibly and only with explicit permission. Unauthorized use of keyloggers can be illegal and unethical.
