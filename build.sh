#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip -o frontend.zip -d public
rm -f frontend.zip