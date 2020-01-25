@echo off
TITLE HISTORICAL 5 MIN SMA
MODE 60,30
:timeLoop
for /f "delims=" %%a in ('wmic OS Get Localdatetime ^| find "."') do set DateTime=%%a
set min=%DateTime:~11,1%
::echo %min%
if %min% ==5 GOTO out
if %min% ==0 GOTO out
goto timeLoop

:out
cd C:\!STOCKS\stocktest\history & SMA_EVERY_5_MINUTES.py
echo SMA saved Successfully...
timeout /t 297 > nul
GOTO :timeLoop

