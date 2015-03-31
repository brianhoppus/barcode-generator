from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39

c=canvas.Canvas("barcode_example.pdf",pagesize=A4)
barcode=code39.Extended39("1234567890",barWidth=.30*mm,barHeight=7*mm)

label_heights = {'row1': 290,
                 'row2': 260,
                 'row3': 230,
                 'row4': 200,
                 'row5': 170,
                 'row6': 140,
                 'row7': 110,
                 'row8': 80,
                 'row9': 50,
                 'row10': 20}

def draw_row(height):
  x_axis = 15
  y_axis = height
  draw_columns(x_axis, y_axis)

def draw_columns(x_axis, y_axis):
  column_count = 0

  while column_count < 3:
    c.drawString(x_axis*mm, y_axis*mm, "Fake Book: The Subtitle")
    barcode.drawOn(c,(x_axis-10)*mm,(y_axis-10)*mm)
    c.drawString((x_axis-2)*mm, (y_axis-15)*mm, "1234567890")
    c.drawString((x_axis+34)*mm, (y_axis-15)*mm, "$24.95")
    x_axis += 65
    column_count += 1

for row in label_heights:
  draw_row(label_heights[row])

# now create the actual PDF
c.showPage()
c.save()
