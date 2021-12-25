@echo off
Title BestBuy 3080
pip install requests playsound bs4
:repeat
powershell "py BestBuy_3080.py | tee BestBuy_3080.txt -append"
:numbergen
set /a num=%random% %%11 +5
echo Waiting %num% seconds
echo.
echo.
ping -n %num% 127.0.0.1 >nul
goto repeat