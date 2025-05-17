from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
def vic():
    victory = QMessageBox()
    victory.setText('ура роблокс')
    victory.exec_()



def los(): 
    lose = QMessageBox()
    lose.setText('жди докс')
    lose.exec_()
    main_win.close()


app = QApplication([])
main_win = QWidget()

question = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
rbtn1 = QRadioButton('2005')
rbtn2 = QRadioButton('2010')
rbtn3 = QRadioButton('2015')
rbtn4 = QRadioButton('2020')

V_line = QVBoxLayout()
H_line1 = QHBoxLayout()
H_line2 = QHBoxLayout()
H_line3 = QHBoxLayout()


H_line1.addWidget(question, alignment = Qt.AlignCenter)
H_line2.addWidget(rbtn1, alignment = Qt.AlignCenter)
H_line2.addWidget(rbtn2, alignment = Qt.AlignCenter)
H_line3.addWidget(rbtn3, alignment = Qt.AlignCenter)
H_line3.addWidget(rbtn4, alignment = Qt.AlignCenter)

V_line.addLayout(H_line1)
V_line.addLayout(H_line2)
V_line.addLayout(H_line3)



main_win.setWindowTitle('Конкурс от Crazy People')

main_win.setLayout(V_line)




rbtn3.clicked.connect(vic)
rbtn1.clicked.connect(los)
rbtn2.clicked.connect(los)
rbtn4.clicked.connect(los)








main_win.show()
app.exec_()