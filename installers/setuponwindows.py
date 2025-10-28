import os
import os.path
import time
import sys
import subprocess
import winreg

def refresh_environment():
    system_env = {}
    try:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
        ) as syskey:
            i = 0
            while True:
                try:
                    name, raw_value, regtype = winreg.EnumValue(syskey, i)
                except OSError:
                    break
                i += 1

                if regtype == winreg.REG_EXPAND_SZ:
                    raw_value = os.path.expandvars(raw_value)

                system_env[name] = raw_value
    except FileNotFoundError:
        pass

    user_env = {}
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Environment"
        ) as userkey:
            i = 0
            while True:
                try:
                    name, raw_value, regtype = winreg.EnumValue(userkey, i)
                except OSError:
                    break
                i += 1

                if regtype == winreg.REG_EXPAND_SZ:
                    raw_value = os.path.expandvars(raw_value)

                user_env[name] = raw_value
    except FileNotFoundError:
        pass


    for name, value in system_env.items():
        os.environ[name] = value

    for name, value in user_env.items():
        if name.upper() == "PATH":
            system_path = system_env.get("Path") or system_env.get("PATH", "")
            combined = value + ";" + system_path if system_path else value
            os.environ["Path"] = combined
            os.environ["PATH"] = combined
        else:
            os.environ[name] = value

arguments = sys.argv

if len(arguments) == 1:
	lang = ""
elif arguments[1].lower() in ["english", "en", "anglais"]:
	lang="_en"
else:
	lang = ""

spath = r'3.10.1-env'

if not os.path.isfile("TP.ipynb"):
	st, out = subprocess.getstatusoutput('echo %USERPROFILE%')
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyenv-win', '--target', out+r'\.pyenv'])
	os.system(r'''powershell -NoProfile -Command "[Environment]::SetEnvironmentVariable('PYENV', \"$env:UserProfile\.pyenv\pyenv-win\", 'User'); [Environment]::SetEnvironmentVariable('PYENV_HOME', \"$env:UserProfile\.pyenv\pyenv-win\", 'User'); [Environment]::SetEnvironmentVariable('PYENV_ROOT', \"$env:UserProfile\.pyenv\pyenv-win\", 'User'); $sep=';'; $new = \"$env:UserProfile\.pyenv\pyenv-win\bin$sep$env:UserProfile\.pyenv\pyenv-win\shims$sep\"; [Environment]::SetEnvironmentVariable('Path', $new + [Environment]::GetEnvironmentVariable('Path','User'), 'User')"''')
	refresh_environment()


	commands = ["pyenv install 3.10.1", "pyenv shell 3.10.1"]

	for command in commands:
		os.system(command)

	subprocess.check_call([sys.executable, '-m', 'venv', spath])

	for command in [spath+r'\Scripts\activate && pyenv rehash', spath+r'\Scripts\activate && pyenv local 3.10.1']:
		os.system(command)


	status, output = subprocess.getstatusoutput("pyenv which python")

	for command in [spath+r'\Scripts\activate && '+output+"  -m pip install --upgrade pip",
					f"curl https://raw.githubusercontent.com/youneshlal/TP-world3/refs/heads/main/notebooks/TP{lang}.ipynb -o TP.ipynb",
					spath+r'\Scripts\activate && '+output+" -m pip install ipykernel pydynamo-w msvc-runtime",
					spath+r'\Scripts\activate && '+output+' -m ipykernel install --user --name pydynamo310 --display-name "Python 3.10.1(pydynamoworld3)"',
					spath+r'\Scripts\activate.bat &&'+output+' -m pip install notebook',
                    spath+r'\Scripts\activate.bat &&'+output+' -m pip uninstall hidecode',
					spath+r'\Scripts\activate.bat && '+output+' -m notebook TP.ipynb']:
		os.system(command)
else:
    status, output = subprocess.getstatusoutput("pyenv which python")
    try:
        os.system(spath+r'\Scripts\activate.bat && '+output+' -m notebook TP.ipynb')
    except:
        os.system(spath+r'\Scripts\activate.bat && '+output+' -m jupyter notebook TP.ipynb')


