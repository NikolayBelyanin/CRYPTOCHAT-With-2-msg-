# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1299, 689)
        Form.setStyleSheet("background-color: rgb(33, 97, 140);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setContentsMargins(48, -1, 53, -1)
        self.horizontalLayout_5.setSpacing(13)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.input_name_2 = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_name_2.sizePolicy().hasHeightForWidth())
        self.input_name_2.setSizePolicy(sizePolicy)
        self.input_name_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.input_name_2.setObjectName("input_name_2")
        self.horizontalLayout_5.addWidget(self.input_name_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(7, 0, 32, -1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"     border: 1px solid gray;\n"
"     border-radius: 3px;\n"
"     padding: 1px 1px 1px 1px;\n"
"     min-width: 6em;\n"
" }\n"
"\n"
"QComboBox::drop-down {\n"
"     width: 0px;\n"
"     border-left-width: 0px;\n"
" }")
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_6.addWidget(self.comboBox_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.setStretch(0, 24)
        self.horizontalLayout_4.setStretch(1, 50)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page)
        self.scrollArea_3.setStyleSheet("background-color: rgb(216, 240, 255);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 412, 613))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.addWidget(self.scrollArea_3)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page)
        self.stackedWidget_3.setStyleSheet("background-color: rgb(247, 253, 255);")
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page_8)
        self.label_8.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 2, 1, 1, 1)
        self.stackedWidget_3.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(18, -1, 4, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.page_9)
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 14, -1, 13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_9.addWidget(self.lineEdit_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(127, 10, 144, 13)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 1, 1, 2, 1)
        spacerItem6 = QtWidgets.QSpacerItem(224, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(225, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem9, 3, 1, 1, 1)
        self.stackedWidget_3.addWidget(self.page_9)
        self.horizontalLayout_3.addWidget(self.stackedWidget_3)
        self.horizontalLayout_3.setStretch(0, 24)
        self.horizontalLayout_3.setStretch(1, 50)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea.setStyleSheet("background-color: rgb(216, 240, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 412, 613))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(33, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(68, 68, 68);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.horizontalLayout_7.setStretch(0, 50)
        self.horizontalLayout_7.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.setStretch(0, 50)
        self.verticalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 24)
        self.horizontalLayout_2.setStretch(1, 50)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem10 = QtWidgets.QSpacerItem(18, 272, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem10, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(255, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem11, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 1, 1, 2, 2)
        spacerItem12 = QtWidgets.QSpacerItem(255, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem12, 2, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 272, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem13, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem14 = QtWidgets.QSpacerItem(20, 279, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem14, 0, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(254, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem15, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 1, 1, 2)
        spacerItem16 = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem16, 1, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 278, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem17, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.input_name_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.input_name_2.setPlaceholderText(_translate("Form", " Search"))
        self.label_7.setText(_translate("Form", " Hello there!"))
        self.label_8.setText(_translate("Form", "select a user to transfer \n"
"cryptocurrency"))
        self.label_10.setText(_translate("Form", "\n"
"enter the required transfer amount"))
        self.pushButton_5.setText(_translate("Form", "send"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Write your message. . ."))
        self.pushButton.setText(_translate("Form", "кнопка"))
        self.label_4.setText(_translate("Form", "здесь будет отобраджаться инфа о пользователе"))
        self.label_5.setText(_translate("Form", "запасное окно, где можно что угодно разместить"))
        self.label_6.setText(_translate("Form", "сюда добавим настройки, но пока я не знаю как мы планируем их реализовать"))
