@echo off
cd /d %~dp0
for %%f in (%*) do (
    python resize_thumbnail.py %%f
)
pause
