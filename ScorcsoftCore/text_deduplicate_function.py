from PyQt5.QtWidgets import QWidget, QFileDialog
from ScorcsoftUI.page_text_deduplicate import Ui_page_text_deduplicate


class Text_Deduplicate(QWidget, Ui_page_text_deduplicate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.checkBox_line.setChecked(True)
        self.checkBox_line.toggled.connect(self.on_line_toggled)
        self.checkBox_char.toggled.connect(self.on_char_toggled)
        self.pushButton_source_directory_button.clicked.connect(self.select_source_file)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_save_to_file.clicked.connect(self.save_to_file)
        self.plainTextEdit_source_text.textChanged.connect(self.unselect_source_file)

    def start(self):
        if len(self.plainTextEdit_source_text.toPlainText()) == 0 and len(self.lineEdit_source_directory_input.text()) == 0:
            return

        if self.checkBox_char.isChecked():
            if len(self.plainTextEdit_source_text.toPlainText()) == 0:
                self.char_deduplicate("file")
            else:
                self.char_deduplicate("string")
        else:
            if len(self.plainTextEdit_source_text.toPlainText()) == 0:
                self.line_deduplicate("file")
            else:
                self.line_deduplicate("string")

    def select_source_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择TXT文件",  # 对话框标题
            "",  # 默认打开路径
            "文本文件 (*.txt)"  # 文件过滤器，只显示TXT文件
        )
        if file_path:
            self.plainTextEdit_source_text.disconnect()
            self.lineEdit_source_directory_input.setText(file_path)
            self.plainTextEdit_source_text.setPlainText('')
            self.plainTextEdit_source_text.textChanged.connect(self.unselect_source_file)

    def unselect_source_file(self):
        if len(self.plainTextEdit_source_text.toPlainText()) > 0:
            self.lineEdit_source_directory_input.setText('')

    def char_deduplicate(self, source):
        if source == "string":
            s = self.plainTextEdit_source_text.toPlainText()
            result = "".join(dict.fromkeys(s))
        else:
            s = ''
            path = self.lineEdit_source_directory_input.text()
            with open(path, 'r') as line:
                s += line.read()
            result = "\n".join(dict.fromkeys(s))
        self.plainTextEdit_result_text.setPlainText(result)

    def save_to_file(self):
        if len(self.plainTextEdit_result_text.toPlainText()) > 0:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Text Files (*.txt);;All Files (*)",
                                                       options=options)
            if file_path:
                result = self.plainTextEdit_result_text.toPlainText()
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(result)

    def line_deduplicate(self, source):
        if source == "string":
            s = self.plainTextEdit_source_text.toPlainText()
            lines = s.splitlines()
        else:
            path = self.lineEdit_source_directory_input.text()
            lines = []
            for line in open(path, 'r'):
                lines.append(line.strip())
        unique_lines = list(dict.fromkeys(lines))
        result = "\n".join(unique_lines)
        self.plainTextEdit_result_text.setPlainText(result)

    def on_line_toggled(self, checked):
        if checked:
            self.checkBox_char.setChecked(False)

    def on_char_toggled(self, checked):
        if checked:
            self.checkBox_line.setChecked(False)

    def reset(self, width, height):
        base_w = (width - 212 - 20) // 2
        self.lineEdit_source_directory_input.setGeometry(10, 30, base_w - 20 - 50, 30)
        self.pushButton_source_directory_button.setGeometry(base_w - 20 - 50, 27, 50, 37)

        self.plainTextEdit_source_text.setGeometry(10, 90, base_w - 20, height - 120 - 90)  # 原字符串输入框

        self.label_type_title.setGeometry(10, height - 100, base_w - 20, 20)
        self.checkBox_line.setGeometry(10, height - 70, base_w - 20, 20)
        self.checkBox_char.setGeometry(10, height - 40, base_w - 20, 20)

        self.label_result_title.setGeometry((width - 1024) // 2 + 420, 10, base_w - 20, 20)  # 结果输入框
        self.plainTextEdit_result_text.setGeometry((width-1024)//2 + 420, 30, base_w - 20, height - 120 - 30)

        self.pushButton_start.setGeometry((width - 1024) // 2 + 480, height - 75, 120, 40)
        self.pushButton_save_to_file.setGeometry((width - 1024) // 2 + 600 , height - 75, 120, 40)