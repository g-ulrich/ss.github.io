@echo off
TITLE AutoTrade
MODE 60,30

:timeLoop
echo Okay
echo ...
REM timeout /t 297 > nul
timeout /t 20 > nul
goto timeLoop
