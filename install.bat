@echo off
echo Installing Astra Voice Assistant...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo Installation complete!
echo Starting Astra...
python main.py