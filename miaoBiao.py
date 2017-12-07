# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import sys

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

reload(sys)
sys.setdefaultencoding('utf8')

#秒表界面
class miaoBiao(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.initUi()
        self.ui=countDown()

    #定义所有组件
    def initUi(self):
        self.setObjectName(_fromUtf8("widget"))
        self.resize(439, 311)
        self.widget = QtGui.QWidget(self)
        self.widget.resize(416, 257)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_time = QtGui.QLabel(self.widget)
        self.label_time.setObjectName(_fromUtf8("label_time"))
        self.horizontalLayout.addWidget(self.label_time)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_begin = QtGui.QPushButton(self.widget)
        self.btn_begin.setObjectName(_fromUtf8("btn_begin"))
        self.horizontalLayout_2.addWidget(self.btn_begin)
        self.btn_stop = QtGui.QPushButton(self.widget)
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.horizontalLayout_2.addWidget(self.btn_stop)
        self.btn_reset = QtGui.QPushButton(self.widget)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.horizontalLayout_2.addWidget(self.btn_reset)
        self.btn_exit = QtGui.QPushButton(self.widget)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.horizontalLayout_2.addWidget(self.btn_exit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.btn_color = QtGui.QPushButton(self.widget)
        self.btn_color.setObjectName(_fromUtf8("btn_color"))
        self.horizontalLayout_5.addWidget(self.btn_color)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.btn_size = QtGui.QPushButton(self.widget)
        self.btn_size.setObjectName(_fromUtf8("btn_size"))
        self.horizontalLayout_5.addWidget(self.btn_size)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.btn_advanced = QtGui.QPushButton(self.widget)
        self.btn_advanced.setObjectName(_fromUtf8("btn_advanced"))
        self.horizontalLayout_3.addWidget(self.btn_advanced)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    #初始化组件的显示内容
    def retranslateUi(self):
        self.setWindowTitle(_translate("widget", "Python小秒表", None))
        self.label_time.setText(_translate("widget", "00:00:00", None))
        self.btn_begin.setText(_translate("widget", "Begin", None))
        self.btn_stop.setText(_translate("widget", "Stop", None))
        self.btn_reset.setText(_translate("widget", "Reset", None))
        self.btn_exit.setText(_translate("widget", "Exit", None))
        self.btn_color.setText(_translate("widget", "COLOR", None))
        self.btn_size.setText(_translate("widget", "SIZE", None))
        self.btn_advanced.setText(_translate("widget", "Advanced", None))

        self.label_time.setStyleSheet(_fromUtf8("font: 24pt \"微软雅黑\";\n"
                                             ""))
        #设置按钮的监听函数
        self.btn_begin.clicked.connect(self.beginTime)
        self.btn_stop.clicked.connect(self.stopTime)
        self.btn_reset.clicked.connect(self.resetTime)
        self.btn_exit.clicked.connect(self.exitTime)
        self.btn_advanced.clicked.connect(self.advancedTime)
        self.btn_size.clicked.connect(self.sizeTime)
        self.btn_color.clicked.connect(self.colorTime)

        # 利用一个定时器来每秒更新
        self.timerSecond = QTimer(self)
        self.timerSecond.timeout.connect(self.updateSecond)

        self.hour = 1
        self.minute = 2
        self.second = 15

    #监听键盘输入，按ESC键退出计时程序
    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()

    #开始计时，或恢复计时
    def beginTime(self):
        self.timerSecond.start(1000)

    #停止计时
    def stopTime(self):
        self.timerSecond.stop()

    #重置计时，时分秒都重置为0
    def resetTime(self):
        self.label_time.setText("00:00:00")
        self.timerSecond.stop()

        self.hour=0
        self.minute = 0
        self.second = 0

    #退出计时程序
    def exitTime(self):
        self.close()

    #设置时间数字的显示大小
    def sizeTime(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label_time.setFont(font)

    #设置时间数字的显示颜色
    def colorTime(self):
        color = QtGui.QColorDialog.getColor()  # 创建颜色选择对话框
        if color.isValid():
            # self.ui.label_title.setText(color.name())
            self.mycolor = "color:" + str(color.name())
            self.label_time.setStyleSheet(self.mycolor)

    #每秒更新时间显示
    def updateSecond(self):
            self.second = self.second + 1

            if self.second==60:
                self.second=0

                if self.minute  < 60:

                    self.minute=self.minute+1

                if self.minute==60:
                    self.minute=0
                    self.hour=self.hour+1




            if self.hour < 10:
                hourStr = "0" + str(self.hour)
            else:
                hourStr = str(self.hour)

            if self.minute < 10:
                minuteStr = "0" + str(self.minute)
            else:
                minuteStr = str(self.minute)
            if self.second < 10:
                secondStr = "0" + str(self.second)
            else:
                secondStr = str(self.second)

            strTime = hourStr + ":" + minuteStr + ":" + secondStr
            self.label_time.setText(strTime)

            return

    #转到高级功能
    def advancedTime(self):
        self.close()
        self.ui.show()

#倒计时界面
class countDown(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.initUi()
        self.ui = countDownShow()

    def initUi(self):
        self.setObjectName(_fromUtf8("Form"))
        self.resize(403, 300)
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 50, 261, 175))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_h = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_h.setObjectName(_fromUtf8("lineEdit_h"))
        self.horizontalLayout.addWidget(self.lineEdit_h)
        self.label_h = QtGui.QLabel(self.layoutWidget)
        self.label_h.setObjectName(_fromUtf8("label_h"))
        self.horizontalLayout.addWidget(self.label_h)
        self.lineEdit_m = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_m.setObjectName(_fromUtf8("lineEdit_m"))
        self.horizontalLayout.addWidget(self.lineEdit_m)
        self.label_m = QtGui.QLabel(self.layoutWidget)
        self.label_m.setObjectName(_fromUtf8("label_m"))
        self.horizontalLayout.addWidget(self.label_m)
        self.lineEdit_s = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_s.setObjectName(_fromUtf8("lineEdit_s"))
        self.horizontalLayout.addWidget(self.lineEdit_s)
        self.label_s = QtGui.QLabel(self.layoutWidget)
        self.label_s.setObjectName(_fromUtf8("label_s"))
        self.horizontalLayout.addWidget(self.label_s)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_fullsreen = QtGui.QLabel(self.layoutWidget)
        self.label_fullsreen.setObjectName(_fromUtf8("label_fullsreen"))
        self.horizontalLayout_2.addWidget(self.label_fullsreen)
        self.radioBtn_fullscreen = QtGui.QRadioButton(self.layoutWidget)
        self.radioBtn_fullscreen.setText(_fromUtf8(""))
        self.radioBtn_fullscreen.setObjectName(_fromUtf8("radioBtn_fullscreen"))
        self.horizontalLayout_2.addWidget(self.radioBtn_fullscreen)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.btn_begin = QtGui.QPushButton(self.layoutWidget)
        self.btn_begin.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.btn_begin)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Form", "Python小秒表-倒计时", None))
        self.label_h.setText(_translate("Form", "H", None))
        self.label_m.setText(_translate("Form", "M", None))
        self.label_s.setText(_translate("Form", "S", None))
        self.label_fullsreen.setText(_translate("Form", "FullScreen", None))
        self.btn_begin.setText(_translate("Form", "Begin", None))

        self.btn_begin.clicked.connect(self.beginShow)

        self.fullscreen = False
        self.hour = 0
        self.minute = 0
        self.second = 0

    #设置倒计时时间
    def setCountDownTime(self):
        self.ui.hour=int(self.lineEdit_h.text())
        self.ui.minute = int(self.lineEdit_m.text())
        self.ui.second = int(self.lineEdit_s.text())

        if (self.radioBtn_fullscreen.isChecked()):
            self.fullscreen = True

    #开始倒计时显示
    def beginShow(self):
        self.setCountDownTime()
        self.close()

        if self.fullscreen:
            self.ui.label.setStyleSheet(_fromUtf8("font: 48pt \"微软雅黑\";\n"
                                                  ""))
            self.ui.showFullScreen()

        else:
            self.ui.label.setStyleSheet(_fromUtf8("font: 36pt \"微软雅黑\";\n"
                                                  ""))
            self.ui.show()

#倒计时显示界面
class countDownShow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.initUi()

    def initUi(self):
        self.setObjectName(_fromUtf8("Form"))
        self.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 121, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(self)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 121, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Form", "Python小秒表-倒计时", None))
        self.label.setText(_translate("Form", "00:00:00", None))

        self.hour = 0
        self.minute = 0
        self.second = 0

        # 利用一个定时器来每秒更新
        self.timerSecond = QTimer(self)
        self.timerSecond.timeout.connect(self.updateSecond)

    #重载show事件函数，窗口打开时自动显示时间和倒计时
    def showEvent(self, QShowEvent):
        strtime=self.getStrTime()
        self.label.setText(strtime)
        self.timerSecond.start(1000)

    # 监听键盘输入，按ESC键退出计时程序
    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            self.close()

    #将时分秒整合为一个字符串
    def getStrTime(self):
        if self.second > 0:
            self.second = self.second - 1

        if self.hour < 10:
            hourStr = "0" + str(self.hour)
        else:
            hourStr = str(self.hour)

        if self.minute < 10:
            minuteStr = "0" + str(self.minute)
        else:
            minuteStr = str(self.minute)
        if self.second < 10:
            secondStr = "0" + str(self.second)
        else:
            secondStr = str(self.second)

        strTime = hourStr + ":" + minuteStr + ":" + secondStr
        return strTime

    #每秒更新时间数字
    def updateSecond(self):
            if self.second==0:
                if self.minute==0:
                    if self.hour==0:
                        self.timerSecond.stop()
                        return
                    if self.hour > 0:
                        self.hour=self.hour -1
                        self.minute=60
                if self.minute > 0:
                    self.minute=self.minute-1
                    self.second=60

            strTime = self.getStrTime()
            self.label.setText(strTime)
            return



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    #为了让中文显示
    app.Encoding(QtGui.QApplication.UnicodeUTF8)
    utfcodec = QTextCodec.codecForName("UTF-8")
    QTextCodec.setCodecForTr(utfcodec)
    QTextCodec.setCodecForLocale(utfcodec)
    QTextCodec.setCodecForCStrings(utfcodec)

    ui =miaoBiao()
    ui.show()

    sys.exit(app.exec_())