import pdfkit

options = {
    'page-size': 'A4',
    # 'dpi': 100,
    # 'print-media-type': True,
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    # 'no-outline': None
}

pdfkit.from_file('html2pdf.html','html2pdf.pdf', options=options)
