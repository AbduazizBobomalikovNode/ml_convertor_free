import subprocess
import os
import urllib.request

# ODT ni yuklab olish URL'si
odt_url = "https://download.microsoft.com/download/2/7/A/27AF1BE6-DD20-4CB4-B154-EBAB8A7D4A7E/officedeploymenttool_18129-20030.exe"
odt_installer = "officedeploymenttool.exe"
config_path = "configuration.xml"
odt_dir = os.getcwd()  # Joriy papka

# 1. ODT ni yuklab olish
def download_odt():
    print("Yuklab olinmoqda: ODT...")
    urllib.request.urlretrieve(odt_url, odt_installer)
    print("ODT yuklab olindi!")

# 2. configuration.xml faylini yaratish
def create_config_file():
    config_content = '''<Configuration>
        <Add SourcePath="C:\\path\\to\\Office" OfficeClientEdition="64" Channel="Current">
            <Product ID="ProPlus2019Retail">
                <Language ID="en-us" />
                <ExcludeApp ID="Access" />
                <ExcludeApp ID="Outlook" />
                <ExcludeApp ID="Publisher" />
                <ExcludeApp ID="OneNote" />
            </Product>
        </Add>
        <Display Level="None" AcceptEULA="TRUE" />
    </Configuration>'''

    with open(config_path, "w") as config_file:
        config_file.write(config_content)
    print(f"{config_path} fayli yaratildi!")

# 3. ODT ni ishga tushurib, Office'ni o'rnatish
def install_office():
    # ODT ni ishga tushurish
    print("Office o'rnatilmoqda...")
    subprocess.run([odt_installer, "/configure", config_path], check=True)
    print("Office o'rnatish tugadi!")

# Asosiy funktsiyalarni chaqirish
if __name__ == "__main__":
    # 1. ODT ni yuklab olish
    download_odt()

    # 2. configuration.xml faylini yaratish
    create_config_file()

    # 3. Office o'rnatish jarayonini boshlash
    install_office()
