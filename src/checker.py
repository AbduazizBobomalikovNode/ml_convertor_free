import winreg
import platform
import subprocess
import sys
import ctypes

system = platform.system()

def is_libreoffice_installed():
    try:
        # LibreOffice ning `soffice` buyrug'i mavjudligini tekshirish
        subprocess.run(["soffice", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False
    
def is_ms_office_installed():
    try:
        # Microsoft Word reestr kalitini tekshirish
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\winword.exe")
        # Kalit mavjud bo'lsa, MS Office o'rnatilgan deb hisoblanadi
        install_path = winreg.QueryValue(reg_key, None)
        print(f"MS Office joylashuvi: {install_path}")
        winreg.CloseKey(reg_key)
        return True
    except FileNotFoundError:
        return False


# Administrator huquqlarini so'rash funksiyasi
def run_as_admin():
    if not is_admin():
        print("Ogohlantirish: Bu dastur administrator huquqlari bilan ishlashi kerak.")
        # Administrator sifatida qayta ishga tushirish
        if system == "Windows":
            subprocess.run(['powershell', 'Start-Process', 'py', "winOffeceInstaller.py", '-Verb', 'runAs'])
        elif system == "Linux":
            subprocess.run(['sudo', 'apt', 'install', 'libreoffice', '-y'])
            sys.exit()
    else:
        print("Administrator huquqlari bilan dastur ishga tushirilmoqda...")

# Administrator huquqlarini tekshirish
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Asosiy funktsiya
def main_function():
    if system == "Windows":
        if not is_ms_office_installed():
            print("Microsoft Office o'rnatilmagan. Iltimos, dasturiy ta'minotni o'rnating.")
            print("yoki dastur Administrator huquqi bilan Microsoft Officeni o'rnatishga ruxsat bering.")
            run_as_admin()  # Tizimga mos tarzda administrator sifatida qayta ishga tushiradi

    elif system == "Linux":
        if not is_libreoffice_installed():
            print("LibreOffice o'rnatilmagan. Iltimos, https://www.libreoffice.org saytiga tashrif buyurib, uni o'rnating.")
            print("yoki dastur Administrator huquq bilan LibreOfficeni o'rnatishga ruxsat bering.")
            run_as_admin()  # Administrator huquqlari bilan LibreOffice ni o'rnatadi
