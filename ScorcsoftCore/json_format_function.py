import re
import json
from PyQt5.QtWidgets import QWidget
from ScorcsoftUI.page_json_format import Ui_json_format


class Json_Format(QWidget, Ui_json_format):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_start.clicked.connect(self.json_format)

    def fix_single_quotes(self, json_str):
        try:
            result = re.sub(r"(?<!\w)'(.*?)'(?!\w)", r'"\1"', json_str)
            return result
        except:
            return json_str

    def json_format(self):
        raw_string = self.plainTextEdit_source_text.toPlainText()
        raw_string = self.fix_single_quotes(raw_string)
        try:
            result = json.loads(raw_string)
            result = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
            self.plainTextEdit_source_text.setPlainText(result)
            self.label_result.setText("这个 JSON 他没毛病！")
            self.label_result.setStyleSheet("color: #05c803")
        except json.JSONDecodeError as e:
            self.label_result.setText(f"这不是一个正确格式的JSON：{str(e)}")
            self.label_result.setStyleSheet("color: #ff3c3c")

    def reset(self, width, height):
        w = width - 212 - 20 - 12
        self.plainTextEdit_source_text.setGeometry(10, 10, w, height - 100)

        self.label_result.setGeometry(10, height - 80, 780, 16)

        x = (width - 224) // 2 - (120 // 2)
        self.pushButton_start.setGeometry(x, height - 50, 120, 40)