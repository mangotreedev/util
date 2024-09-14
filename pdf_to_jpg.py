import os
import argparse
from pdf2image import convert_from_path

def convert_pdf_to_jpg(pdf_path):
    # Convert the PDF path to an absolute path
    pdf_path = os.path.abspath(pdf_path)

    # Extract PDF filename without extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Get the directory where the PDF is located
    pdf_directory = os.path.dirname(pdf_path)

    # Create a folder with the same name as the PDF file in the same directory
    output_folder = os.path.join(pdf_directory, pdf_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF pages to images
    pages = convert_from_path(pdf_path)

    # Save each page as a JPG file
    for i, page in enumerate(pages):
        output_filename = os.path.join(output_folder, f'page_{i + 1}.jpg')
        page.save(output_filename, 'JPEG')
        print(f'Saved {output_filename}')

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Convert PDF pages to JPG images")
    parser.add_argument('pdf_file', help="Absolute path to the PDF file to be converted")

    # Parse arguments
    args = parser.parse_args()

    # Ensure that the provided path is an absolute path
    pdf_file = os.path.abspath(args.pdf_file)

    # Convert the PDF to JPG
    convert_pdf_to_jpg(pdf_file)

if __name__ == '__main__':
    main()
