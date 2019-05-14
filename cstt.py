# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_cstt.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from test import result
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(829, 528)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 831, 541))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(193, 255, 255);\n"
""))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.textBrowser = QtGui.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 10, 771, 51))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color: rgb(47, 206, 153);"))
        self.textBrowser.setStyleSheet(_fromUtf8("border-image: url(./green.png);"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.widget)
        self.textBrowser_3.setGeometry(QtCore.QRect(530, 80, 271, 161))
        # self.textBrowser_3.setStyleSheet(_fromUtf8("border-image: url(./green.png);"))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.widget)
        self.textBrowser_4.setGeometry(QtCore.QRect(570, 310, 201, 131))
        # self.textBrowser_4.setStyleSheet(_fromUtf8("border-image: url(./red.png);"))
        # self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(520, 450, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.textEdit_2 = QtGui.QTextEdit(self.widget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 190, 121, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(320, 150, 121, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_3 = QtGui.QTextEdit(self.widget)
        self.textEdit_3.setGeometry(QtCore.QRect(320, 310, 121, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(self.widget)
        self.textEdit_4.setGeometry(QtCore.QRect(320, 270, 121, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(self.widget)
        self.textEdit_5.setGeometry(QtCore.QRect(320, 230, 121, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(self.widget)
        self.textEdit_6.setGeometry(QtCore.QRect(320, 390, 121, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_7 = QtGui.QTextEdit(self.widget)
        self.textEdit_7.setGeometry(QtCore.QRect(320, 350, 121, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(520, 260, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(480, 70, 41, 441))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(320, 450, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
";\n"
"background-color: rgb(47, 206, 153);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(230, 150, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(220, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(230, 200, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(230, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(230, 280, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(230, 320, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(230, 360, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(230, 400, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 140, 111, 111))
        self.textBrowser_2.setAutoFillBackground(False)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_2.setStyleSheet(_fromUtf8("border-image: url(./user.png);"))
        self.line = QtGui.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(170, 70, 51, 441))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 270, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">Forecast of forest fires</span></p></body></html>", None))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        #self.label_12.setText(_translate("MainWindow", "Exact:", None))
        # self.label_11.setText(_translate("MainWindow", "Result:", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))
        self.pushButton.clicked.connect(self.getdata)
        self.label_2.setText(_translate("MainWindow", "FFMC", None))
        self.label_10.setText(_translate("MainWindow", "Fill in the box", None))
        self.label_3.setText(_translate("MainWindow", "DMC", None))
        self.label_4.setText(_translate("MainWindow", "DC", None))
        self.label_5.setText(_translate("MainWindow", "ISI", None))
        self.label_6.setText(_translate("MainWindow", "Temp", None))
        self.label_7.setText(_translate("MainWindow", "RH", None))
        self.label_8.setText(_translate("MainWindow", "Wind", None))
        self.label_9.setText(_translate("MainWindow", "Information user", None))
        # self.label.setText(_translate("MainWindow", "Name :", None))

    def getdata(self):
        # .split(QRegExp("\\D+"))[i]).toFloat()
        FFMC = self.textEdit.toPlainText()
        DMC = self.textEdit_2.toPlainText()
        DC = self.textEdit_3.toPlainText()
        ISI = self.textEdit_4.toPlainText()
        temp = self.textEdit_5.toPlainText()
        RH = self.textEdit_6.toPlainText()
        wind = self.textEdit_7.toPlainText()
        test = []
        test.append(float(FFMC))
        test.append(float(DMC))
        test.append(float(DC))
        test.append(float(ISI))
        test.append(float(temp))
        test.append(float(RH))
        test.append(float(wind))
        print(test)
        ketqua =  result(test)
        # 
        # ketqua = 2
        if ketqua == 0:
            self.textBrowser_3.setStyleSheet(_fromUtf8("border-image: url(./rung.jpg);"))
            self.textBrowser_4.setStyleSheet(_fromUtf8("border-image: url(./green.png);"))
            self.label_11.setText(_translate("MainWindow", "Result: No Dangerous ", None))
        else:
            self.textBrowser_3.setStyleSheet(_fromUtf8("border-image: url(./chayrung.jpg);"))
            self.textBrowser_4.setStyleSheet(_fromUtf8("border-image: url(./red.png);"))
            self.label_11.setText(_translate("MainWindow", "Result: Dangerous", None))
            # self.label.setText(_translate("MainWindow", "Dangerous", None))
        # return test
# import ab_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

