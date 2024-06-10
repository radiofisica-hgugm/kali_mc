from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, Flowable
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from PIL import Image as PILImage


def get_image_size(path, desired_width):
    with PILImage.open(path) as img:
        width, height = img.size
        aspect_ratio = height / width
        new_width = desired_width
        new_height = new_width * aspect_ratio
        return new_width, new_height


class RectText(Flowable):
    def __init__(self, width, height, text, style):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.text = text
        self.style = style

    def draw(self):
        self.canv.setFillColor(colors.HexColor("#2A82C0"))
        self.canv.rect(0, -0.2, self.width, self.height, fill=1, stroke=0)
        self.canv.setFillColor(colors.white)
        self.canv.setFont(self.style.fontName, self.style.fontSize)
        self.canv.drawString(3, self.height - self.style.fontSize - 2, self.text)


def create_pdf(output_path, cross_img, in_img, tri_img, data_dict):
    # Register Lucida Sans font
    pdfmetrics.registerFont(TTFont('LucidaSans', 'report/LSANS.ttf'))

    # Document setup
    doc = SimpleDocTemplate(output_path,
                            pagesize=A4, topMargin=1.0*cm, leftMargin=2*cm, rightMargin=2*cm, bottomMargin=1.0*cm,
                            title="Kali MC - Informe de radioterapia intraoperatoria",  # exchange with your title
                            author="Servicio de Dosimetría y Radioprotección",  # exchange with your authors name
                            )
    elements = []

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(name='LucidaTitle', fontName='LucidaSans', fontSize=20, textColor=colors.HexColor("#2A82C0")))
    styles.add(
        ParagraphStyle(name='LucidaSubtitle', fontName='LucidaSans', fontSize=16, textColor=colors.HexColor("#2A82C0")))
    styles.add(ParagraphStyle(name='LucidaBody', fontName='LucidaSans', fontSize=10, leading=18))


    # Add logo
    logo_ratio = 1200 / 151
    logo_path = 'report/logo_gregoriomaranon.png'
    logo_width = 200
    logo_height = logo_width / logo_ratio
    logo_img = Image(logo_path, width=logo_width, height=logo_height)

    # Add department
    department = Paragraph("Servicio de Dosimetría y Radioprotección", styles['LucidaBody'])
    header_table = Table([[logo_img, department]], colWidths=[8 * cm, 9 * cm])

    elements.append(header_table)
    elements.append(Spacer(1, 0.3 * cm))

    # Add title
    title = Paragraph("Radioterapia Intraoperatoria", styles['LucidaTitle'])
    subtitle = Paragraph("Informe de tratamiento", styles['LucidaSubtitle'])
    elements.append(title)
    elements.append(Spacer(1, 0.4 * cm))
    elements.append(subtitle)
    elements.append(Spacer(1, 0.5 * cm))

    # Administrative data table
    admin_data = [
        ["NOMBRE:", data_dict['Name']],
        ["APELLIDOS:", data_dict['Surname']],
        ["Nº DE HISTORIA:", data_dict['ID']],
        ["LOCALIZACIÓN:", data_dict['Site']],
        ["RADIOFÍSICO HOSPITALARIO:", data_dict['Physicist']],
        ["ONCÓLOGO RADIOTERÁPICO:", data_dict['Oncologist']],
        ["T.E.R.t:", data_dict['TERt']],
        ["Fecha:", data_dict['Date']],
        ["Nº DE RIO:", data_dict['IORT_number']]
    ]
    admin_table = Table(admin_data, colWidths=[7 * cm, 10 * cm])
    admin_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor("#2A82C0")),
        ('FONTNAME', (0, 0), (-1, -1), 'LucidaSans'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5)
    ]))
    elements.append(admin_table)
    elements.append(Spacer(1, 0.3 * cm))

    # Prescription section
    prescription_title = RectText(width=16 * cm, height=0.8 * cm, text="Prescripción:", style=styles['LucidaSubtitle'])
    elements.append(prescription_title)
    elements.append(Spacer(1, 0.3 * cm))
    prescription_data = [
        ["DIÁMETRO CONO (cm):", data_dict['Applicator']],
        ["BISEL (º):", data_dict['Bevel']],
        ["DOSIS PRESCRITA (cGy):", data_dict['Dose']],
        ["PROF. TRATAMIENTO AL 90%:", ""]
    ]
    prescription_table = Table(prescription_data, colWidths=[7 * cm, 10 * cm])
    prescription_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor("#2A82C0")),
        ('FONTNAME', (0, 0), (-1, -1), 'LucidaSans'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5)
    ]))
    elements.append(prescription_table)
    elements.append(Spacer(1, 0.3 * cm))

    # Treatment plan section
    plan_title = RectText(width=16 * cm, height=0.8 * cm, text="Planificación:", style=styles['LucidaSubtitle'])
    elements.append(plan_title)
    elements.append(Spacer(1, 0.4 * cm))
    plan_data = [
        ["ENERGÍA (MeV):", data_dict['Energy']],
        ["PROFUNDIDAD R90 (cm):", ""],
        ["zmax (cm):", ""],
        ["cGy/UM @ zmax:", data_dict['Output']],
        ["Long. X R90 (cm):", ""],
        ["Long. Y R90 (cm):", ""]
    ]
    plan_table = Table(plan_data, colWidths=[7 * cm, 10 * cm])
    plan_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor("#2A82C0")),
        ('FONTNAME', (0, 0), (-1, -1), 'LucidaSans'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5)
    ]))
    elements.append(plan_table)
    elements.append(Spacer(1, 0.1 * cm))

    # UM section
    um_title = Paragraph("UM:", styles['LucidaSubtitle'])
    elements.append(um_title)
    elements.append(Spacer(1, 0.2 * cm))
    um_data = [
        ["UM segundo cálculo:", data_dict['Energy']],
        ["Desviación (%):", ""]
    ]
    um_table = Table(um_data, colWidths=[7 * cm, 10 * cm])
    um_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor("#2A82C0")),
        ('FONTNAME', (0, 0), (-1, -1), 'LucidaSans'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5)
    ]))
    elements.append(um_table)
    elements.append(Spacer(1, 0.2 * cm))

    # Images
    images = [cross_img, in_img, tri_img, in_img]
    desired_width = 8.5 * cm  # Desired width for image

    imgs = []
    for image_path in images:
        img_width, img_height = get_image_size(image_path, desired_width)
        imgs.append(Image(image_path, width=img_width, height=img_height))

    img_table = Table([[imgs[0], imgs[1]], [imgs[2], imgs[3]]], colWidths=[9 * cm, 8 * cm])
    img_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor("#2A82C0")),
        ('FONTNAME', (0, 0), (-1, -1), 'LucidaSans'),
        ('FONTSIZE', (0, 0), (-1, -1), 5),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3)
    ]))
    elements.append(img_table)
    # Build PDF
    doc.build(elements)


