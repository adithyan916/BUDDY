from datetime import datetime
import os

COMMAND_LOG_FILE = "command_history.log"

def get_greeting():
    """Return a greeting based on time of day"""
    hour = datetime.now().hour
    
    if hour < 12:
        return "Good morning! How can I assist you today?"
    elif hour < 18:
        return "Good afternoon! What can I do for you?"
    else:
        return "Good evening! What do you need help with?"

def log_command(command):
    """Log user commands to a file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {command}\n"
    
    try:
        with open(COMMAND_LOG_FILE, 'a') as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Error logging command: {e}")
