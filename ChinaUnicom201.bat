@echo off
for /f "tokens=2 delims=:" %%i in ('ipconfig ^| find /i "ipv4" ^| find "172"') do set ip=%%i
set ip=%ip:~1%
curl -A "User-Agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5" -d "wlanuserip=%ip%&localIp=&basip=61.148.2.82&lpsUserName=用户名&lpsPwd=密码" -v "http://114.247.41.52:808/protalAction!portalAuth.action?" | find /i "false"
if %errorlevel%==0 pause
