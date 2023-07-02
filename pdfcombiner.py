import os
import re
import PyPDF2
import pdfplumber
import shutil

pdf_dir = './pdf/'  # Directory with original PDFs
combined_dir = './pdf/combined/'  # Directory to output combined PDFs

os.makedirs(combined_dir, exist_ok=True)  # Ensure the combined directory exists

base_files = {}  # Dictionary to hold base file names and their associated PDFs

# Read each file in the directory
for file in sorted(os.listdir(pdf_dir)):
    if file.endswith(".pdf"):
        # Separate the base file name from the letter and extension
        match = re.match(r'(.*)-([a-z])\.pdf', file)
        if match:
            base, letter = match.groups()

            # Get the heading from the first line of the PDF
            with pdfplumber.open(pdf_dir + file) as pdf:
                first_page = pdf.pages[0]
                text = first_page.extract_text()
                heading = text.split('\n')[0]  # Assuming the first line of the page is the heading

            # Create a new PDF writer and add the current PDF to it
            pdf_writer = PyPDF2.PdfWriter()
            with open(pdf_dir + file, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)

                # If we've already seen this base file name, add the current PDF to it
                if base in base_files:
                    base_files[base]['pdf_writer'].add_page(page)
                    base_files[base]['toc'].append(f'{base}-{letter} - {heading}')

                # If this is a new base file name, create a new entry for it
                else:
                    base_files[base] = {'pdf_writer': pdf_writer, 'toc': [f'{base}-{letter} - {heading}']}

# Write each combined PDF to a file
for base, data in base_files.items():
    # Create a table of contents as text
    toc = '\n'.join(data['toc'])

    # Write the table of contents to a text file
    with open(combined_dir + base + '_toc.txt', 'w') as out:
        out.write(toc)

    # Write the combined PDF to a file
    with open(combined_dir + base + '.pdf', 'wb') as out:
        data['pdf_writer'].write(out)

    # Create a new directory for the base file
    new_dir = f'{pdf_dir}/{base}/'
    os.makedirs(new_dir, exist_ok=True)

    # Move the individual PDFs to the new directory
    for file in os.listdir(pdf_dir):
        if file.startswith(base) and file.endswith('.pdf'):
            shutil.move(pdf_dir + file, new_dir + file)
