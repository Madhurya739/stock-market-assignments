from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os


def generate_tearsheet(ticker: str, company_name: str):
    """TODO: Add docstring."""
    # Ensure output directory exists
    output_dir = "reports/tearsheets"
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, f"{ticker}_tearsheet.pdf")

    # Create PDF canvas
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Page 1: Company Overview
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, f"{company_name} ({ticker})")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, "Sector: IT")
    c.drawString(50, height - 120, "Sub-sector: Software")
    c.drawString(50, height - 140, "Market Cap: LargeCap")
    c.drawString(50, height - 160, "Description: Sample company overview text...")

    c.showPage()

    # Page 2: Key Financials
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Key Financials (Latest Year)")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, "Revenue: ₹120,000 Cr")
    c.drawString(50, height - 120, "Net Income: ₹25,000 Cr")
    c.drawString(50, height - 140, "ROE: 25.3%")
    c.drawString(50, height - 160, "ROCE: 30.1%")
    c.drawString(50, height - 180, "PE Ratio: 28.5")
    c.drawString(50, height - 200, "Debt/Equity: 0.2")

    c.showPage()
    c.save()

    print(f"Tearsheet generated: {file_path}")


if __name__ == "__main__":
    # Generate one sample tearsheet for INFY
    generate_tearsheet("INFY", "Infosys")
