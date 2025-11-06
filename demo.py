from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String, Line

# Create detailed PDF with diagram-style explanations
pdf_path = "/mnt/data/DBMS_Detailed_With_Diagrams.pdf"
styles = getSampleStyleSheet()
story = []

# Title Page
title = Paragraph("<b>DBMS Concepts & Architecture - Detailed Notes with Diagrams</b>", styles['Title'])
story.append(title)
story.append(Spacer(1, 20))

subtitle = Paragraph("Clear Explanation | Visual Diagrams | Exam Ready", styles['Heading2'])
story.append(subtitle)
story.append(Spacer(1, 30))

# Section 1 - DBMS Introduction
story.append(Paragraph("<b>1️⃣ Introduction to DBMS</b>", styles['Heading1']))
intro_text = """
A Database Management System (DBMS) is software that stores and manages databases. 
It provides functions like data retrieval, update, user access control, backup, security and integrity.
"""
story.append(Paragraph(intro_text, styles['BodyText']))
story.append(Spacer(1, 10))

# Section 2 - File System vs Database Diagram
story.append(Paragraph("<b>2️⃣ Traditional File System vs Database Approach</b>", styles['Heading1']))
story.append(Paragraph("Below is a conceptual diagram showing the difference:", styles['BodyText']))
story.append(Spacer(1, 10))

# Diagram using Drawing objects
draw = Drawing(400, 130)
draw.add(Rect(10, 60, 150, 60, strokeColor=colors.black))
draw.add(String(20, 90, "Traditional File System"))
draw.add(String(20, 75, "→ Independent files"))
draw.add(Line(160, 90, 240, 90))
draw.add(String(250, 90, "Problem:"))
draw.add(String(250, 75, "Redundancy & Inconsistency"))

draw.add(Rect(10, 0, 150, 50, strokeColor=colors.black))
draw.add(String(20, 25, "Database Approach"))
draw.add(Line(160, 25, 240, 25))
draw.add(String(250, 25, "Centralized\nData Store"))

story.append(draw)
story.append(Spacer(1, 20))

# Section 3 Data Independence Diagram
story.append(Paragraph("<b>3️⃣ 3-Level Architecture (Data Independence)</b>", styles['Heading1']))
story.append(Paragraph("Shows separation between users, logical schema, and physical storage:", styles['BodyText']))
story.append(Spacer(1, 10))

# Architecture Diagram
arch = Drawing(400, 150)
arch.add(Rect(100, 100, 200, 30, strokeColor=colors.black))
arch.add(String(120, 110, "External Level (Users Views)"))

arch.add(Rect(100, 60, 200, 30, strokeColor=colors.black))
arch.add(String(120, 70, "Conceptual Level (Logical Model)"))

arch.add(Rect(100, 20, 200, 30, strokeColor=colors.black))
arch.add(String(120, 30, "Internal Level (Physical Storage)"))

arch.add(Line(200, 100, 200, 90))
arch.add(Line(200, 60, 200, 50))

story.append(arch)
story.append(Spacer(1, 20))

# Section 4 - ER Model
story.append(PageBreak())
story.append(Paragraph("<b>4️⃣ ER Data Model</b>", styles['Heading1']))
story.append(Paragraph("ER model visually represents entities, attributes, and relationships.", styles['BodyText']))
story.append(Spacer(1, 10))

# ER Diagram Example
er = Drawing(400, 150)
er.add(Rect(40, 80, 80, 40, strokeColor=colors.black))
er.add(String(50, 100, "STUDENT"))
er.add(Rect(200, 80, 80, 40, strokeColor=colors.black))
er.add(String(215, 100, "COURSE"))
er.add(Line(120, 100, 200, 100))
er.add(String(150, 110, "ENROLLED"))

story.append(er)
story.append(Spacer(1, 20))

# Section 5 - Advantages Table
story.append(Paragraph("<b>5️⃣ Advantages of DBMS</b>", styles['Heading1']))

data = [
    ["Advantage", "Explanation"],
    ["Reduced Redundancy", "Single database removes duplicate files"],
    ["Data Security", "Authorization controls protect data"],
    ["Data Independence", "Change data storage without affecting users"],
    ["Backup & Recovery", "Automatic recovery from failure"],
    ["Multiple User Access", "Supports concurrency"]
]
table = Table(data, colWidths=[150, 250])
table.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 1, colors.black),
                           ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)]))
story.append(table)
story.append(Spacer(1, 20))

# Section 6 - Data Model Comparison
story.append(PageBreak())
story.append(Paragraph("<b>6️⃣ Comparison of Data Models</b>", styles['Heading1']))
comparison_data = [
    ["Feature", "Relational Model", "Object-Oriented Model", "Network Model"],
    ["Storage", "Tables", "Objects", "Records + Pointers"],
    ["Complex Data", "Moderate", "Excellent", "Moderate"],
    ["Ease of Use", "Very High", "Medium", "Low"],
]
cmp_table = Table(comparison_data, colWidths=[100, 100, 120, 120])
cmp_table.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 1, colors.black),
                               ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)]))
story.append(cmp_table)
story.append(Spacer(1, 20))

# Final Page Note
story.append(Paragraph("<b>✅ End of Notes</b>", styles['Heading2']))
story.append(Paragraph("This document covers DBMS architecture, ER diagrams, data models, and key comparisons with diagrams.", styles['BodyText']))

# Build PDF
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
doc.build(story)

pdf_path
