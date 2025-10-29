from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
import io

# ====== CONFIGURATION ======
logo_path = "naomtech_logo.png"  # path to your NaomTech logo file
footer_text = "NaomTech — Free Tech Learning Platform | Learn • Build • Grow"

# ====== CREATE WATERMARK PAGE ======
def create_watermark_page():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    width, height = A4

    # Add diagonal watermark
    can.saveState()
    can.translate(width/2, height/2)
    can.rotate(30)
    can.setFillAlpha(0.1)  # transparency
    logo = ImageReader(logo_path)
    can.drawImage(logo, -150, -150, width=300, height=300, mask='auto')
    can.restoreState()

    # Add footer
    can.setFont("Helvetica-Oblique", 10)
    can.setFillColor(colors.grey)
    can.drawCentredString(width / 2, 25, footer_text)
    can.save()

    packet.seek(0)
    return PdfReader(packet)

# ====== APPLY WATERMARK ======
def add_watermark(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    watermark = create_watermark_page().pages[0]

    for page in reader.pages:
        page.merge_page(watermark)
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"✅ Watermarked PDF created successfully: {output_pdf}")

# ====== MAIN EXECUTION ======
if __name__ == "__main__":
    input_pdf = "Python_List_Deep_Dive.pdf"   # your input file
    output_pdf = "NaomTech_ython_List_Deep_Dive.pdf"  # output file
    add_watermark(input_pdf, output_pdf)
