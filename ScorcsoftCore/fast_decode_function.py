import base64
import urllib.parse
from PyQt5.QtWidgets import QWidget
from ScorcsoftUI.page_fast_decode import Ui_Fast_Decode


class Fast_Decode(QWidget, Ui_Fast_Decode):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit_1.textChanged.connect(self.url_to_text)
        self.lineEdit_2.textChanged.connect(self.base64_to_text)

    def reset(self, width, height):
        self.lineEdit_1.setGeometry(10, 40, width - 212 - 20, 40)
        self.lineEdit_2.setGeometry(10, 160, width - 212 - 20, 40)
        self.plainTextEdit_result.setGeometry(10, 260, width - 212 - 20, height - 600 + 320)

    def url_to_text(self):
        source_text = self.lineEdit_1.text()
        self.lineEdit_2.disconnect()
        self.lineEdit_2.setText('')
        self.lineEdit_2.textChanged.connect(self.base64_to_text)
        try:
            result_text = urllib.parse.unquote(source_text)
        except Exception as e:
            result_text = f"URL解码失败！错误: {e}"
        self.plainTextEdit_result.setPlainText(result_text)

    def base64_to_text(self):
        source_text = self.lineEdit_2.text()
        self.lineEdit_1.disconnect()
        self.lineEdit_1.setText('')
        self.lineEdit_1.textChanged.connect(self.url_to_text)
        try:
            decoded_bytes = base64.b64decode(source_text)
            result_text = decoded_bytes.decode("utf-8")
        except Exception as e:
            result_text = f"Base64 解码失败！错误: {e}"
        self.plainTextEdit_result.setPlainText(result_text)