# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/walter/Documents/code/monkeyString/ScorcsoftUI/page_about_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_page_about(object):
    def setupUi(self, page_about):
        page_about.setObjectName("page_about")
        page_about.resize(800, 600)
        page_about.setMinimumSize(QtCore.QSize(800, 600))
        page_about.setMaximumSize(QtCore.QSize(8000, 16777215))
        self.label_qr_code = QtWidgets.QLabel(page_about)
        self.label_qr_code.setGeometry(QtCore.QRect(340, 30, 120, 120))
        self.label_qr_code.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qr_code.setObjectName("label_qr_code")
        self.label_software_name = QtWidgets.QLabel(page_about)
        self.label_software_name.setGeometry(QtCore.QRect(0, 170, 800, 40))
        self.label_software_name.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_software_name.setText("")
        self.label_software_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_software_name.setObjectName("label_software_name")
        self.label_company_name = QtWidgets.QLabel(page_about)
        self.label_company_name.setGeometry(QtCore.QRect(0, 500, 800, 40))
        self.label_company_name.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_company_name.setText("")
        self.label_company_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_company_name.setObjectName("label_company_name")
        self.label_version = QtWidgets.QLabel(page_about)
        self.label_version.setGeometry(QtCore.QRect(0, 200, 800, 40))
        self.label_version.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_version.setText("")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName("label_version")
        self.label_copyright = QtWidgets.QLabel(page_about)
        self.label_copyright.setGeometry(QtCore.QRect(0, 550, 800, 40))
        self.label_copyright.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_copyright.setText("")
        self.label_copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.label_copyright.setObjectName("label_copyright")
        self.label_Introduction = QtWidgets.QLabel(page_about)
        self.label_Introduction.setGeometry(QtCore.QRect(0, 230, 800, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Introduction.sizePolicy().hasHeightForWidth())
        self.label_Introduction.setSizePolicy(sizePolicy)
        self.label_Introduction.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_Introduction.setText("")
        self.label_Introduction.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_Introduction.setWordWrap(True)
        self.label_Introduction.setObjectName("label_Introduction")

        self.retranslateUi(page_about)
        QtCore.QMetaObject.connectSlotsByName(page_about)

    def retranslateUi(self, page_about):
        _translate = QtCore.QCoreApplication.translate
        page_about.setWindowTitle(_translate("page_about", "Form"))
        self.label_qr_code.setText(_translate("page_about", "QR Code"))
