import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QLabel,QHBoxLayout,QVBoxLayout,QPushButton
from Puzzel_main import *




class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()


        self.setFixedSize(500,300)
        self.setWindowTitle("Choise")
        self.setStyleSheet("background:black")
        
        self.edit = QLineEdit()
        self.btn = QPushButton()
        self.label = QLabel()
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.label.setFixedSize(400,80)
        self.label.setStyleSheet("Border-radius:15px;border-2px solid;color:black;background:green;font-size:100pt")
        self.label.setText("Puzzle")

        self.edit.setFixedSize(475,50)
        self.edit.setStyleSheet("Border-radius:15px;border-2px solid;color:black;background:green;font-size:10pt")
        self.edit.setPlaceholderText("Enter count of row and columb from 2 to 5...")

        self.btn.setFixedSize(100,40)
        self.btn.setStyleSheet("Border-radius:15px;border-2px solid;color:black;background:blue;font-size:10pt")
        self.btn.setText("Ok")

        self.h_box.addStretch()
        self.h_box.addWidget(self.btn)
        self.h_box.addStretch()

    
        self.v_box.addWidget(self.edit)
        self.v_box.addLayout(self.h_box)
        self.v_box.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.v_box)

        self.btn.clicked.connect(self.next_page)
    
    def next_page(self):
        
        text = self.btn.text()

        try:
            # new = int(text)
            self.n = Game()
            self.close()
            self.n.show(int(text))

        except ValueError:
            self.label.setText('Enter only number from 2 to 5')



app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
        