@echo off
REM Build and upload the adcutils package to PyPI

REM Clean previous builds
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q *.egg-info

REM Build the distribution
python -m build --wheel

REM Upload using Twine
twine upload dist/*