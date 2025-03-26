import base64
import urllib.parse
from PyQt5.QtWidgets import QWidget
from ScorcsoftUI.page_encode_decode import Ui_Encode_Decode
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtCore import QTimer


class AutoCloseTip(QLabel):
    def __init__(self, text, timeout=2000, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setStyleSheet("background-color: yellow; padding: 10px; border-radius: 5px;")
        self.adjustSize()
        self.move(100, 100)

        # 2 秒后自动关闭
        QTimer.singleShot(timeout, self.close)
        self.show()


class Encode_Decode(QWidget, Ui_Encode_Decode):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_paste_1.clicked.connect(self.paste_text)
        self.pushButton_copy_1.clicked.connect(self.copy_text)
        self.pushButton_paste_2.clicked.connect(self.paste_text)
        self.pushButton_copy_2.clicked.connect(self.copy_text)

        self.pushButton_clear_1.clicked.connect(self.clear_input)
        self.pushButton_clear_2.clicked.connect(self.clear_input)

        self.comboBox_decode_type_1.currentIndexChanged.connect(self.decode_text)
        self.comboBox_encode_type_1.currentIndexChanged.connect(self.encode_text)
        self.comboBox_decode_type_2.currentIndexChanged.connect(self.decode_text)
        self.comboBox_encode_type_2.currentIndexChanged.connect(self.encode_text)

        self.source = self.plainTextEdit_source_text_1
        self.result = self.plainTextEdit_source_text_2
        self.encode_type = self.comboBox_encode_type_1
        self.decode_type = self.comboBox_decode_type_1
        notes = [
                 '本功能支持循环编解码，无需多次重复粘贴。例如一个多重编码字符串"614756736247387349473176626d746c6553453d"：',
                 '1. 上方输入框右侧选择Hex解码，下方输入框将出现解码结果："aGVsbG8sIG1vbmtleSE="',
                 '2. 在下方输入框右侧直接选择Base64解码，将会在上方输入框出现解码结果："hello, monkey!"',
                 '3. 如果仍然有编码，重复第1、2步操作，直到解码完成，全程无需复制粘贴。',
                 '4. 如果想要对字符串进行多重编码，也是同理。'
        ]
        self.label_note.setText("<br><br>".join(notes))

    def clear_input(self):
        sender = self.sender()
        if sender:
            if sender.objectName().endswith('_1'):
                self.plainTextEdit_source_text_1.setPlainText('')
                self.comboBox_decode_type_1.setCurrentIndex(0)
                self.comboBox_encode_type_1.setCurrentIndex(0)
            elif sender.objectName().endswith('_2'):
                self.plainTextEdit_source_text_2.setPlainText('')
                self.comboBox_encode_type_2.setCurrentIndex(0)
                self.comboBox_decode_type_2.setCurrentIndex(0)

    def reset(self, width, height):
        base_h = (height - 600) // 2
        self.plainTextEdit_source_text_1.setGeometry(10, 10, width - 1024 + 600, base_h + 200)
        self.plainTextEdit_source_text_2.setGeometry(10, base_h + 230, width - 1024 + 600, base_h + 200)

        self.pushButton_paste_1.setGeometry(width - 1024 + 616, 10, 70, 40)
        self.pushButton_copy_1.setGeometry(width - 1024 + 720, 10, 70, 40)
        self.comboBox_decode_type_1.setGeometry(width - 1024 + 622, 60, 160, 30)
        self.comboBox_encode_type_1.setGeometry(width - 1024 + 622, 110, 160, 30)
        self.pushButton_clear_1.setGeometry(width - 1024 + 616, 160, 174, 40)

        self.pushButton_paste_2.setGeometry(width - 1024 + 616, base_h + 230, 70, 40)
        self.pushButton_copy_2.setGeometry(width - 1024 + 720, base_h + 230, 70, 40)
        self.comboBox_decode_type_2.setGeometry(width - 1024 + 622, base_h + 280, 160, 30)
        self.comboBox_encode_type_2.setGeometry(width - 1024 + 622, base_h + 330, 160, 30)
        self.pushButton_clear_2.setGeometry(width - 1024 + 616, base_h + 380, 174, 40)

        self.label_note.setGeometry(20, height - 150, width - 212 - 40, 150)

    def paste_text(self):
        clipboard = QApplication.clipboard()
        sender = self.sender()
        if sender:
            if sender.objectName().endswith('_1'):
                self.plainTextEdit_source_text_1.setPlainText(clipboard.text())
            elif sender.objectName().endswith('_2'):
                self.plainTextEdit_source_text_2.setPlainText(clipboard.text())

    def copy_text(self):
        clipboard = QApplication.clipboard()
        sender = self.sender()
        if sender:
            if sender.objectName().endswith('_1'):
                text = self.plainTextEdit_source_text_1.toPlainText()
                clipboard.setText(text)
            elif sender.objectName().endswith('_2'):
                text = self.plainTextEdit_source_text_2.toPlainText()
                clipboard.setText(text)

    def decode_text(self):
        sender = self.sender()
        if sender:
            if sender.objectName() == "comboBox_decode_type_1":
                self.source = self.plainTextEdit_source_text_1
                self.result = self.plainTextEdit_source_text_2
                self.decode_type = self.comboBox_decode_type_1
            elif sender.objectName() == "comboBox_decode_type_2":
                self.source = self.plainTextEdit_source_text_2
                self.result = self.plainTextEdit_source_text_1
                self.decode_type = self.comboBox_decode_type_2

        index = self.decode_type.currentIndex()
        if index == 1:
            self.url_to_text()
            return
        if index == 2:
            self.base64_to_text()
            return
        if index == 3:
            self.unicode_to_text()
            return
        if index == 4:
            self.hex_to_text()
            return
        if index == 5:
            self.binary_to_text()
            return

    def encode_text(self):
        sender = self.sender()
        if sender:
            if sender.objectName() == "comboBox_encode_type_1":
                self.source = self.plainTextEdit_source_text_1
                self.result = self.plainTextEdit_source_text_2
                self.encode_type = self.comboBox_encode_type_1
            elif sender.objectName() == "comboBox_encode_type_2":
                self.source = self.plainTextEdit_source_text_2
                self.result = self.plainTextEdit_source_text_1
                self.encode_type = self.comboBox_encode_type_2

        index = self.encode_type.currentIndex()
        if index == 1:
            self.text_to_url()
            return
        if index == 2:
            self.text_to_base64()
            return
        if index == 3:
            self.text_to_unicode()
            return
        if index == 4:
            self.text_to_hex()
            return
        if index == 5:
            self.text_to_binary()
            return

    def url_to_text(self):
        source_text = self.source.toPlainText()
        try:
            result_text = urllib.parse.unquote(source_text)
        except Exception as e:
            result_text = f"URL解码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def base64_to_text(self):
        source_text = self.source.toPlainText()
        try:
            decoded_bytes = base64.b64decode(source_text)
            result_text = decoded_bytes.decode("utf-8")
        except Exception as e:
            result_text = f"Base64 解码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def unicode_to_text(self):
        source_text = self.source.toPlainText()
        try:
            result_text = source_text.encode().decode("unicode_escape")
        except Exception as e:
            result_text = f"Unicode 解码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def hex_to_text(self):
        source_text = self.source.toPlainText()
        try:
            result_text = bytes.fromhex(source_text).decode("utf-8")
        except Exception as e:
            result_text = f"Hex 解码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def binary_to_text(self):
        source_text = self.source.toPlainText()
        try:
            result_text = "".join(chr(int(b, 2)) for b in source_text.split())
        except Exception as e:
            result_text = f"二进制解码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def text_to_url(self):
        source_text = self.source.toPlainText()
        try:
            result_text = urllib.parse.quote(source_text)
        except Exception as e:
            result_text = f"URL 编码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def text_to_base64(self):
        source_text = self.source.toPlainText()
        try:
            encoded_bytes = base64.b64encode(source_text.encode("utf-8"))
            result_text = encoded_bytes.decode("utf-8")
        except Exception as e:
            result_text = f"Base64 编码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def text_to_unicode(self):
        source_text = self.source.toPlainText()
        try:
            result_text = source_text.encode("unicode_escape").decode("utf-8")
        except Exception as e:
            result_text = f"Unicode 编码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def text_to_hex(self):
        source_text = self.source.toPlainText()
        try:
            result_text = source_text.encode("utf-8").hex()
        except Exception as e:
            result_text = f"Hex 编码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)

    def text_to_binary(self):
        source_text = self.source.toPlainText()
        try:
            result_text = " ".join(format(ord(c), "08b") for c in source_text)
        except Exception as e:
            result_text = f"二进制编码失败！错误: {e}"
        self.result.setPlainText(result_text)
        self.encode_type.setCurrentIndex(0)
        self.decode_type.setCurrentIndex(0)
