@echo off
set folder_name = %1
cd /d %~dp0

If "%1" == "" (
    echo "error"
) else (
    python create.py %folder_name%
)