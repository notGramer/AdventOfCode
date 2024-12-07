import webbrowser
import os
import subprocess

# Set volume to 50%
# subprocess.run(['powershell', '-File', 'SetVolume.ps1', '-volume', '50'])


os.environ['MY_VAR'] = 'value'
os.system('echo $MY_VAR')  # For Linux/MacOS
os.system('echo %MY_VAR%')  # For Windows


# Define the PowerShell script as a Python raw string
powershell_script = r'''
param (
    [int]$volume = 50 # Accepts volume as a percentage (0 to 100)
)

Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
public class Volume {
    [DllImport("user32.dll")]
    public static extern int SendMessageW(IntPtr hWnd, int Msg, IntPtr wParam, IntPtr lParam);
}
"@

$hwnd = 0xffff  # Handle for all windows
$WM_APPCOMMAND = 0x319
$APPCOMMAND_VOLUME_UP = 0xA0000
$APPCOMMAND_VOLUME_MUTE = 0x80000

# Mute and unmute to ensure baseline
[Volume]::SendMessageW($hwnd, $WM_APPCOMMAND, 0, $APPCOMMAND_VOLUME_MUTE)

# Adjust volume
$currentVolume = 0
while ($currentVolume -lt $volume) {
    [Volume]::SendMessageW($hwnd, $WM_APPCOMMAND, 0, $APPCOMMAND_VOLUME_UP)
    $currentVolume++
}
'''

# Pass the PowerShell script to subprocess
subprocess.run(["powershell", "-Command", powershell_script])



# Windows

# Increase Volume to 50% in PowerShell
# os.system('powershell -Command "(New-Object -ComObject SAPI.SPVoice).Volume = 50"')

# -----------------------------------------------------------------------------------------------------------------
# MAC OS

# Set volume to 100%
# os.system("osascript -e 'set volume output volume 100'")

# Increase volume by 10%
# os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")

# Decrease volume by 10%
# os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 10)'")
# -----------------------------------------------------------------------------------------------------------------

# Linux

# Increase volume by 100%
# os.system('amixer set Master 100%+')

# Decrease volume by 10%
# os.system('amixer set Master 10%-')

# Mute volume
# os.system('amixer set Master mute')

# Unmute volume
# os.system('amixer set Master unmute')

# Open the URL in the default browser
# webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")