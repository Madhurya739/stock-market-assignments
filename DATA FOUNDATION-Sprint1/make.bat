@echo off
REM Simple Makefile replacement for Windows

IF "%1"=="venv" (
    python -m venv venv
    echo Virtual environment created.
)

IF "%1"=="install" (
    call venv\Scripts\activate
    pip install -r requirements.txt
    echo Libraries installed.
)

IF "%1"=="run" (
    call venv\Scripts\activate
    python main.py
)

IF "%1"=="notebook" (
    call venv\Scripts\activate
    jupyter notebook
)

IF "%1"=="clean" (
    rmdir /s /q __pycache__
    rmdir /s /q .pytest_cache
    rmdir /s /q .mypy_cache
    echo Cleaned caches.
)

IF "%1"=="freeze" (
    call venv\Scripts\activate
    pip freeze > requirements.txt
    echo Requirements updated.
)
