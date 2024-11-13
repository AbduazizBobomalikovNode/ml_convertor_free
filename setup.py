from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools import setup, find_packages

# README.md ni ochib, o'qib olish
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()




class PostInstallCommand(install):
    def run(self):
        try:
            from src.checker import main_function as checker
            checker()  # Bu yerda main_function()ni chaqirishingiz mumkin
        except Exception as e:
            # Barcha boshqa xatolarni ushlash uchun umumiy except
            print(f"kutibxona uchun zarur bo'lgan Office")
            print(f"dasturlarini tekshirish va o'rnatishda xatolik: {e}")
        
        install.run(self)
        

setup(
    name="ml_convertor_free",
    version="0.1.12",
    author="Bobomalikov Abduaziz",
    author_email="Abduaziz7071@gmail.com",
    description="MS Office va LibreOffice uchun konvertatsiya vositasi",
    long_description=long_description,  # To'liq tavsif
    long_description_content_type="text/markdown",  # Fayl turini markdown deb belgilash
    packages=find_packages(),
    install_requires=[
        "pywin32; platform_system=='Windows'",
        # Bu yerda sizning kutubxonangizni ishga tushirish uchun kerakli boshqa paketlarni kiritishingiz mumkin
    ],
    entry_points={
        'console_scripts': [
            'ml_convertor = src.main:main',
        ],
    },
)
