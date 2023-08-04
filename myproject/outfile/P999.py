import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the total number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Loop through each page and extract the text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Process the text as needed (print or store it)
            print(f"Page {page_num + 1}:")
#            print(text)
#            print("\n")

if __name__ == "__main__":
    pdf_file_path = "/home/pi/Desktop/The Python Workbook.pdf"  # Replace this with the actual path to your PDF file
    read_pdf(pdf_file_path)