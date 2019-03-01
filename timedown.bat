@echo off
set /p hours="Please enter shutdown time in hours: "
set /a time=hours*60*60
timeout /t %time% /nobreak
shutdown /s
