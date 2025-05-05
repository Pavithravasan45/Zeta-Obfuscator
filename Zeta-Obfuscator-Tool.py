# Internal filename: Zeta-Obfuscator-Tool.py

import marshal
import random
import string
import ast
import astor
import sys
import os
import datetime
import colorama
import ctypes
import tkinter as tk
from tkinter import filedialog
import shutil
import time

# Initialisation de Colorama et configuration des couleurs
colorama.init()
color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET

BEFORE = f'{red}[{white}'
AFTER = f'{red}]'
INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'

# Informations de contact (affichage uniquement, non utilisés pour une vérification)
discord_server = 'discord.gg/Denzo0dev'
github = 'github.com/BenzoXdev'
telegram = 't.me/Benzox'
instagram = 'just._.benzo'
by = 'BenzoXdev'
folder = 'Zeta-Obfuscator'
output_folder_1 = folder + '/Script-Obfuscate'
script_folder = folder + '/Script'
txt_file = folder + '/README.txt'

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

def Title(title):
    if sys.platform.startswith('win'):
        ctypes.windll.kernel32.SetConsoleTitleW(f'Zeta - Obfuscator Tool | {title}')
    elif sys.platform.startswith('linux'):
        sys.stdout.write(f'\033]2;Zeta - Obfuscator Tool | {title}\a')

def Clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('linux'):
        os.system('clear')

# Suppression de la vérification de clé, on démarre directement
Clear()
Title('Zeta Obfuscator Tool')

def ChoosePythonFile():
    try:
        print(f'{BEFORE + current_time_hour() + AFTER} {INPUT} Choisissez un fichier Python -> {reset}')
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        python_file = filedialog.askopenfilename(parent=root,
                                                  title='Zeta - Obfuscator Tool | Choisissez un fichier Python (.py)',
                                                  filetypes=[('Fichiers PYTHON', '*.py')])
    except Exception:
        python_file = input(f'{BEFORE + current_time_hour() + AFTER} {INPUT} Choisissez un fichier Python -> {reset}')
    return python_file

def random_var(used_vars, number=10):
    while True:
        rdm_var = ''.join(random.choices(string.ascii_letters, k=number))
        if rdm_var not in used_vars:
            used_vars.add(rdm_var)
            return rdm_var

def layer_1(script):
    anti_kids_code = (
        "\ntry:\n"
        "    Zeta\n"
        "    Zeta\n"
        "    _Zeta_\n"
        "except:\n"
        "    import sys\n"
        "    input(\"ERROR: Le code obfusqué a été modifié. Pour éviter une erreur, veuillez ne pas modifier le code obfusqué.\")\n"
        "    sys.exit()\n"
    )
    return anti_kids_code + script

def layer_2(script, size_1, size_2):
    used_vars = set()
    # Injection de code bidon (ajouté à la fin)
    for i in range(random.randint(size_1, size_2)):
        var_1 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_2 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_3 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_4 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_5 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_6 = random_var(used_vars, number=random.randint(size_1, size_2))
        script += (
            f'\nclass {var_1}:\n'
            f' def {var_2}({var_3}):\n'
            f'  {var_4} = {var_3}\n'
            f'  {var_5} = {var_4}\n'
            f'  return {var_5}\n'
            f' {var_3} = \'{var_6}\'\n'
            f' {var_5} = {var_2}({var_3})\n'
            f'{var_1}()\n'
        )
    # Injection de code bidon (ajouté au début)
    for i in range(random.randint(size_1, size_2)):
        var_1 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_2 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_3 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_4 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_5 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_6 = random_var(used_vars, number=random.randint(size_1, size_2))
        script = (
            f'\nclass {var_1}:\n'
            f' def {var_2}({var_3}):\n'
            f'  {var_4} = {var_3}\n'
            f'  {var_5} = {var_4}\n'
            f'  return {var_5}\n'
            f' {var_3} = \'{var_6}\'\n'
            f' {var_5} = {var_2}({var_3})\n'
            f'{var_1}()\n'
        ) + script
    return script

def layer_3(script):
    used_vars = set()
    key = random.randint(1, 10)
    var_1 = random_var(used_vars)
    var_2 = random_var(used_vars)
    var_3 = random_var(used_vars)
    obfuscated_script = ''.join(chr(ord(c) + key) for c in script)
    script = (
        f'{var_1} = {repr(obfuscated_script)}\n'
        f'{var_3} = {key}\n'
        f'{var_2} = "".join(chr(ord(c) - {var_3}) for c in {var_1})\n'
        f'exec({var_2})'
    )
    return script

def layer_4(script):
    compiled_code = marshal.dumps(compile(script, '<string>', 'exec'))
    script = f'_Zeta_ = {repr(compiled_code)}\nexec(marshal.loads(_Zeta_))'
    return script

def layer_5(script):
    chunks = [script[i:i + 1000] for i in range(0, len(script), 1000)]
    used_vars = set()
    chunk_vars = {random_var(used_vars): repr(chunk) for chunk in chunks}
    code_vars = '\n    '.join(f'{k} = {v}' for k, v in chunk_vars.items())
    vars_list = ', '.join(f"Zeta.{k}" for k in chunk_vars.keys())
    script = (
        f"\nclass Zeta:\n    {code_vars}\n\n"
        f"import marshal as Zeta\n"
        f"exec(''.join([ {vars_list} ]))"
    )
    return script

def obfuscate(script, size_1, size_2):
    script = layer_1(script)
    script = layer_2(script, size_1, size_2)
    script = layer_3(script)
    script = layer_4(script)
    script = layer_5(script)
    return script

def Zeta_Obfuscator():
    Clear()
    Title(f'By: {by}')
    # Affichage du bandeau
    print(''.join(
        f'{red}                                                                                                  \n'
        f'                                           ▒███████▒▓█████▄▄▄█████▓ ▄▄▄                                          \n'
        f'                                           ▒ ▒ ▒ ▄▀░▓█   ▀▓  ██▒ ▓▒▒████▄                                        \n'
        f'                                           ░ ▒ ▄▀▒░ ▒███  ▒ ▓██░ ▒░▒██  ▀█▄                                      \n'
        f'                                             ▄▀▒   ░▒▓█  ▄░ ▓██▓ ░ ░██▄▄▄▄██                                     \n'
        f'                                           ▒███████▒░▒████▒ ▒██▒ ░  ▓█   ▓██▒                                    \n'
        f'                                           ░▒▒ ▓░▒░▒░░ ▒░ ░ ▒ ░░    ▒▒   ▓▒█░                                    \n'
        f'                                           ░░▒ ▒ ░ ▒ ░ ░  ░   ░      ▒   ▒▒ ░                                    \n'
        f'                                           ░ ░ ░ ░ ░   ░    ░        ░   ▒                                       \n'
        f'                                             ░ ░       ░  ░              ░  ░                                    \n'
        f'\n                                                  {red}   By BenzoXdev\n'
        f'                                                  {white}╔═════════════════╗\n'
        f'                                                  {white}║ {red}Obfuscator Tool{white} ║\n'
        f'                                                  {white}╚═════════════════╝\n'
        f'{red}[{white}~{red}] Discord  : {red}[{white}{discord_server}{red}]\n'
        f'{red}[{white}~{red}] Telegram : {red}[{white}{telegram}{red}]\n'
        f'{red}[{white}~{red}] Instagram : {red}[{white}{instagram}{red}]\n'
        f'{"Zeta Obfuscator Tool"}\n'
    ))

    file_python = ChoosePythonFile()
    print('\n    '.join([
        f'    {red}[{white}1{red}] {white}Weak',
        f'{red}[{white}2{red}] {white}Medium',
        f'{red}[{white}3{red}] {white}Strong',
        f'{red}[{white}4{red}] {white}Very Strong'
    ]))

    try:
        obfuscation_force = int(input(f'{BEFORE + current_time_hour() + AFTER} {INPUT} Obfuscation Force -> {reset}'))
    except ValueError:
        print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number.')
        return

    if obfuscation_force == 1:
        size_1, size_2 = 8, 15
    elif obfuscation_force == 2:
        size_1, size_2 = 10, 25
    elif obfuscation_force == 3:
        size_1, size_2 = 30, 50
    elif obfuscation_force == 4:
        size_1, size_2 = 50, 100
    else:
        print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number.')
        return

    if '\\' in file_python:
        file_name = file_python.split('\\')[-1]
    elif '/' in file_python:
        file_name = file_python.split('/')[-1]
    else:
        file_name = file_python

    with open(file_python, 'r', encoding='utf-8') as file:
        script = file.read()

    print(f'{BEFORE + current_time_hour() + AFTER} {WAIT} Deleting previous folders..')
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    time.sleep(1)
    print(f'{BEFORE + current_time_hour() + AFTER} {INFO} The previous folders were deleted.')
    print(f'{BEFORE + current_time_hour() + AFTER} {INFO} Creating folder: {white + folder}')
    os.mkdir(folder)
    time.sleep(1)
    print(f'{BEFORE + current_time_hour() + AFTER} {INFO} Creating folder: {white + output_folder_1}')
    os.mkdir(output_folder_1)
    print(f'{BEFORE + current_time_hour() + AFTER} {INFO} Creating folder: {white + script_folder}')
    os.mkdir(script_folder)
    time.sleep(1)
    print(f'{BEFORE + current_time_hour() + AFTER} {INFO} Copying Python script to: {white + script_folder}/{file_name}')
    with open(f'{script_folder}/{file_name}', 'w', encoding='utf-8') as file:
        file.write(script)
    print(f'{BEFORE + current_time_hour() + AFTER} {WAIT} Obfuscation in progress..')
    obfuscated_script = obfuscate(script, size_1, size_2)
    with open(f'{output_folder_1}/{file_name}', 'w', encoding='utf-8') as file:
        file.write(obfuscated_script)
    print(f'{BEFORE + current_time_hour() + AFTER} {INFO} Obfuscation finished: {white + output_folder_1}/{file_name}')

while True:
    Zeta_Obfuscator()
    input(f'{BEFORE + current_time_hour() + AFTER} {INPUT} Press to continue.. ')
