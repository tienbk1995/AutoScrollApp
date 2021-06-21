@echo off
tasklist /FI "IMAGENAME eq main.exe" | find ":" > nul
if errorlevel 1 (goto :errorHandle) else (goto :runScript)
:errorHandle
echo "Script is already run"
timeout 3
exit
:runScript
PowerShell.exe Start-Process "C:\Users\anhhu\Desktop\VersionControl\autoScroll\src\dist\main.exe" -WindowStyle Hidden
echo "Script run successfully"
timeout 3
exit