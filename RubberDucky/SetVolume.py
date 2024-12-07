import subprocess

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
