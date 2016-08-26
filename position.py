#coding:utf-8
# 导入必须模块
import sys
from PySide.QtGui import *
from Dialog import *

if __name__ == '__main__':
     # 创建main application
     myApp = QApplication(sys.argv)
     w = Dialog()
     #w.setAttribute(QtCore.Qt.WA_StyledBackground, True)
     # 显示这个Label
     # p = w.palette()
     # p.setColor(w.backgroundRole(), QColor(0,0,255))
     # w.setPalette(p)
     w.show()
     # 运行main application
     myApp.exec_()
     sys.exit()