How to use this script
1. Navigate to the path of "main.exe"
2. Open PowerShell or run directly
PowerShell => Run command for running task in background: Start-Process "path/to/main.exe" -WindowStyle Hidden

How to find task's PID by task name
1. Command: tasklist /FI 'IMAGENAME eq <task_name>'

How to kill process running in background
1. Open PowerShell
2. Run Command: taskkill /IM "<process_name>" /F
	(eg: taskkill /IM "main.exe" /F)
	
Build Python package
1. Install pyinstaller
2. Run command: pyinstaller -F <build_target.py>

How to run automatically
1. Navigate into ../bat/
2. Run "Run.bat" to run script
3. Run "Exit.bat" to stop running script