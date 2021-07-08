# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/UNSUP_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 801)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.intime_canvs = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intime_canvs.sizePolicy().hasHeightForWidth())
        self.intime_canvs.setSizePolicy(sizePolicy)
        self.intime_canvs.setMinimumSize(QtCore.QSize(980, 380))
        self.intime_canvs.setObjectName("intime_canvs")
        self.intime_layout = QtWidgets.QVBoxLayout(self.intime_canvs)
        self.intime_layout.setObjectName("intime_layout")
        self.verticalLayout.addWidget(self.intime_canvs)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.ep_whole_edit = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ep_whole_edit.setFont(font)
        self.ep_whole_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ep_whole_edit.setObjectName("ep_whole_edit")
        self.gridLayout.addWidget(self.ep_whole_edit, 2, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.bs_edit = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.bs_edit.setFont(font)
        self.bs_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.bs_edit.setObjectName("bs_edit")
        self.gridLayout.addWidget(self.bs_edit, 3, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.ep_layer_edit = QtWidgets.QLineEdit(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ep_layer_edit.setFont(font)
        self.ep_layer_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ep_layer_edit.setObjectName("ep_layer_edit")
        self.gridLayout.addWidget(self.ep_layer_edit, 1, 1, 1, 2)
        self.save_last_only = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_last_only.sizePolicy().hasHeightForWidth())
        self.save_last_only.setSizePolicy(sizePolicy)
        self.save_last_only.setObjectName("save_last_only")
        self.gridLayout.addWidget(self.save_last_only, 4, 2, 1, 1)
        self.train_btn = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.train_btn.setFont(font)
        self.train_btn.setObjectName("train_btn")
        self.gridLayout.addWidget(self.train_btn, 5, 1, 1, 1)
        self.load_data_btn = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.load_data_btn.setFont(font)
        self.load_data_btn.setObjectName("load_data_btn")
        self.gridLayout.addWidget(self.load_data_btn, 5, 0, 1, 1)
        self.show_tb_btn = QtWidgets.QPushButton(self.tab_3)
        self.show_tb_btn.setEnabled(False)
        self.show_tb_btn.setObjectName("show_tb_btn")
        self.gridLayout.addWidget(self.show_tb_btn, 5, 2, 1, 1)
        self.train_progressBar = QtWidgets.QProgressBar(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.train_progressBar.setFont(font)
        self.train_progressBar.setStatusTip("")
        self.train_progressBar.setProperty("value", 20)
        self.train_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.train_progressBar.setTextVisible(True)
        self.train_progressBar.setObjectName("train_progressBar")
        self.gridLayout.addWidget(self.train_progressBar, 6, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.load_model_btn = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_model_btn.sizePolicy().hasHeightForWidth())
        self.load_model_btn.setSizePolicy(sizePolicy)
        self.load_model_btn.setObjectName("load_model_btn")
        self.gridLayout_2.addWidget(self.load_model_btn, 2, 1, 1, 1)
        self.load_test_btn = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_test_btn.sizePolicy().hasHeightForWidth())
        self.load_test_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.load_test_btn.setFont(font)
        self.load_test_btn.setObjectName("load_test_btn")
        self.gridLayout_2.addWidget(self.load_test_btn, 2, 0, 1, 1)
        self.predict_btn = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predict_btn.sizePolicy().hasHeightForWidth())
        self.predict_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.predict_btn.setFont(font)
        self.predict_btn.setObjectName("predict_btn")
        self.gridLayout_2.addWidget(self.predict_btn, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.clas_edit = QtWidgets.QLineEdit(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.clas_edit.setFont(font)
        self.clas_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.clas_edit.setReadOnly(True)
        self.clas_edit.setObjectName("clas_edit")
        self.gridLayout_2.addWidget(self.clas_edit, 0, 1, 1, 3)
        self.clas_pro_edit = QtWidgets.QLineEdit(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.clas_pro_edit.setFont(font)
        self.clas_pro_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.clas_pro_edit.setReadOnly(True)
        self.clas_pro_edit.setObjectName("clas_pro_edit")
        self.gridLayout_2.addWidget(self.clas_pro_edit, 1, 1, 1, 3)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.ep_layer_edit)
        MainWindow.setTabOrder(self.ep_layer_edit, self.ep_whole_edit)
        MainWindow.setTabOrder(self.ep_whole_edit, self.bs_edit)
        MainWindow.setTabOrder(self.bs_edit, self.save_last_only)
        MainWindow.setTabOrder(self.save_last_only, self.load_data_btn)
        MainWindow.setTabOrder(self.load_data_btn, self.train_btn)
        MainWindow.setTabOrder(self.train_btn, self.show_tb_btn)
        MainWindow.setTabOrder(self.show_tb_btn, self.clas_edit)
        MainWindow.setTabOrder(self.clas_edit, self.clas_pro_edit)
        MainWindow.setTabOrder(self.clas_pro_edit, self.load_test_btn)
        MainWindow.setTabOrder(self.load_test_btn, self.load_model_btn)
        MainWindow.setTabOrder(self.load_model_btn, self.predict_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "无监督学习"))
        self.label.setStatusTip(_translate("MainWindow", "训练迭代轮数--SAE"))
        self.label.setText(_translate("MainWindow", "epochs_layer:"))
        self.label_2.setStatusTip(_translate("MainWindow", "Batch_size大小"))
        self.label_2.setText(_translate("MainWindow", "batch size:"))
        self.label_6.setStatusTip(_translate("MainWindow", "训练迭代轮数--CLASSIFICATION"))
        self.label_6.setText(_translate("MainWindow", "epochs_whole:"))
        self.save_last_only.setStatusTip(_translate("MainWindow", "是否仅保存最后一个epoch的模型"))
        self.save_last_only.setText(_translate("MainWindow", "Save last only"))
        self.train_btn.setStatusTip(_translate("MainWindow", "开始训练"))
        self.train_btn.setText(_translate("MainWindow", "训练"))
        self.load_data_btn.setStatusTip(_translate("MainWindow", "加载数据，前处理所存的.npy文件所在文件夹"))
        self.load_data_btn.setText(_translate("MainWindow", "加载数据"))
        self.show_tb_btn.setStatusTip(_translate("MainWindow", "展开TensorBoard具体训练过程"))
        self.show_tb_btn.setText(_translate("MainWindow", "展开训练过程"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "训练"))
        self.load_model_btn.setStatusTip(_translate("MainWindow", "加载训练好的.h5模型"))
        self.load_model_btn.setText(_translate("MainWindow", "加载权重"))
        self.load_test_btn.setStatusTip(_translate("MainWindow", "加载待测试数据"))
        self.load_test_btn.setText(_translate("MainWindow", "加载数据"))
        self.predict_btn.setStatusTip(_translate("MainWindow", "开始检测"))
        self.predict_btn.setText(_translate("MainWindow", "检测"))
        self.label_5.setText(_translate("MainWindow", "类别:"))
        self.label_4.setText(_translate("MainWindow", "概率："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "检测"))

