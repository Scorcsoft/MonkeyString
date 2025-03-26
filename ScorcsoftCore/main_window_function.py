import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout
from ScorcsoftUI.main_window import Ui_MainWindow
from ScorcsoftCore.about_function import AboutPage
from ScorcsoftCore.replace_file_content_function import Replace_File_Content_Page
from ScorcsoftCore.json_format_function import Json_Format
from ScorcsoftCore.encode_decode_function import Encode_Decode
from ScorcsoftCore.text_compare_function import TextCompare
from ScorcsoftCore.fast_decode_function import Fast_Decode
# from ScorcsoftCore.encrypt_decrypt_function import Encrypt_Decrypt
from ScorcsoftCore.text_deduplicate_function import Text_Deduplicate


class monkeyStringApp(QMainWindow, Ui_MainWindow):
    def __init__(self, BASE_DIR):
        super().__init__()
        self.setupUi(self)
        self.BASE_DIR = BASE_DIR

        layout = QVBoxLayout(self.centralwidget)
        layout.addWidget(self.Main_Window_Left_Menu_QListWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setStretch(0, 1)  # 让 QListWidget 充满整个布局
        self.centralwidget.setLayout(layout)
        self.set_menu_icons()

        # 模块注册开始

        self.encode_decode = Encode_Decode()
        self.Function_Main_Area.addWidget(self.encode_decode)

        self.fast_decode = Fast_Decode()
        self.Function_Main_Area.addWidget(self.fast_decode)

        # self.encrypt_decrypt = Encrypt_Decrypt()
        # self.Function_Main_Area.addWidget(self.encrypt_decrypt)

        self.text_dedulicate = Text_Deduplicate()
        self.Function_Main_Area.addWidget(self.text_dedulicate)

        self.replace_file_content = Replace_File_Content_Page()
        self.Function_Main_Area.addWidget(self.replace_file_content)

        self.about_page = AboutPage()
        self.Function_Main_Area.addWidget(self.about_page)

        self.text_compare = TextCompare()
        self.Function_Main_Area.addWidget(self.text_compare)

        self.json_format = Json_Format()
        self.Function_Main_Area.addWidget(self.json_format)

        self.page_map = {
            "关于": self.about_page,
            "批量替换文件内容": self.replace_file_content,
            "JSON 格式化": self.json_format,
            "编码与解码": self.encode_decode,
            "文本对比": self.text_compare,
            "快速解码": self.fast_decode,
            # "加密与解密": self.encrypt_decrypt
        }
        # 模块注册结束

        self.Main_Window_Left_Menu_QListWidget.currentRowChanged.connect(self.switch_page)

    def switch_page(self, index):
        item = self.Main_Window_Left_Menu_QListWidget.item(index)
        if item:
            page = self.page_map.get(item.text())
            if page:
                self.Function_Main_Area.setCurrentWidget(page)

    def set_menu_icons(self):
        icons = {
            "编码与解码": os.path.join(self.BASE_DIR, "ScorcsoftAssets", "encode_decode.png"),
            "快速解码": os.path.join(self.BASE_DIR, "ScorcsoftAssets", "fast_decode.png"),
            # "加密与解密": "ScorcsoftAssets/encrypt_decrypt.png",
            "文本去重": os.path.join(self.BASE_DIR, "ScorcsoftAssets", "text_deduplicate.png"),
            "文本对比": os.path.join(self.BASE_DIR, "ScorcsoftAssets", "text_compare.png"),
            "JSON 格式化": os.path.join(self.BASE_DIR, "ScorcsoftAssets", "json_format.png"),
            "批量替换文件内容": os.path.join(self.BASE_DIR, "ScorcsoftAssets", "replace_file_content.png"),
            # "设置": "ScorcsoftAssets/settings.png",
            "关于": os.path.join(self.BASE_DIR, "ScorcsoftAssets", "about.png"),
        }
        for index in range(self.Main_Window_Left_Menu_QListWidget.count()):
            item = self.Main_Window_Left_Menu_QListWidget.item(index)
            text = item.text()
            if text in icons:
                item.setIcon(QIcon(icons[text]))

    def resizeEvent(self, event):
        self.Main_Window_Left_Menu_QListWidget.setMinimumHeight(self.height())
        self.Function_Main_Area.setGeometry(210, 0, self.width(), self.height())

        self.about_page.reset(self.width(), self.height())
        self.json_format.reset(self.width(), self.height())
        self.encode_decode.reset(self.width(), self.height())
        self.text_compare.reset(self.width(), self.height())
        self.fast_decode.reset(self.width(), self.height())
        self.text_dedulicate.reset(self.width(), self.height())
        super().resizeEvent(event)


