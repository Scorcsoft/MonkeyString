import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase, QFont
from ScorcsoftCore.main_window_function import monkeyStringApp


if __name__ == "__main__":
    app = QApplication(sys.argv)

    font_id = QFontDatabase.addApplicationFont(os.path.abspath("ScorcsoftAssets/YaHei_Consolas_Hybrid.ttf"))
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    else:
        font_family = "Arial"
    app.setFont(QFont(font_family))
    app.setWindowIcon(QIcon(os.path.abspath("ScorcsoftAssets/monkey.ico")))

    if getattr(sys, 'frozen', False):
        BASE_DIR = sys._MEIPASS
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    window = monkeyStringApp(BASE_DIR=BASE_DIR)
    window.show()
    sys.exit(app.exec_())
