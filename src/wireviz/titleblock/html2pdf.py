# import pdfkit
import yaml
from datetime import datetime

with open('metadata.yml', 'r') as file:
    yaml_input = file.read()
yaml_data = yaml.safe_load(yaml_input)

with open('template.html', 'r') as file:
    html = file.read()

html = html.replace('<!-- part_title -->', yaml_data['metadata']['title'])
html = html.replace('<!-- part_number -->', yaml_data['metadata']['partno'])
html = html.replace('<!-- company -->', yaml_data['metadata']['company'])

# TODO: handle multi-page documents
html = html.replace('<!-- sheet_current -->', 'Sheet<br />1')
html = html.replace('<!-- sheet_total -->', 'of 1')

for i, (k, v) in enumerate(yaml_data['metadata']['authors'].items(), 1):
    title = k
    name = v['name']
    date = v['date'].strftime('%Y-%m-%d')
    html = html.replace(f'<!-- process_{i}_title -->', title)
    html = html.replace(f'<!-- process_{i}_name -->', name)
    html = html.replace(f'<!-- process_{i}_date -->', date)
    print(title, name, date)

for i, (k, v) in enumerate(yaml_data['metadata']['revisions'].items(), 1):
    # TODO: for more than 8 revisions, keep only the 8 most recent ones
    number = k
    changelog = v['changelog']
    name = v['name']
    date = v['date'].strftime('%Y-%m-%d')
    html = html.replace(f'<!-- rev_{i}_number -->', '{:02d}'.format(number))
    html = html.replace(f'<!-- rev_{i}_changelog -->', changelog)
    html = html.replace(f'<!-- rev_{i}_name -->', name)
    html = html.replace(f'<!-- rev_{i}_date -->', date)


with open('output.html','w') as file:
    file.write(html)

# pdfkit export

# options = {
#     'page-size': 'A4',
#     # 'dpi': 100,
#     # 'print-media-type': True,
#     'margin-top': '0mm',
#     'margin-right': '0mm',
#     'margin-bottom': '0mm',
#     'margin-left': '0mm',
#     'encoding': "UTF-8",
#     'custom-header' : [
#         ('Accept-Encoding', 'gzip')
#     ],
#     # 'no-outline': None
# }

# pdfkit.from_string(html,'html2pdf.pdf', options=options)
