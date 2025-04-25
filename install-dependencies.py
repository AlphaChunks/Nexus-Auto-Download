import subprocess
import sys

def installPackages():
    packages = ['pyautogui', 'keyboard']
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    installPackages()
