How to use this script
1. Navigate to the path of "main.exe"
2. Open PowerShell or run directly
PowerShell => Run command for running task in background: Start-Process "path/to/main.exe" -WindowStyle Hidden

How to kill process running in background
1. Open PowerShell
2. Run Command: taskkill /IM "<process_name>" /F
	(eg: taskkill /IM "main.exe" /F)
	
Build Python package
1. Install pyinstaller
2. Run command: pyinstaller -F <build_target.py>