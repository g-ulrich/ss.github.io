@echo off
TITLE AutoTrade
MODE 60,30
:start
for /f "delims=" %%a in ('wmic OS Get Localdatetime ^| find "."') do set DateTime=%%a
set min=%DateTime:~11,1%
set time=%DateTime:~8,2%:%DateTime:~10,2%
if %time% gtr 09:29 GOTO execute
goto start

:execute
cd C:\!STOCKS\Alpha-Vantage & test.py
echo See you soon - press any key to close.
pause > nul
exit /b