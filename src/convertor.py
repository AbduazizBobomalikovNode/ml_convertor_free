import subprocess
import platform
import win32com.client as win32
import argparse
import os
import logging

# Operatsion tizimni aniqlash
system = platform.system()

# Konvertatsiya qilish uchun qo'llab-quvvatlanadigan metodlar
Enable_methods = [
    "xls2ods", "xls2xps", "xls2xlsm", "xls2slk", "xls2dif", "xls2prn", "xls2csv", "xls2txt", "xls2xlt", "xls2xltm", "xls2xltx", 
    "xls2mhtml", "xls2mht", "xls2xml", "xls2xlsb", "xls2xlsx", "xls2html", "xls2pdf",
    "xlsx2ods", "xlsx2xps", "xlsx2xlsm", "xlsx2slk", "xlsx2dif", "xlsx2prn", "xlsx2csv", "xlsx2txt", "xlsx2xlt", "xlsx2xltm", 
    "xlsx2xltx", "xlsx2mhtml", "xlsx2mht", "xlsx2xml", "xlsx2xlsb", "xlsx2xls", "xlsx2html", "xlsx2pdf",
    "doc2xps", "doc2odt", "doc2xml", "doc2txt", "doc2rtf", "doc2docx", "doc2html", "doc2pdf",
    "docx2xps", "docx2odt", "docx2xml", "docx2txt", "docx2rtf", "docx2doc", "docx2html", "docx2pdf",
    "pptx2ppa", "pptx2ppam", "pptx2docm", "pptx2docx", "pptx2wps", "pptx2wpd", "pptx2doc", "pptx2rtf", "pptx2txt", "pptx2thmx", 
    "pptx2mhtml", "pptx2mht", "pptx2html", "pptx2htm", "pptx2xml", "pptx2odp", "pptx2potm", "pptx2pot", "pptx2potx", "pptx2ppsm", 
    "pptx2pps", "pptx2ppsx", "pptx2pptm", "pptx2ppt", "pptx2pptx",
    "ppt2ppa", "ppt2ppam", "ppt2docm", "ppt2docx", "ppt2wps", "ppt2wpd", "ppt2doc", "ppt2rtf", "ppt2txt", "ppt2thmx", "ppt2mhtml", 
    "ppt2mht", "ppt2html", "ppt2htm", "ppt2xml", "ppt2odp", "ppt2potm", "ppt2pot", "ppt2potx", "ppt2ppsm", "ppt2pps", "ppt2ppsx", 
    "ppt2pptm", "ppt2ppt", "ppt2pptx"
]

# Formatlar va ularning konvertatsiya kodlari
Format_dic = {
    "excel": ["pdf", "html", "xls", "xlsx", "xlsb", "xml", "mht", "mhtml", "xltx", "xltm", "xlt", "txt", "csv", "prn", "dif", "slk", 
              "xlsm", "xps", "ods"],
    "word": ["pdf", "html", "doc", "docx", "rtf", "txt", "xml", "odt", "xps"],
    "powerPoint": ["pptx", "ppt", "pptm", "ppsx", "pps", "ppsm", "potx", "pot", "potm", "odp", "xml", "htm", "html", "mht", "mhtml", 
                   "thmx", "txt", "rtf", "doc", "wpd", "wps", "docx", "docm", "ppam", "ppa"]
}

Format_dic_code = {
    "excel": {"pdf": 32, "html": 44, "xls": 51, "xlsx": 51, "xlsb": 50, "xml": 46, "mht": 8, "mhtml": 8, "xltx": 51, "xltm": 51, 
              "xlt": 51, "txt": 2, "csv": 6, "prn": 4, "dif": 5, "slk": 7, "xlsm": 51, "xps": 31, "ods": 24},
    "word": {"pdf": 17, "html": 8, "doc": 0, "docx": 12, "rtf": 6, "txt": 2, "xml": 11, "odt": 24, "xps": 31},
    "powerPoint": {"pptx": 12, "ppt": 1, "pptm": 13, "ppsx": 17, "pps": 4, "ppsm": 16, "potx": 19, "pot": 20, "potm": 21, "odp": 24, 
                   "xml": 27, "htm": 5, "html": 5, "mht": 8, "mhtml": 8, "thmx": 33, "txt": 2, "rtf": 6, "doc": 0, "wpd": 36, "wps": 35, 
                   "docx": 12, "docm": 13, "ppam": 18, "ppa": 19}
}

# Logging sozlamalari
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename="conversion_log.log")

def main():
    parser = argparse.ArgumentParser(description="Office faylini boshqa formatga o'tkazish")
    parser.add_argument('option', type=str, help="Qaysi formatga o'tkazish (masalan, 'xls2pdf')")
    parser.add_argument('input', type=str, help="Fayl yo'li (masalan: 'file.xls')")
    parser.add_argument('output', type=str, help="Chiqarish fayli yo'li (masalan: 'output.pdf')")
    args = parser.parse_args()

    option_method = args.option
    input_file = get_full_path(args.input)
    output_file = get_full_path(args.output)

    if not os.path.exists(input_file):
        logging.error(f"Xato: '{input_file}' fayli topilmadi.")
        print(f"Xato: '{input_file}' fayli topilmadi.")
        return

    if option_method in Enable_methods:
        from_, to_ = option_method.split("2")

        if (from_ in ["xls", "xlsx"] and to_ in Format_dic["excel"]) or (from_ in ["doc", "docx"] and to_ in Format_dic["word"]) or (from_ in ["ppt", "pptx"] and to_ in Format_dic["powerPoint"]):
            try:
                convert_document_to_any(input_file, output_file, to_)
                logging.info(f"Fayl '{input_file}' {to_} formatiga o'tkazildi: '{output_file}'")
                print(f"Fayl '{input_file}' {to_} formatiga o'tkazildi: '{output_file}'")
            except Exception as e:
                logging.error(f"Xato yuz berdi: {e}")
                print(f"Xato yuz berdi: {e}")
        else:
            logging.warning(f"Ushbu format uchun o'girish qo'llab-quvvatlanmaydi: {option_method}")
            print(f"Ushbu format uchun o'girish qo'llab-quvvatlanmaydi: {option_method}")
    else:
        logging.warning(f"Ushbu usul qo'llab-quvvatlanmaydi: {option_method}")
        print(f"Ushbu usul qo'llab-quvvatlanmaydi: {option_method}")

def convert_document_to_any(input_path, output_path, target_format):
    if system == "Windows":
        if target_format in Format_dic["excel"]:
            convert_excel_to_any(input_path, output_path, target_format)
        elif target_format in Format_dic["word"]:
            convert_word_to_any(input_path, output_path, target_format)
        elif target_format in Format_dic["powerPoint"]:
            convert_presentation_to_any(input_path, output_path, target_format)
    elif system == "Linux":
        try:
            subprocess.run(['libreoffice', '--headless', '--convert-to', target_format, input_path, '--outdir', os.path.dirname(output_path)], 
                           check=True)
            logging.info(f"Konvertatsiya muvaffaqiyatli amalga oshirildi: '{output_path}'")
            print(f"Konvertatsiya muvaffaqiyatli amalga oshirildi: '{output_path}'")
        except subprocess.CalledProcessError as e:
            logging.error(f"Linux tizimida konvertatsiya xatosi: {e}")
            print(f"Linux tizimida konvertatsiya xatosi: {e}")

def convert_excel_to_any(input_file, output_file, target_format):
    logging.debug(f"Excel faylini {target_format} formatiga o'tkazish: {input_file} -> {output_file}")
    excel = win32.Dispatch('Excel.Application')
    workbook = excel.Workbooks.Open(input_file)
    workbook.SaveAs(output_file, Format_dic_code["excel"][target_format])
    workbook.Close()
    excel.Quit()

def convert_word_to_any(input_file, output_file, target_format):
    logging.debug(f"Word faylini {target_format} formatiga o'tkazish: {input_file} -> {output_file}")
    word = win32.Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(output_file, Format_dic_code["word"][target_format])
    doc.Close()
    word.Quit()

def convert_presentation_to_any(input_file, output_file, target_format):
    logging.debug(f"PowerPoint faylini {target_format} formatiga o'tkazish: {input_file} -> {output_file}")
    ppt = win32.Dispatch('PowerPoint.Application')
    presentation = ppt.Presentations.Open(input_file)
    presentation.SaveAs(output_file, Format_dic_code["powerPoint"][target_format])
    presentation.Close()
    ppt.Quit()

def get_full_path(file_name):
    full_path = os.path.abspath(file_name)
    logging.debug(f"Faylning to'liq yo'li: {full_path}")
    return full_path

if __name__ == "__main__":
    main()
