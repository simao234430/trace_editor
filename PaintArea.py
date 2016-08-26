#coding:utf-8
# 导入必须模块
import sys, random
from socket import *
import time
from PySide.QtGui import *
from PySide.QtCore import *
import numpy as np
from Dialog import *
TRUE = 1
FALSE = 0

MAXPOINTS = 2000;  # maximum number of points
MAXCOLORS = 40;
class PaintArea(QFrame):
#class PaintArea(QGraphicsView):
    def __init__(self, parent=None):
        self.parent = parent
        QFrame.__init__(self,parent)
        #print self.width(),self.height()

        #QFrame.setStyleSheet()
        self.setStyleSheet("border: 1px solid red");

        self.down = FALSE

        self.points = []
        self.colors = []
        self.pencolor = None

    def file_choose(self):
        fname = QFileDialog.getOpenFileName()
        print fname[0]
        # palette = QPalette()
        # palette.setBrush(self.backgroundRole(),QBrush(QImage(fname[0])))
        # self.setPalette(palette)
        # self.update()
        #
        # brush = self..backgroundBrush()
        # self.setBackgroundBrush(QBrush(QImage(fname[0])))


        #self.setBackgroundBrush(brush)
        #print fname


    def color_picker(self):
        self.pencolor = QColorDialog.getColor()
        #self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def paintEvent(self, pe):
        paint = QPainter(self)
        #print "###", len(self.points)
        paint.setPen(self.pencolor)  # set random pen color
        for i in range(len(self.points) - 1):  # connect all points
            #for j in range(i + 1, self.count):
            #paint.setPen(QColor(Qt.red))  # set random pen color
            paint.drawLine(self.points[i], self.points[i+1])  # draw line



    def erase(self):
        pass

    #
    # Handles mouse press events for the connect widget.
    #
    def mousePressEvent(self, me):
        self.down = TRUE
        #self.count = 0  # start recording points
        self.erase()  # erase widget contents
        self.points = []
        self.startTimer = time.time()

    #
    # Handles mouse release events for the connect widget.
    #
    def mouseReleaseEvent(self, me):

        self.down = FALSE  # done recording points
        self.costTime = time.time() - self.startTimer
        self.update()  # draw the lines
        # for i in self.points:
        #     print i.x(),i.y()
        #print self.size().width(), self.size().height()



    #
    # Handles mouse move events for the connect widget.
    #
    def mouseMoveEvent(self, me):
        if self.down:
            paint = QPainter(self)
            self.points.append(QPoint(me.pos()))  # add point
            paint.drawPoint(me.pos())  # plot point
            #self.count = self.count + 1
            self.update()  # draw the lines

    def show(self,x,y):
        for i in xrange(len(x)):
            print x[i],y[i]

    def process_data(self,x,y,density):
        try:
            new_x = []
            new_y = []
            for i in xrange(len(x) - 1):
                x_data = [x[i],x[i+1]]
                y_data = [y[i], y[i + 1]]
                t = np.linspace(x[i], x[i+1], len(x_data))
                t2 = np.linspace(x[i], x[i+1], int(abs(x[i+1] - x[i])/density))
                x2 = np.interp(t2, t, x_data)
                y2 = np.interp(t2, t, y_data)
                #print x_data, t,t2,x2,(x[i+1] - x[i+1])/density
                #print type(x2.tolist())
                new_x += x2.tolist()
                new_y += y2.tolist()
            return new_x,new_y
        except Exception,e:
            print e
    def generate_send_data(self):

        #print type(self.parent.actDistanceText.text())
        #print str(self.parent.actDistanceText.text())
        transfort_rate =  float(str(self.parent.actDistanceText.text()))/self.size().height()
        #print transfort_rate
        pos_x = []
        pos_y = []
        #位置转换
        for i in self.points:
            pos_x.append(i.x() * transfort_rate)
            pos_y.append((self.size().height() - i.y()) * transfort_rate)
        #self.show(pos_x,pos_y)
        #print "#插值"
        #插值
        new_x,new_y = self.process_data(pos_x,pos_y,float(str(self.parent.densityText.text())))
        #self.show(new_x, new_y)
        #print "#插值2"
        data = []
        offset_x = float(str(self.parent.offset_xText.text()))
        offset_y = float(str(self.parent.offset_yText.text()))
        for i in xrange(len(new_x)):
        #for i in self.points:
            #print i.x(), i.y()
            #temp = "$POS,%d,%d,%d,0,0,%f\n" % (int(str(self.parent.tagText.text())), i.x(), i.y(), time.time())
            temp = "$POS,%d,%0.1f,%0.1f,0.0,0,%f\n" % (int(str(self.parent.tagText.text())), float('%0.1f'% (new_x[i] + offset_x)) , \
                                                 float('%0.1f' %(new_y[i] + offset_y)), time.time())
            data.append(temp)
        #print len(data)
        return data

    def send(self):
        try:

            HOST = str(self.parent.ipText.text())
            #HOST = "10.0.0.49"
            PORT = int(str(self.parent.portText.text()))
            addr = (HOST, PORT)
            sock = socket(AF_INET, SOCK_DGRAM)
            send_data = self.generate_send_data()
            #print send_data

            #time.sleep(1.0)
            for d in send_data:
                #print self.costTime
                #print self.parent.rateComboBox.currentIndex()
                ratio = 2 ** (self.parent.rateComboBox.currentIndex()-3)
                rate = (self.costTime/len(send_data)) / ratio
                time.sleep(rate)
                #print d
                #sock.sendto("test",addr)
                sock.sendto(d.encode('utf-8'), addr)

            sock.close()
            m = QMessageBox()
            m.setText(QTextCodec.codecForName("utf-8").toUnicode("发送完毕"))
            m.exec_()
        except Exception,e:
            print e
        # m = QMessageBox()
        # m.setText("dd")
        # m.exec_()