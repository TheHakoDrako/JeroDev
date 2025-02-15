python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
if [ -f frontend.zip ]; then
    unzip frontend.zip -d public
    rm -f frontend.zip
else
    echo "frontend.zip not found."
fi
deactivate