#!/bin/bash
source ./.venv/bin/activate
pip install -r requirements.txt
python main.py
python assistant_bot.py
