# Advanced Keylogger with Real-time Telegram Reporting

This project is an advanced keylogger developed in Python. It intelligently captures keyboard inputs, including correct handling for **Shift key states** and **numpad keys**, and sends the logs in real-time to a private Telegram chat. The data is sent immediately after specific actions like pressing `Space`, `Enter`, or `Backspace`.


***

### ⚠️ **Disclaimer**

This tool is intended for **educational and research purposes only**. It was created to demonstrate how system-level keyboard listeners work and how data can be exfiltrated over common protocols. Using this software on any computer without the owner's explicit permission is illegal and unethical. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

***

### ⚙️ **Key Features**

- **Intelligent Shift Handling**: Correctly logs uppercase letters and symbols (e.g., `!` instead of `1`) when the Shift key is pressed.
- **Full Numpad Support**: Accurately logs numbers and symbols from the numpad.
- **Event-Triggered Reporting**: Unlike timed loggers, this script sends the captured log instantly when `Space`, `Enter`, or `Backspace` is pressed, providing immediate feedback.
- **Clean Logging**: Special keys are logged with clear labels like `[SPACE]` and `[ENTER]`.
- **Graceful Exit**: The listener can be safely stopped at any time by pressing the `Esc` key.

***

### 🚀 **Setup and Usage**

#### **1. Prerequisites**
- Python 3.8+
- A Telegram Account

#### **2. Clone the Repository**
- Clone this repository https://github.com/Devam0109/Keylogger.git
- Run python script

#### **3. Configure the Script**
You need to get a Bot Token and your Chat ID from Telegram.

Create a Bot: Talk to @BotFather on Telegram, use the /newbot command, and follow the instructions. It will give you a unique Bot Token.

Get your Chat ID: Find your new bot on Telegram and send it a message. Then, visit this URL in your browser (replace <YourBotToken> with your token): https://api.telegram.org/bot<YourBotToken>/getUpdates. Your Chat ID will be listed in the response.

#### **4. Replace in code**
Now, open key.py and replace the placeholder values with your credentials:

Telegram bot token and chat ID
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
CHAT_ID = 'YOUR_CHAT_ID_HERE'

#### **5. Run the script**
python key.py
