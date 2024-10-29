import datetime
import os
import sys

from PIL import Image as PILImage
from PySide6.QtCore import QCoreApplication
from reportlab.lib import colors, utils
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    Flowable,
    BaseDocTemplate,
    PageTemplate,
    Frame,
)

from kali_mc.conf import __version__, DepartmentName, DepartmentLogo_path


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


def footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    footer_text = f"Kali MC v. {__version__} -  {datetime.datetime.now()} - Hospital G. Universitario Gregorio Marañón"
    canvas.setFont("LucidaSans", 8)
    canvas.drawString(width - 14 * cm, 0.5 * cm, footer_text)
    canvas.restoreState()


def get_image(path, height=1 * cm):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return Image(path, width=height / aspect, height=height)


def create_pdf(output_path, cross_img, in_img, coronal_img, tri_img, data_dict):
    if getattr(sys, "frozen", False):
        # we are running in a bundle
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.realpath(__file__))
    # Register Lucida Sans font
    pdfmetrics.registerFont(
        TTFont("LucidaSans", os.path.join(bundle_dir, "report/LSANS.ttf"))
    )

    # Document setup
    doc = BaseDocTemplate(
        output_path,
        pagesize=A4,
        topMargin=1.0 * cm,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        bottomMargin=1.0 * cm,
        title=QCoreApplication.translate(
            "Report", "Kali MC - Informe de radioterapia intraoperatoria"
        ),
        author=DepartmentName,
    )

    # Define the Frame
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    # Define the PageTemplate with footer
    page_template = PageTemplate(id="PageWithFooter", frames=frame, onPage=footer)
    doc.addPageTemplates([page_template])

    elements = []

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="LucidaTitle",
            fontName="LucidaSans",
            fontSize=20,
            textColor=colors.HexColor("#2A82C0"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="LucidaSubtitle",
            fontName="LucidaSans",
            fontSize=16,
            textColor=colors.HexColor("#2A82C0"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="LucidaComments",
            fontName="LucidaSans",
            fontSize=14,
            textColor=colors.HexColor("#2A82C0"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="LucidaBody", fontName="LucidaSans", fontSize=10, leading=18
        )
    )

    # Add logo
    logo_path = os.path.join(bundle_dir, DepartmentLogo_path)
    logo_img = get_image(logo_path, height=0.8 * cm)
    # Add department
    department = Paragraph(DepartmentName, styles["LucidaBody"])
    header_table = Table([[logo_img, department]], colWidths=[9.5 * cm, 7.5 * cm])

    elements.append(header_table)
    elements.append(Spacer(1, 0.3 * cm))

    # Add title
    title = Paragraph(
        QCoreApplication.translate("Report", "Radioterapia Intraoperatoria"),
        styles["LucidaTitle"],
    )
    subtitle = Paragraph(
        QCoreApplication.translate("Report", "Informe de tratamiento"),
        styles["LucidaSubtitle"],
    )
    elements.append(title)
    elements.append(Spacer(1, 0.4 * cm))
    elements.append(subtitle)
    elements.append(Spacer(1, 0.5 * cm))

    # Administrative data table
    admin_data = [
        [QCoreApplication.translate("Report", "NOMBRE:"), data_dict["Name"]],
        [QCoreApplication.translate("Report", "APELLIDOS:"), data_dict["Surname"]],
        [QCoreApplication.translate("Report", "Nº DE HISTORIA:"), data_dict["ID"]],
        [QCoreApplication.translate("Report", "LOCALIZACIÓN:"), data_dict["Site"]],
        [
            QCoreApplication.translate("Report", "RADIOFÍSICO HOSPITALARIO:"),
            data_dict["Physicist"],
        ],
        [
            QCoreApplication.translate("Report", "ONCÓLOGO RADIOTERÁPICO:"),
            data_dict["Oncologist"],
        ],
        [QCoreApplication.translate("Report", "T.E.R.t:"), data_dict["TERt"]],
        [QCoreApplication.translate("Report", "Fecha:"), data_dict["Date"]],
        [QCoreApplication.translate("Report", "Nº DE RIO:"), data_dict["IORT_number"]],
    ]
    admin_table = Table(admin_data, colWidths=[6 * cm, 11 * cm])
    admin_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#2A82C0")),
                ("FONTNAME", (0, 0), (-1, -1), "LucidaSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]
        )
    )
    elements.append(admin_table)
    elements.append(Spacer(1, 0.3 * cm))

    # Prescription section
    prescription_title = RectText(
        width=17 * cm,
        height=0.8 * cm,
        text=QCoreApplication.translate("Report", "Prescripción:"),
        style=styles["LucidaSubtitle"],
    )
    elements.append(prescription_title)
    elements.append(Spacer(1, 0.1 * cm))
    prescription_data = [
        [
            QCoreApplication.translate("Report", "DIÁMETRO CONO (cm):", "UTF-8"),
            data_dict["Applicator"],
        ],
        [QCoreApplication.translate("Report", "BISEL (º):"), data_dict["Bevel"]],
        [
            QCoreApplication.translate("Report", "DOSIS PRESCRITA (cGy):"),
            data_dict["Dose"],
        ],
        [
            QCoreApplication.translate("Report", "PROF. TRATAMIENTO AL 90%:"),
            data_dict["R90"],
        ],
    ]
    presc_left_table = Table(prescription_data, colWidths=[6 * cm, 2.5 * cm])
    presc_left_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#2A82C0")),
                ("FONTNAME", (0, 0), (-1, -1), "LucidaSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0.0),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]
        )
    )
    presc_right_data = [
        [
            QCoreApplication.translate("Report", "PRESIÓN DE HOY (hPa):"),
            data_dict["Pressure"],
        ],
        [
            QCoreApplication.translate("Report", "PRESIÓN DE REFERENCIA (hPa):"),
            data_dict["RefPressure"],
        ],
    ]
    presc_right_table = Table(presc_right_data, colWidths=[5.5 * cm, 3.0 * cm])
    presc_right_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#2A82C0")),
                ("FONTNAME", (0, 0), (-1, -1), "LucidaSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0.0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]
        )
    )
    prescription_table = Table(
        [[presc_left_table, presc_right_table]], colWidths=[8.5 * cm, 8.5 * cm]
    )
    elements.append(prescription_table)
    elements.append(Spacer(1, 0.3 * cm))

    # Treatment plan section
    plan_title = RectText(
        width=17 * cm,
        height=0.8 * cm,
        text=QCoreApplication.translate("Report", "Planificación:"),
        style=styles["LucidaSubtitle"],
    )
    elements.append(plan_title)
    elements.append(Spacer(1, 0.1 * cm))
    plan_data = [
        [QCoreApplication.translate("Report", "ENERGÍA (MeV):"), data_dict["Energy"]],
        [
            QCoreApplication.translate("Report", "PROFUNDIDAD R90 (cm):"),
            data_dict["Beam_R90"],
        ],
        [QCoreApplication.translate("Report", "zmax (cm):"), data_dict["Beam_zmax"]],
        [QCoreApplication.translate("Report", "cGy/UM @ zmax:"), data_dict["Output"]],
        [
            QCoreApplication.translate("Report", "Factor de reescalado de dosis:"),
            data_dict["Rescale_factor"],
        ],
        [QCoreApplication.translate("Report", "Long. X R90 (cm):"), data_dict["R90X"]],
        [QCoreApplication.translate("Report", "Long. Y R90 (cm):"), data_dict["R90Y"]],
    ]
    plan_table = Table(plan_data, colWidths=[6 * cm, 2.5 * cm])
    plan_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#2A82C0")),
                ("FONTNAME", (0, 0), (-1, -1), "LucidaSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0.0),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]
        )
    )
    # UM section
    UM_data = [
        [QCoreApplication.translate("Report", "UM"), data_dict["UM"]],
    ]
    UM_table = Table(UM_data, colWidths=[6 * cm, 2.5 * cm])
    UM_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#2A82C0")),
                ("FONTNAME", (0, 0), (-1, -1), "LucidaSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 16),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), -0.6),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]
        )
    )
    calc2_data = [
        [QCoreApplication.translate("Report", "UM segundo cálculo:"), data_dict["UM2"]],
        [QCoreApplication.translate("Report", "Desviación (%):"), data_dict["UM_dev"]],
    ]

    calc2_table = Table(calc2_data, colWidths=[6 * cm, 2.5 * cm])
    calc2_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#2A82C0")),
                ("FONTNAME", (0, 0), (-1, -1), "LucidaSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    left_table = Table([[plan_table], [UM_table], [calc2_table]], colWidths=[8.5 * cm])

    linac_data = [
        [QCoreApplication.translate("Report", "ACELERADOR:"), data_dict["Linac"]],
        [QCoreApplication.translate("Report", "PITCH (º):"), data_dict["Pitch"]],
        [QCoreApplication.translate("Report", "ROLL (º):"), data_dict["Roll"]],
        [QCoreApplication.translate("Report", "VERTICAL (cm):"), data_dict["Vertical"]],
    ]
    linac_table = Table(linac_data, colWidths=[5.5 * cm, 3.0 * cm])
    linac_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#2A82C0")),
                ("FONTNAME", (0, 0), (-1, -1), "LucidaSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0.0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]
        )
    )

    comments = Paragraph(data_dict["Comments"])
    subtitle = Paragraph(
        QCoreApplication.translate("Report", "Incidencias"), styles["LucidaComments"]
    )
    bordered_table = Table([[subtitle], [comments]], colWidths=[8.5 * cm])
    bordered_table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.5, colors.black),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )
    right_table = Table([[linac_table], [bordered_table]])
    big_table = Table([[left_table, right_table]], colWidths=[8.5 * cm, 8.5 * cm])
    big_table.setStyle(
        TableStyle(
            [
                # ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTNAME", (0, 0), (-1, 0), "LucidaSans"),
                ("LEFTPADDING", (0, 0), (-1, 0), 0),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 0),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
            ]
        )
    )
    elements.append(big_table)
    elements.append(Spacer(1, 0.0 * cm))

    # Images
    images = [cross_img, in_img, tri_img, coronal_img]
    desired_width = 8.5 * cm  # Desired width for image

    imgs = []
    for image_path in images:
        img_width, img_height = get_image_size(image_path, desired_width)
        imgs.append(Image(image_path, width=img_width, height=img_height))

    img_table = Table(
        [[imgs[0], imgs[1]], [imgs[2], imgs[3]]], colWidths=[9 * cm, 8 * cm]
    )
    img_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#2A82C0")),
                ("FONTNAME", (0, 0), (-1, -1), "LucidaSans"),
                ("FONTSIZE", (0, 0), (-1, -1), 5),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    elements.append(img_table)
    # Build PDF
    doc.build(elements)
