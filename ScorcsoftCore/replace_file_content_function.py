import os
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from ScorcsoftUI.page_replace_file_content_widget import Ui_page_replace_file_coontent


class Replace_File_Content_Page(QWidget, Ui_page_replace_file_coontent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_step_1.setText("第一步：选择原始文件路径")
        self.label_step_2.setText("第二步：选择结果文件的保存路径")
        self.label_step_3.setText("第三步：添加替换规则")
        self.label_source_text_type_descript.setText("字符串：从原文本中搜索左边输入框中的字符串并替换为右边输入框中的内容")
        self.label_status.setText("准备就绪")

        self.pushButton_source_directory_button.clicked.connect(self.select_source_directory)
        self.pushButton_result_directory_button.clicked.connect(self.select_result_directory)
        self.comboBox_source_text_type.currentIndexChanged.connect(self.select_source_text_type_changed)
        self.pushButton_start.clicked.connect(self.replace_start)

    def select_source_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "选择目录", "")
        if directory:
            self.lineEdit_source_directory_input.setText(directory)
            self.label_status.setText("已选择原文件目录")

    def select_result_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "选择目录", "")
        if directory:
            self.lineEdit_result_directory_input.setText(directory)
            self.label_status.setText("已选择结果文件保存目录")

    def select_source_text_type_changed(self):
        index = self.comboBox_source_text_type.currentIndex()
        print(index)
        if index == 0:
            self.label_source_text_type_descript.setText("字符串：从原文件中搜索左边输入框中的字符串并替换为右边输入框中的内容")
        if index == 1:
            self.label_source_text_type_descript.setText("正则表达式：从原文件中匹配左边输入框中的正则表达式并替换右边输入框中的内容")

    def replace_start(self):
        source_path = self.lineEdit_source_directory_input.text()
        if not os.path.isdir(source_path):
            QMessageBox.warning(None, "警告", "原文件目录不存在，请重新选择")
            return

        result_path = self.lineEdit_result_directory_input.text()
        if not os.path.isdir(result_path):
            QMessageBox.warning(None, "警告", "结果文件目录不存在，请重新选择或手动创建后再开始！")
            return

        if source_path == result_path:
            QMessageBox.warning(None, "警告", "原文件目录和结果文件目录不能相同！")
            return

        source_text = self.plainTextEdit_source_text.toPlainText()
        print(f"source_text:{source_text}")
        if len(source_text) < 1:
            QMessageBox.warning(None, "警告", "搜索的字符串或正则为空，请先在【左侧输入框】填写要批量替换的原字符串")
            return

        result_text = self.plainTextEdit_result_text.toPlainText()
        print(f"result_text:{result_text}")
        if len(result_text) < 1:
            QMessageBox.warning(None, "警告", "替换的字符串为空，请先在【右侧输入框】填写要批量成什么结果")
            return

