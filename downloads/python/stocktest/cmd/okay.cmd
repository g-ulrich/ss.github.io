@echo off
TITLE OKAY 60 sec
MODE 60,30

:timeLoop
echo Okay
echo ...
timeout /t 12 > nul
echo 2
echo ...
timeout /t 12 > nul
echo 3
echo ...
timeout /t 12 > nul
echo 4
echo ...
timeout /t 12 > nul
echo 5
echo ...
timeout /t 12 > nul
goto timeLoop
