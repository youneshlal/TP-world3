import os
import os.path
import time
import sys

arguments = sys.argv

if len(arguments) == 1:
	lang = ""
elif arguments[1].lower() in ["english", "en", "anglais"]:
	lang="_en"
else:
	lang = ""


if not os.path.isfile("TP.ipynb"):
	commands = ["sudo apt update", "sudo apt install python3 && sudo apt install python3-pip -y", "sudo add-apt-repository ppa:deadsnakes/ppa -y",
				"sudo apt install python3.10-venv -y && python3.10 -m venv dnovenv",
				". dnovenv/bin/activate && python3.10 -m pip install --upgrade ipykernel jupyter jupyter_contrib_nbextensions notebook==6.4.12",
				". dnovenv/bin/activate && jupyter contrib nbextension install --user && jupyter nbextension enable exercise2/main",
				f"curl https://raw.githubusercontent.com/youneshlal/TP-world3/refs/heads/main/notebooks/TP{lang}.ipynb -o TP.ipynb"]


	for command in commands:
		os.system(command)
		time.sleep(1)

	os.system("clear && . dnovenv/bin/activate && jupyter-lab TP.ipynb --ip=0.0.0.0")
else:
	os.system(". dnovenv/bin/activate && jupyter-lab TP.ipynb --ip=0.0.0.0")