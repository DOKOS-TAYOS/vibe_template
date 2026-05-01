@echo off
python -m project_name.cli quality %*
exit /b %errorlevel%
