import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

# Folder path (current folder)
folder_path = "."

# Create PDF file
pdf = SimpleDocTemplate("Internship_All_Files.pdf")
elements = []

styles = getSampleStyleSheet()

# Custom style for code
code_style = ParagraphStyle(
    name='CodeStyle',
    fontName='Courier',
    fontSize=8,
    leading=10,
)

# Loop through all python files
for file in sorted(os.listdir(folder_path)):
    if file.endswith(".py") and file != "combine_all_to_pdf.py":
        
        # Add file name as heading
        elements.append(Paragraph(f"<b>{file}</b>", styles["Heading2"]))
        elements.append(Spacer(1, 0.3 * inch))
        
        # Read file content
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
            elements.append(Preformatted(code, code_style))
        
        elements.append(PageBreak())

# Build PDF
pdf.build(elements)

print("✅ PDF Created Successfully!")