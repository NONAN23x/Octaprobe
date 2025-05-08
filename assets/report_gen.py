from datetime import datetime
from reportlab.pdfgen import canvas 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Flowable, FrameBreak, KeepTogether, PageBreak, Spacer
from reportlab.platypus import Frame, PageTemplate, KeepInFrame
from reportlab.lib.units import cm
from reportlab.platypus import (Table, TableStyle, BaseDocTemplate)


class ReportGenerator:
    def __init__(self, filename):
        # Initialize the PDF generator
        self.title = "Report"
        self.author = "Octaprobe"
        self.filename = filename
        
        self.styleSheet = getSampleStyleSheet()

        self.text_frame = Frame(
            x1=1.5 * cm,  # From left
            y1=1.5 * cm,  # From bottom
            height=19.60 * cm,
            width=15.90 * cm,
            leftPadding=0 * cm,
            bottomPadding=0 * cm,
            rightPadding=0 * cm,
            topPadding=0 * cm,
            showBoundary=1,
            id='text_frame')

    def generate_port_scan_report(self):
        # Placeholder for port scan report generation
        filename = "Port_Scan_" + self.filename + ".pdf"
        pdf = canvas.Canvas(filename)
        pdf.setFillColorRGB(0, 0, 255)
        pdf.drawCentredString(290, 720, self.title)
        pdf.save()

    def generate_malware_analysis_report(self, data):
        # Placeholder for malware analysis report generation
        filename = "Analysis_" + self.filename + ".pdf"
        
        M = [Paragraph(str(data))]
        # M.append(KeepTogether([]))

        doc = BaseDocTemplate(filename, pagesize=letter)
        frontpage = PageTemplate(id='FrontPage',
                                 frames=[self.text_frame])
        doc.addPageTemplates(frontpage)
        doc.build(M)

    def generate_file_metadata_report(self):
        # Placeholder for file metadata report generation
        filename = "File_Metadata_" + self.filename + ".pdf"
        pdf = canvas.Canvas(filename)
        pdf.setFillColorRGB(0, 0, 255)
        pdf.drawCentredString(290, 720, self.title)
        pdf.save()

    def generate_summary_report(self):
        # Placeholder for summary report generation
        filename = "Summary_Report_" + self.filename + ".pdf"
        pdf = canvas.Canvas(filename)
        pdf.setFillColorRGB(0, 0, 255)
        pdf.drawCentredString(290, 720, self.title)
        pdf.save()
