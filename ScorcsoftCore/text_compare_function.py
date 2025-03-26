from PyQt5.QtWidgets import QWidget
from itertools import zip_longest
from ScorcsoftUI.page_text_compare import Ui_text_compare


class TextCompare(QWidget, Ui_text_compare):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.compare)

    def reset(self, width, height):
        base_h = (height - 600) // 2
        self.textEdit_1.setGeometry(10, 10, width - 1024 + 780, base_h + 260)
        self.textEdit_2.setGeometry(10, base_h + 260 + 20, width - 1024 + 780, base_h + 260)

        self.pushButton.setGeometry((width - 1024) // 2 + 350, height - 50, 100, 40)

    def compare(self):
        source_1 = self.textEdit_1.toPlainText()
        source_2 = self.textEdit_2.toPlainText()
        result_1 = ""
        result_2 = ""

        for char1, char2 in zip_longest(source_1, source_2, fillvalue=""):
            if char1 == char2:
                result_1 += char1
                result_2 += char2
            else:
                result_1 += f'<span style="background-color: #05c803; color: #ffffff;">{char1}</span>'
                result_2 += f'<span style="background-color: #ff3c3c; color: #ffffff;">{char2}</span>'

        self.textEdit_1.setText(result_1)
        self.textEdit_2.setText(result_2)
