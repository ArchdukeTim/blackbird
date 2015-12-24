@echo off

REM  --> Check for permissions
IF '%PROCESSOR_ARCHITECTURE%' EQU 'amd64' (
   >nul 2>&1 "%SYSTEMROOT%\SysWOW64\icacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
 ) ELSE (
   >nul 2>&1 "%SYSTEMROOT%\system32\icacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"

:test
C:\Python34\py.exe test

if errorlevel 3 (
	cls
	echo Installing Python3 prerequisite.
	if %PROCESSOR_ARCHITECTURE%==x86 (
		msiexec /qb+ /i resources\python-3.4.4.msi
	else (
		msiexec /qb+ /i resources\python-3.4.4.amd64.msi
	)
	goto test
)
if errorlevel 2 (
	echo Installing/Upgrading prerequisite Python modules
	C:\Python34\Scripts\pip.exe install colorama
	cls
	C:\Python34\py.exe SR_71.py
)


pause