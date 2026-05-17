from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import textwrap


def text_to_pdf(text: str, output_file: str) -> None:
    """
    Converts the given text to a PDF file.
    
    Args:
        text (str): The text content to be converted to PDF.
        output_file (str): The path to the output PDF file.
    """
    pdf_document = canvas.Canvas(output_file, pagesize=LETTER)
    width, height = LETTER
    margin = 50
    text_object = pdf_document.beginText(margin, height - margin)
    text_object.setFont("Times-Roman", 12)

    wrapped_lines = []

    for paragraph in text.split('\n'):
        wrapped_lines.extend(textwrap.wrap(paragraph, width=80))
        wrapped_lines.append('')  # Add a blank line after each paragraph

    for line in wrapped_lines:
        text_object.textLine(line)
        if text_object.getY() < margin:  # Check if we need to start a new page
            pdf_document.drawText(text_object)
            pdf_document.showPage()
            text_object = pdf_document.beginText(margin, height - margin)
            text_object.setFont("Times-Roman", 12)
    pdf_document.drawText(text_object)
    pdf_document.save()
