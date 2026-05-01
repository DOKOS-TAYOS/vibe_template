@echo off
python -m project_name.cli bootstrap %*
exit /b %errorlevel%
