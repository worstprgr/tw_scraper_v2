Install Twint via following commands:

Inside a VENV:
pip3 install --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint

W/O VENV:
pip3 install twint
    - or -
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint

Pipenv:
pipenv install git+https://github.com/twintproject/twint.git#egg=twint

Git:
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt