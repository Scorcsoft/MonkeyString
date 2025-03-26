from PyQt5.QtWidgets import QWidget, QLabel, QStackedWidget
from ScorcsoftUI.page_decrypt_encrypt import Ui_Decrypt_Encrypt


class Encrypt_Decrypt(QWidget, Ui_Decrypt_Encrypt):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox_decrypt_type.currentIndexChanged.connect(self.show_options)
        self.comboBox_encrypt_type.currentIndexChanged.connect(self.show_options)

        self.option_ui = {}

    def show_options(self):
        sender = self.sender()
        if sender:
            if sender.objectName().endswith('decrypt_type'):
                index = self.comboBox_decrypt_type.currentIndex()
                if index == 1:
                    pass

    def reset(self, width, height):
        self.plainTextEdit_result.setGeometry(10, 260, width - 212 - 20, height - 600 + 320)

    def md5_options(self):
        pass