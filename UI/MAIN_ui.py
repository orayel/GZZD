# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAIN_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pre_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pre_btn.sizePolicy().hasHeightForWidth())
        self.pre_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pre_btn.setFont(font)
        self.pre_btn.setToolTip("")
        self.pre_btn.setObjectName("pre_btn")
        self.verticalLayout.addWidget(self.pre_btn)
        self.sup_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sup_btn.sizePolicy().hasHeightForWidth())
        self.sup_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.sup_btn.setFont(font)
        self.sup_btn.setObjectName("sup_btn")
        self.verticalLayout.addWidget(self.sup_btn)
        self.semisup_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semisup_btn.sizePolicy().hasHeightForWidth())
        self.semisup_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.semisup_btn.setFont(font)
        self.semisup_btn.setObjectName("semisup_btn")
        self.verticalLayout.addWidget(self.semisup_btn)
        self.unsup_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unsup_btn.sizePolicy().hasHeightForWidth())
        self.unsup_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.unsup_btn.setFont(font)
        self.unsup_btn.setObjectName("unsup_btn")
        self.verticalLayout.addWidget(self.unsup_btn)
        self.suffix_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suffix_btn.sizePolicy().hasHeightForWidth())
        self.suffix_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.suffix_btn.setFont(font)
        self.suffix_btn.setObjectName("suffix_btn")
        self.verticalLayout.addWidget(self.suffix_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主程序"))
        self.pre_btn.setStatusTip(_translate("MainWindow", "支持用户自行定义截取信号长度、输入信号类型（如时域信号、频域信号），可以显示信号的时域、频域特征。"))
        self.pre_btn.setText(_translate("MainWindow", "前处理"))
        self.sup_btn.setStatusTip(_translate("MainWindow", "监督学习训练与预测（MobileNet）"))
        self.sup_btn.setText(_translate("MainWindow", "监督学习"))
        self.semisup_btn.setStatusTip(_translate("MainWindow", "半监督学习训练与预测（SGAN）"))
        self.semisup_btn.setText(_translate("MainWindow", "半监督学习"))
        self.unsup_btn.setStatusTip(_translate("MainWindow", "无监督学习训练与预测（SAE）"))
        self.unsup_btn.setText(_translate("MainWindow", "无监督学习"))
        self.suffix_btn.setStatusTip(_translate("MainWindow", "计算结果的统计分析与展示"))
        self.suffix_btn.setText(_translate("MainWindow", "后处理"))
