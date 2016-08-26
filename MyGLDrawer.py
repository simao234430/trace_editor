from PySide.QtOpenGL import *
class MyGLDrawer(QGLWidget):

    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        pass

    def initializeGL(self):
        # Set up the rendering context, define display lists etc.:

        glClearColor(0.0, 0.0, 0.0, 0.0)
        glEnable(GL_DEPTH_TEST)


    def resizeGL(self, w, h):
        # setup viewport, projection etc.:
        glViewport(0, 0, w, h)

        glFrustum(...)


    def paintGL(self):
        # draw the scene:

        glRotatef(...)
        glMaterialfv(...)
        glBegin(GL_QUADS)
        glVertex3f(...)
        glVertex3f(...)

        glEnd()
