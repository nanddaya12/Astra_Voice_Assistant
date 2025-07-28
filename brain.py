from system import execute_system_command
from web import handle_web_request
from ai import process_ai_query
import wmi


def process_command(command):
    # System commands
    if any(keyword in command for keyword in ["shutdown", "restart", "volume", "brightness", "wifi"]):
        return execute_system_command(command)

    # Web commands
    elif any(keyword in command for keyword in ["search", "open", "website"]):
        return handle_web_request(command)

    # AI features
    elif any(keyword in command for keyword in ["what is", "who is", "define"]):
        return process_ai_query(command)

    # Custom responses
    elif "hello" in command:
        return "Hello! How can I help you today?"

    return "I didn't understand that command. Try something else."


wifi = wmi.WMI().Win32_NetworkAdapter(NetConnectionID="Wi-Fi")[0]