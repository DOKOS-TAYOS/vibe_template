@echo off
python -m project_name.cli test %*
exit /b %errorlevel%
