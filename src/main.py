import argparse
from convertor import convert_document

def main():
    parser = argparse.ArgumentParser(description="Office faylini boshqa formatga o'tkazish")
    parser.add_argument('option_method', type=str, help="Qaysi formatga o'tkazish (masalan, 'xls2pdf')")
    parser.add_argument('input_file', type=str, help="Kiritish fayli yo'li")
    parser.add_argument('output_file', type=str, help="Chiqarish fayli yo'li")
    args = parser.parse_args()

    convert_document(args.option_method, args.input_file, args.output_file)

if __name__ == '__main__':
    main()
