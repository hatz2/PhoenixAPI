@echo off
setlocal enabledelayedexpansion

REM Load variables from .env file
for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    set %%A=%%B
)

REM Define base path to .proto files
set "PROTO_DIR=.\phoenixapi\protos"
set "PY_DIR=.\python\"

REM Change to the directory where this script is located
cd /d %~dp0

REM Activate virtual environment
call python\venv\Scripts\activate.bat

REM Change to proto directory
REM cd %PROTO_DIR%

REM Iterate over all subdirectories in .\proto
for /d %%D in (%PROTO_DIR%\*) do (
    echo Compiling files in: %%D

    REM Collect all .proto files in this subdirectory
    for %%F in (%%D\*) do (
        echo    - %%F
        python -m grpc_tools.protoc -I. --python_out=%PY_DIR% --pyi_out=%PY_DIR% --grpc_python_out=%PY_DIR% %%F

        protoc -I. --cpp_out=%CPP_DIR% --grpc_out=%CPP_DIR%  --plugin=protoc-gen-grpc=%CPP_PLUGIN_PATH% %%F  
    )
)

REM Collect all .proto files in the phoenix api dir
for %%F in (%PROTO_DIR%\*) do (
    echo    - %%F
    python -m grpc_tools.protoc -I. --python_out=%PY_DIR% --pyi_out=%PY_DIR% --grpc_python_out=%PY_DIR% %%F

    protoc -I. --cpp_out=%CPP_DIR% --grpc_out=%CPP_DIR%  --plugin=protoc-gen-grpc=%CPP_PLUGIN_PATH% %%F  
)

echo.
echo ✅ Compilation finished.
