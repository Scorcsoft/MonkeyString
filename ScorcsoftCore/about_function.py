import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from ScorcsoftUI.page_about_widget import Ui_page_about


class AboutPage(QWidget, Ui_page_about):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        i = """
monkeyString(吗喽字符串)是一个吗喽🐒使用Python + PyQt5开发的吗喽专用的字符串处理工具，拥有以下功能模块帮助各位大师傅在渗透时快速处理字符串：

1. 链式编解码(类似burp suite decoder模块，多重编码的字符串可以链式解码，无需重复多次复制粘贴。)
2. 字符串加解密
3. 文本去重
4. 文本对比
5. JSON 格式化 
6. 批量替换文件内容

如果有bug或功能建议，你可以扫描上方二维码或者在 Github 中提交 Issue，被采纳建议的提供者将加入牛马名单成为牛马。
        """
        self.label_software_name.setText("吗喽字符串工具")
        self.label_version.setText("Version 1.0.1")
        self.label_Introduction.setText(i)
        self.label_company_name.setText("Scorcsoft | 天蝎软件")
        self.label_copyright.setText("Copyright © 2021-2025 Scorcsoft. All rights reserved.")

        self.label_qr_code.setPixmap(QPixmap(os.path.abspath("ScorcsoftAssets/contact.jpg")))
        self.label_qr_code.setScaledContents(True)  # 确保图片适应 QLabel

    def reset(self, width, height):
        x = (width - 224) // 2 - (120 // 2)
        self.label_qr_code.setGeometry(x, 30, 120, 120)

        self.label_software_name.setGeometry(0, 170, width - 212, 40)
        self.label_version.setGeometry(0, + 200, width - 212, 40)

        x = (width - 224) // 2 - (800 // 2)
        self.label_Introduction.setGeometry(x, 230, 800, 221)

        self.label_company_name.setGeometry(0, (height - 600) + 500, width - 212, 40)
        self.label_copyright.setGeometry(0, (height - 600) + 550, width - 212, 40)


