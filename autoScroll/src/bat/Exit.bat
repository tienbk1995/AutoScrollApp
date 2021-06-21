@echo off
tasklist /FI "IMAGENAME eq main.exe" | find ":" > nul
if errorlevel 1 (goto :killTask) else (goto :errorHandle)
:errorHandle
echo "Script has not run yet, run script by using Run.bat"
timeout 3
exit
:killTask
taskkill /F /IM "main.exe"
echo "Script has been killed"
timeout 3
exit