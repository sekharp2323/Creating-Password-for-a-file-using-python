import PyPDF2

def add_password(input_file, output_file, password):
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(password)

        with open(output_file, 'wb') as output:
            pdf_writer.write(output)

if __name__ == '__main__':
    input_file = 'Two Scoops of Django 3.x (Daniel Feldroy, Audrey Feldroy) (Z-Library).pdf'
    output_file = 'output133.pdf'
    password = 'happyday'
    
    add_password(input_file, output_file, password)
