@echo off
python -m project_name.cli clean %*
exit /b %errorlevel%
