from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PIL import Image


def get_image_size(path, desired_width):
    with Image.open(path) as img:
        width, height = img.size
        aspect_ratio = height / width
        new_width = desired_width
        new_height = new_width * aspect_ratio
        return new_width, new_height


def create_pdf(output_path, cross_img, in_img):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    # Register Lucida Sans font
    pdfmetrics.registerFont(TTFont('LucidaSans', 'report/LSANS.ttf'))
    c.setFont('LucidaSans', 14)  # Set default font size

    # Define sizes in centimeters
    title_font_size = 24
    desired_width = 8.5 * cm  # Desired width for image
    padding = 1.27 * cm  # Padding in centimeters


    # Add Logo
    logo_ratio = 1200/151
    c.drawImage('report/logo_gregoriomaranon.png', padding, height - 1*cm -padding, width=200, height=200/logo_ratio, mask='auto' )

    # Add title
    text_x = padding
    text_y = height - 3.5 * cm
    # Draw title
    c.setFont('LucidaSans', title_font_size)
    # c.drawCentredString(title_x, title_y, "Sample Report Title")
    c.drawString(text_x, text_y, "Radioterapia Intraoperatoria")
    c.setFont('LucidaSans', title_font_size-4)
    c.drawString(text_x, text_y - 1 *cm, "Informe de tratamiento")

    # Reset font size for the rest of the document
    c.setFont('LucidaSans', 14)

    # Image coordinates (top-left corner)
    y_pos_img = height - 16 * cm
    positions = [
        (padding, y_pos_img),
        (2 * padding + desired_width, y_pos_img),
        (padding, height - 2 * (desired_width + padding)),
        (2 * padding + desired_width, height - 2 * (desired_width + padding)),
    ]
    images = [cross_img, in_img, cross_img, in_img]
    # Draw images with aspect ratio preserved
    for i, (x, y) in enumerate(positions):
        image_path = cross_img
        img_width, img_height = get_image_size(image_path, desired_width)
        c.drawImage(images[i], x, y - img_height + desired_width, img_width, img_height)

    # Add some text
    text_x = padding
    text_y = padding
    c.drawString(text_x, text_y, "Servicio de Dosimetría y Radioprotección")

    c.showPage()
    c.save()