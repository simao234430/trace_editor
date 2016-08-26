#coding:utf-8
# 导入必须模块
import sys

from PySide.QtGui import *
from PySide.QtCore import *
from PaintArea import *
import PySide.QtOpenGL
def config_color(w, color):
    p = w.palette()
    p.setColor(w.backgroundRole(), color)
    w.setPalette(p)
    # p = w.palette()
    # p.setColor(QtGui.QPalette.Window, QtGui.QColor().red())
    # w.setPalette(p)

class Dialog(QDialog):
    def __init__(self):
        self.codec = QTextCodec.codecForName("utf-8")
        super(Dialog, self).__init__()
        self.resize(800,600)
        mainLayout = QVBoxLayout()
        self.createHorizontalGroupBox()
        self.createHorizontalGroupBox1()

        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.horizontalGroupBox1)


        self.createPaintArea()
        mainLayout.addWidget(self.PaintArea)


        # p = self.PaintArea.palette()
        # self.PaintArea(self.PaintArea.backgroundRole(), QtGui.QColor(0, 255, 255))
        # self.PaintArea.setPalette(p)
        #self.PaintArea.setPalette(QtGui.QPalette(QtCore.Qt.red))
        #self.PaintArea.setBackgroundRole(QtGui.QColor().red())
        self.connect(self.sendbutton, SIGNAL("clicked()"),
                     self.PaintArea, SLOT("send()"))

        self.connect(self.colorbutton, SIGNAL("clicked()"),
                     self.PaintArea, SLOT("color_picker()"))

        self.connect(self.filebutton, SIGNAL("clicked()"),
                     self.PaintArea, SLOT("file_choose()"))

        mainLayout.setStretchFactor(self.horizontalGroupBox,1)
        mainLayout.setStretchFactor(self.horizontalGroupBox1, 1)
        mainLayout.setStretchFactor(self.PaintArea, 7)
        self.setLayout(mainLayout)
        #self.sizeInfo.setText(self.codec.toUnicode("x y轴比例:%d,%d" % (self.PaintArea.frameRect().size().width()\
        #                                                                 , self.PaintArea.frameRect().size().height())))

    def createHorizontalGroupBox1(self):
        self.horizontalGroupBox1 = QGroupBox(self.codec.toUnicode("测试1"))
        layout = QHBoxLayout()

        self.density = QLabel(self.codec.toUnicode("插值密度"))
        self.densityText = QLineEdit("0.1")

        self.actDistance = QLabel(self.codec.toUnicode("编辑区域距离"))
        self.actDistanceText = QLineEdit("100")

        self.offset_x = QLabel(self.codec.toUnicode("x轴偏移量"))
        self.offset_xText = QLineEdit("0")

        self.offset_y = QLabel(self.codec.toUnicode("y轴"))
        self.offset_yText = QLineEdit("0")

        self.tag = QLabel(self.codec.toUnicode("tag编号"))
        self.tagText = QLineEdit("1")

        layout.addWidget(self.density)
        layout.addWidget(self.densityText)
        layout.addWidget(self.actDistance)
        layout.addWidget(self.actDistanceText)
        layout.addWidget(self.offset_x)
        layout.addWidget(self.offset_xText)
        layout.addWidget(self.offset_y)
        layout.addWidget(self.offset_yText)
        layout.addWidget(self.tag)
        layout.addWidget(self.tagText)


        self.horizontalGroupBox1.setLayout(layout)

    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QGroupBox(self.codec.toUnicode("测试"))
        layout = QHBoxLayout()

        self.rateComboBox=QComboBox()
        self.rateComboBox.insertItem(0,self.codec.toUnicode("-8x"))
        self.rateComboBox.insertItem(1,self.codec.toUnicode("-4x"))
        self.rateComboBox.insertItem(2,self.codec.toUnicode("-2x"))
        self.rateComboBox.insertItem(3,self.codec.toUnicode("1x"))
        self.rateComboBox.insertItem(4,self.codec.toUnicode("2x"))
        self.rateComboBox.insertItem(5,self.codec.toUnicode("4x"))
        self.rateComboBox.insertItem(6,self.codec.toUnicode("8x"))

        self.rateComboBox.setCurrentIndex(3)
        layout.addWidget(self.rateComboBox)

        self.ip = QLabel(self.codec.toUnicode("ip地址"))
        layout.addWidget(self.ip)
        self.ipText = QLineEdit("10.0.0.49")
        layout.addWidget(self.ipText)

        self.port = QLabel(self.codec.toUnicode("端口"))
        layout.addWidget(self.port)
        self.portText = QLineEdit("6666")
        layout.addWidget(self.portText)

        self.sendbutton = QPushButton(self.codec.toUnicode("发送数据"))
        layout.addWidget(self.sendbutton)

        self.filebutton = QPushButton(self.codec.toUnicode("选择背景图文件"))
        layout.addWidget(self.filebutton)

        self.colorbutton = QPushButton(self.codec.toUnicode("选择颜色"))
        layout.addWidget(self.colorbutton)

        self.sizeInfo = QLabel()
        layout.addWidget(self.sizeInfo)

        # for i in range(3):
        #     button = QPushButton("Button %d" % (i + 1))
        #     layout.addWidget(button)

        self.horizontalGroupBox.setLayout(layout)

    def createPaintArea(self):
        # scene = QGraphicsScene()
        # scene.addText("test")
        # scene.addLine(QLineF(0, 0, 100, 100))
        self.PaintArea = PaintArea(self)

        #self.PaintArea = QGraphicsScene()
        # blue = "#0000ff"
        # style_str = "QWidget {background-color: %s}"
        # self.PaintArea.setStyleSheet(style_str % blue)
        #self.PaintArea.setBackground(QtGui.QColor('red'))
        #self.PaintArea.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        # self.PaintArea.setStyleSheet("background-color: red");
        # p = self.PaintArea.palette()
        # p.setColor(QtGui.QPalette.Window,QtCore.Qt.red)
        # self.PaintArea.setPalette(p)


