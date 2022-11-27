Install python 3.8, pip3

Checkout repo: 
https://github.com/sidsanc/yournextmeal


Set Up venv

python3 -m venv ./
source ./bin/activate


pip3 install -r requirements.txt


If you are getting 
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate 
try: 
open /Applications/Python <local version>/Install\ Certificates.command



To run application locally:
python3  manage.py runserver
