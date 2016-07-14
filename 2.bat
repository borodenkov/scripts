echo off
echo 12HC
winrs -u:Administrator -p:R0at2Yv6 -r:10.126.144.35 "c:\pflb\pjs\bin\phantomjs.exe c:\pflb\pjs\run.js %1"
echo 11HC
winrs -u:Administrator -p:R0at2Yv6 -r:10.126.144.34 "c:\pflb\pjs\bin\phantomjs.exe c:\pflb\pjs\run.js %1"