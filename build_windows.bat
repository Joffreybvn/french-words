
:: Cleanup folders from previous build
if exist build (RMDIR /S /Q build)
if exist dist (RMDIR /S /Q dist)

:: Build
pyinstaller --noconsole run.py

:: Add extra files (not covered by pyinstaller)
xcopy /f .\config.py .\dist\run\config.py*
xcopy /f /i /e .\migrations .\dist\run\migrations
mkdir /f /i /e .\dist\run\app
xcopy /f /i /e .\app\static .\dist\run\app\static
xcopy /f /i /e .\app\templates .\dist\run\app\templates
xcopy /f /i /e .\app\translations .\dist\run\app\translations
