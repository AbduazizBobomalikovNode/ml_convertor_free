from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):
        try:
            from .checker import main_function as checker
            checker()  # Bu yerda main_function()ni chaqirishingiz mumkin
        except Exception as e:
            # Barcha boshqa xatolarni ushlash uchun umumiy except
            print(f"kutibxona uchun zarur bo'lgan Office")
            print(f"dasturlarini tekshirish va o'rnatishda xatolik: {e}")
        
        install.run(self)
        

setup(
    name="ml_convertor_free",
    version="0.1",
    author="Bobomalikov Abduaziz",
    author_email="Abduaziz7071@gmail.com",
    description="MS Office va LibreOffice uchun konvertatsiya vositasi",
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
