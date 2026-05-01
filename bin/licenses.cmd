@echo off
python -m project_name.cli licenses %*
exit /b %errorlevel%
