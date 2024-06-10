import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors


def create_pdf_file(name, gross_salary, deductions, net_salary):
    try:
        print(f"Generating receipt for {name}...")
        file_name = f"receipt_{name}.pdf"

        if os.path.exists(file_name):
            os.remove(file_name)

        doc = SimpleDocTemplate(file_name, pagesize=letter)

        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        normal_style = styles['BodyText']

        title_style.fontSize = 18
        title_style.leading = 22
        title_style.alignment = 1

        custom_style = ParagraphStyle(
            'Custom',
            parent=normal_style,
            fontSize=12,
            leading=14,
            spaceAfter=14,
        )

        elements = []

        elements.append(Paragraph("Pay Receipt", title_style))
        elements.append(Spacer(1, 0.2 * inch))

        elements.append(Paragraph(f"Name: {name}", custom_style))
        elements.append(Spacer(1, 0.1 * inch))

        data = [
            ["Description", "Amount"],
            ["Gross Salary", f"${gross_salary:.2f}"],
            ["Deductions", f"${deductions:.2f}"],
            ["Net Salary", f"${net_salary:.2f}"]
        ]

        table = Table(data, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        elements.append(table)
        elements.append(Spacer(1, 0.2 * inch))

        doc.build(elements)
        print(f"Generated receipt: {file_name}")
    except Exception as e:
        print(f"Error generating receipt for {name}: {e}")
