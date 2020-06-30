import svgwrite

white = svgwrite.rgb(255,255,255)
black = svgwrite.rgb(0,0,0)

thick = 0.35
thin = 0.18

# line height
f = 4.25
# width/height
w = 180
h = 9 * f
# vertical splits
v1 = 54
v2 = 98
v3 = w - 3 * f
# revision table
v_rev = [0, 6, 28, 44]
v_bottom = 4
v_top = 9
v_text = ['Rev','Changelog','Date','Name']
v_id = ['r','rc','rd','rn']
# check table
v_check = [72, 88]
c_text = ['Designed','Approved','Printed']
c_id = ['cd','cn']
# text offsets
ff = 'Arial'
fs = 2.8 # font small
fm = 4.0 # font medium
fl = 5.6 # font large
tx = 0.5
ty = -1.1

dwg = svgwrite.Drawing('titleblock.svg', size=(w, h), profile='tiny')

# main lines
dwg.add(dwg.rect((0,0),(w,h), fill=white, stroke=black, stroke_width=thick))
dwg.add(dwg.line((v1,0),(v1,h), stroke=black, stroke_width=thick))
dwg.add(dwg.line((v2,0),(v2,h), stroke=black, stroke_width=thick))
dwg.add(dwg.line((v1,5*f),(w,5*f), stroke=black, stroke_width=thick))
dwg.add(dwg.line((v1,8*f),(w,8*f), stroke=black, stroke_width=thick))

# revision table
for i in range(1,9):
    dwg.add(dwg.line((0,i*f),(v1,i*f), stroke=black, stroke_width=thin))
for i, v in enumerate(v_rev):
    dwg.add(dwg.line((v,0),(v,h), stroke=black, stroke_width=thin))
    dwg.add(svgwrite.text.Text(v_text[i], (v + tx, 9 * f + ty), font_family=ff,font_size=fs))
    for j in range(1,9):
        dwg.add(svgwrite.text.Text('{}{}'.format(v_id[i], 9-j), (v + tx, j * f + ty), font_family=ff,font_size=fs))
# check table
for i in range(1,5):
    dwg.add(dwg.line((v1,i*f),(v2,i*f), stroke=black, stroke_width=thin))
dwg.add(dwg.line((v_check[0],0),(v_check[0],4*f), stroke=black, stroke_width=thin))
dwg.add(dwg.line((v_check[1],0),(v_check[1],5*f), stroke=black, stroke_width=thin))

# check table
dwg.add(svgwrite.text.Text('Date', (v_check[0] + tx, 1 * f + ty), font_family=ff,font_size=fs))
dwg.add(svgwrite.text.Text('Name', (v_check[1] + tx, 1 * f + ty), font_family=ff,font_size=fs))
for i, v in enumerate(c_text):
    dwg.add(svgwrite.text.Text(v, (v1 + tx, (i+2) * f + ty), font_family=ff,font_size=fs))
    for j in range(0,2):
        dwg.add(svgwrite.text.Text('{}{}'.format(c_id[j],i), (v_check[j] + tx, (i+2) * f + ty), font_family=ff,font_size=fs))
dwg.add(svgwrite.text.Text('???', (v1 + tx, 5 * f + ty), font_family=ff,font_size=fs))
dwg.add(svgwrite.text.Text('!!!', (v_check[1] + tx, 5 * f + ty), font_family=ff,font_size=fs))

# Sheet no.
dwg.add(dwg.line((v3,5*f),(v3,8*f), stroke=black, stroke_width=thick))
dwg.add(dwg.line((v3,7*f),(w,7*f), stroke=black, stroke_width=thick))


# labels
dwg.add(svgwrite.text.Text('Part Name', (v2 + tx, 1 * f + ty), font_family=ff,font_size=fs))
dwg.add(svgwrite.text.Text('', (v2 + 2 * tx, 2 * f + 0 * 5.6), font_family=ff,font_size=fl))
dwg.add(svgwrite.text.Text('Lorem ipsum', (v2 + 2 * tx, 2 * f + 1 * 5.6), font_family=ff,font_size=fl))
dwg.add(svgwrite.text.Text('', (v2 + 2 * tx, 2 * f + 2 * 5.6), font_family=ff,font_size=fl))

dwg.add(svgwrite.text.Text('Part No.', (v2 + tx, 6 * f + ty), font_family=ff,font_size=fs))
dwg.add(svgwrite.text.Text('123-456-789', ((v2+v3)/2, 7 * f), font_family=ff,font_size=fl, text_anchor='middle'))

dwg.add(svgwrite.text.Text('Sheet', (v3 + tx, 6 * f + ty), font_family=ff,font_size=fs))
dwg.add(svgwrite.text.Text('1', ((v3+w)/2, 7 * f + ty), font_family=ff,font_size=fm, text_anchor='middle'))
dwg.add(svgwrite.text.Text('N sheets', (v3 + tx, 8 * f + ty), font_family=ff,font_size=fs))

dwg.add(svgwrite.text.Text('XXX', (v1 + tx, 9 * f + ty), font_family=ff,font_size=fs))
dwg.add(svgwrite.text.Text('YYY', (v2 + tx, 9 * f + ty), font_family=ff,font_size=fs))

dwg.save()
