from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

def build_tearsheet(company_data, filename="output/company_tearsheet.pdf"):
    """
    Generate a 2-page company tearsheet PDF.
    :param company_data: dict with keys like 'name', 'sector', 'summary', 'financials', 'kpis'
    :param filename: output PDF path
    """

    # --- Setup ---
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # --- Page 1: Company Overview ---
    title_style = styles["Title"]
    normal_style = styles["Normal"]

    story.append(Paragraph(company_data.get("name", "Company Name"), title_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph(f"Sector: {company_data.get('sector', 'N/A')}", normal_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Executive Summary", styles["Heading2"]))
    story.append(Paragraph(company_data.get("summary", "No summary available."), normal_style))
    story.append(Spacer(1, 24))

    # Financials table
    story.append(Paragraph("Key Financials", styles["Heading2"]))
    financials = company_data.get("financials", {})
    data = [["Metric", "Value"]] + [[k, v] for k, v in financials.items()]
    table = Table(data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 12),
        ("BACKGROUND", (0,1), (-1,-1), colors.beige),
    ]))
    story.append(table)

    story.append(PageBreak())

    # --- Page 2: KPIs and Analysis ---
    story.append(Paragraph("Cashflow Intelligence KPIs", styles["Heading2"]))
    kpis = company_data.get("kpis", {})
    kpi_data = [["KPI", "Value", "Interpretation"]] + [[k, v[0], v[1]] for k, v in kpis.items()]
    kpi_table = Table(kpi_data, hAlign="LEFT")
    kpi_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 12),
        ("BACKGROUND", (0,1), (-1,-1), colors.lightgrey),
    ]))
    story.append(kpi_table)

    story.append(Spacer(1, 24))
    story.append(Paragraph("Capital Allocation Pattern", styles["Heading2"]))
    story.append(Paragraph(company_data.get("capital_allocation", "N/A"), normal_style))

    # --- Build PDF ---
    doc.build(story)
