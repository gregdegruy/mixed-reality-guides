# Guides Generator 

An API to create Dynamics 365 Guides using Python.

## Setup

Open a terminal as an admin.

Setup python3 virtual env or source an existing on your os.

Linux
```python
sudo apt-get update
pip install virtualenv
python3 -m venv linux 
source env/linux/bin/activate 
```
Windows
```python
pip install virtualenv
python -m venv .win
env\.win\Scripts\activate.bat
```

Pull dependencies.
```bash
pip install -r requirements.txt
python __main__.py
```