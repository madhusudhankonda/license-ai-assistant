from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import markdown

def generate_pdf(markdown_text: str) -> bytes:
    """Convert markdown text to PDF using ReportLab"""
    buffer = io.BytesIO()
    
    # Create the PDF object, using BytesIO as its "file."
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Register a Unicode-compatible font
    try:
        pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSansCondensed.ttf'))
        font_name = 'DejaVu'
    except:
        font_name = 'Helvetica'  # Fallback to built-in font
    
    c.setFont(font_name, 12)
    
    # Convert markdown to plain text
    text = markdown_text.replace("#", "").replace("*", "")
    
    # Split text into lines
    y = height - 40  # Start 40 points down from top
    for line in text.split('\n'):
        if y < 40:  # Start new page if we're near the bottom
            c.showPage()
            y = height - 40
            c.setFont(font_name, 12)
        
        c.drawString(40, y, line)
        y -= 20  # Move down 20 points
    
    c.save()
    
    # Get the value of the BytesIO buffer and return it
    pdf = buffer.getvalue()
    buffer.close()
    return pdf 