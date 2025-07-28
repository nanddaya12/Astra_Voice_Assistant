import os
import subprocess
import ctypes
import screen_brightness_control as sbc
import wmi  # For Windows management


def execute_system_command(command):
    command = command.lower()

    # Shutdown/Restart
    if "shutdown" in command:
        os.system("shutdown /s /t 30")
        return "Shutting down in 30 seconds"

    if "restart" in command:
        os.system("shutdown /r /t 30")
        return "Restarting in 30 seconds"

    # Volume Control
    if "volume up" in command:
        for _ in range(5):
            ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)  # VK_VOLUME_UP
        return "Volume increased"

    if "volume down" in command:
        for _ in range(5):
            ctypes.windll.user32.keybd_event(0xAE, 0, 0, 0)  # VK_VOLUME_DOWN
        return "Volume decreased"

    if "mute" in command:
        ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)  # VK_VOLUME_MUTE
        return "Sound muted"

    # Brightness Control
    if "brightness" in command:
        try:
            current = sbc.get_brightness()[0]
            if "increase" in command:
                sbc.set_brightness(min(100, current + 20))
                return "Brightness increased"
            else:
                sbc.set_brightness(max(0, current - 20))
                return "Brightness decreased"
        except:
            return "Brightness control failed"

    # WiFi Control
    if "wifi" in command:
        wifi = wmi.WMI().Win32_NetworkAdapter(NetConnectionID="Wi-Fi")[0]
        if "enable" in command:
            wifi.Enable()
            return "Wi-Fi enabled"
        else:
            wifi.Disable()
            return "Wi-Fi disabled"

    return "System command not recognized"