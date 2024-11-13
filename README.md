
# Office fayl konvertori

Bu Python skripti ofis hujjatlarini (Excel, Word, PowerPoint) turli formatlarga o'zgartirish uchun kuchli yechim taqdim etadi. U PDF, HTML, XLSX, DOCX, PPTX va boshqa ko'plab formatlarni qo'llab-quvvatlaydi.

## Xususiyatlar:
- **Platformalararo qo'llab-quvvatlash**: Skript Windows va Linux tizimlarida ishlaydi.
- **Ko'p formatlarni qo'llab-quvvatlash**: Excel, Word va PowerPoint formatlari o'rtasida hujjatlarni o'zgartirish mumkin (masalan, XLS dan PDF ga, DOCX dan PDF ga, PPT dan PPTX ga).
- **Moslashtirilgan konvertatsiya usullari**: Skript LibreOffice (Linux uchun) va Microsoft Office (Windows uchun) kabi mashhur dasturlar yordamida turli hujjat formatlarini o'zgartirish imkonini beradi.
- **Log yozuvi**: Muvaffaqiyatli konvertatsiyalar va xatoliklar uchun batafsil loglar saqlanadi.
- **Buyruq satri interfeysi (CLI)**: Skriptni buyruq satridan faylni kiritish, natija faylini va kerakli formatni belgilash uchun oddiy argumentlar bilan ishlatish mumkin.

## Qo'llab-quvvatlanadigan fayl formatlari:
- **Excel**: PDF, HTML, XLS, XLSX, XLSB, CSV, ODS va boshqalar.
- **Word**: PDF, DOC, DOCX, RTF, TXT, XML, ODT va boshqalar.
- **PowerPoint**: PPTX, PPT, PPSX, PPS, ODP, XML, RTF, HTML va boshqalar.

## O'rnatish:
- **Linux uchun**: Konvertatsiya qilish uchun LibreOffice o'rnatilishi kerak.
- **Windows uchun**: Microsoft Office (Excel, Word, PowerPoint) o'rnatilishi kerak.

## Misol ishlatish:
```bash
python file_converter.py xls2pdf input.xls output.pdf
```

## Log yozuvi:
Barcha operatsiyalar `conversion_log.log` faylida qayd etiladi va kuzatish uchun ishlatiladi.

---

# Office File Converter

This Python script provides a powerful solution for converting office documents (Excel, Word, PowerPoint) into various formats. It supports a wide range of formats, including PDF, HTML, XLSX, DOCX, PPTX, and many others.

## Features:
- **Cross-platform support**: Works on both Windows and Linux systems.
- **Multiple format support**: Convert documents between Excel, Word, and PowerPoint formats (e.g., XLS to PDF, DOCX to PDF, PPT to PPTX).
- **Customizable conversion methods**: The tool handles conversions for many document formats using well-known software such as LibreOffice (for Linux) and Microsoft Office (for Windows).
- **Logging**: Detailed logs are maintained for successful conversions and error handling.
- **Command-line interface (CLI)**: Can be used directly from the command line with simple arguments for input file, output file, and desired conversion format.

## Supported File Formats:
- **Excel**: PDF, HTML, XLS, XLSX, XLSB, CSV, ODS, and more.
- **Word**: PDF, DOC, DOCX, RTF, TXT, XML, ODT, and more.
- **PowerPoint**: PPTX, PPT, PPSX, PPS, ODP, XML, RTF, HTML, and more.

## Installation:
- **On Linux**: LibreOffice must be installed to handle conversions via the command line.
- **On Windows**: Microsoft Office (Excel, Word, PowerPoint) is required for file conversions.

## Example Usage:
```bash
python file_converter.py xls2pdf input.xls output.pdf
```

## Logging:
All operations are logged into a `conversion_log.log` file for tracking and troubleshooting.
