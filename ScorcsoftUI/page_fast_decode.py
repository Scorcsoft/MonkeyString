# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/walter/Documents/code/monkeyString/ScorcsoftUI/page_fast_decode.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fast_Decode(object):
    def setupUi(self, Fast_Decode):
        Fast_Decode.setObjectName("Fast_Decode")
        Fast_Decode.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Fast_Decode.sizePolicy().hasHeightForWidth())
        Fast_Decode.setSizePolicy(sizePolicy)
        Fast_Decode.setMinimumSize(QtCore.QSize(800, 600))
        Fast_Decode.setMaximumSize(QtCore.QSize(8000, 16777215))
        Fast_Decode.setStyleSheet("")
        self.plainTextEdit_result = QtWidgets.QPlainTextEdit(Fast_Decode)
        self.plainTextEdit_result.setGeometry(QtCore.QRect(10, 260, 780, 320))
        self.plainTextEdit_result.setObjectName("plainTextEdit_result")
        self.label = QtWidgets.QLabel(Fast_Decode)
        self.label.setGeometry(QtCore.QRect(10, 10, 780, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Fast_Decode)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 780, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Fast_Decode)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 780, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Fast_Decode)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 780, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Fast_Decode)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 780, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_1 = QtWidgets.QLineEdit(Fast_Decode)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 40, 780, 40))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(Fast_Decode)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 160, 780, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Fast_Decode)
        QtCore.QMetaObject.connectSlotsByName(Fast_Decode)

    def retranslateUi(self, Fast_Decode):
        _translate = QtCore.QCoreApplication.translate
        Fast_Decode.setWindowTitle(_translate("Fast_Decode", "Form"))
        self.label.setText(_translate("Fast_Decode", "URL 解码"))
        self.label_2.setText(_translate("Fast_Decode", "直接将输入框中的字符串进行URL解码"))
        self.label_3.setText(_translate("Fast_Decode", "Base64 解码"))
        self.label_4.setText(_translate("Fast_Decode", "直接将输入框中的字符串进行Base64解码"))
        self.label_5.setText(_translate("Fast_Decode", "解码结果"))
