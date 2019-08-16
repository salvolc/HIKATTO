import numpy as np 
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
"""
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()
"""

bspIMG = "/home/salv/Japanisch/hiragana/a.jpg"
bspIMGb = "/home/salv/Japanisch/hiragana/o.jpg"

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
#window.resize(300,600)

line = QLineEdit("Write Text")
button = QPushButton('Click')
image = QImage("Zeichen")
label = QLabel("Label")

def on_button_clicked():
	alert = QMessageBox()
	alert.setText('You clicked the button!')
	image.load(bspIMGb)
	label.setPixmap(QPixmap.fromImage(image))
	alert.exec_()

def on_line_clicked():
	alert = QMessageBox()
	alert.setText('You clicked the button!')
	image.load(bspIMGb)
	label.setPixmap(QPixmap.fromImage(image))
	alert.exec_()

button.clicked.connect(on_button_clicked)
line.returnPressed.connect(on_line_clicked)

layout.addWidget(label)
layout.addWidget(line)
layout.addWidget(button)

window.setLayout(layout)

line.selectAll()


image.load(bspIMG)
label.setPixmap(QPixmap.fromImage(image))
label.setAlignment(Qt.AlignHCenter)

window.move(500,500)
window.show()



#button.show()
#line.show()
app.exec_()