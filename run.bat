@REM @Author: JimZhang
@REM @Date:   2019-02-25 22:19:19
@REM @Last Modified by:   JimDreamHeart
@REM Modified time: 2019-03-12 23:51:04

@echo off && setlocal enabledelayedexpansion

del log\* /q /f /s

python depend.py

cd src\

python main.py

pause