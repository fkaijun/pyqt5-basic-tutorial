import sys

from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)   # 创建应用程序实例。管理GUI应用程序的控制流和主要设置

main_win = QtWidgets.QWidget()   # 创建一个窗口对象。
main_win.resize(300, 160)   # 设置创建的窗口对象的宽度与高度。
main_win.setWindowTitle('这个是标题')   # 设置窗口的标题。

hello_lab = QtWidgets.QLabel('Hello World')   # 创建一个小部件标签（GUI组件）对象，同时给标签一个文字。

main_layout = QtWidgets.QHBoxLayout()   # 创建一个水平布局对象。
main_layout.addWidget(hello_lab)    # 把hello_lab标签对象添加到水平布局中，即把hello_lab添加到main_layout容器中。

main_win.setLayout(main_layout)   # 设置主窗口的布局为main_layout，即把main_win作为main_layout的父容器。

main_win.show()   # 显示窗口(向QApplication事件列表中添加新事件，请求对main_win窗口的绘制)


sys.exit(app.exec_())   # app.exec_()的作用是运行主循环，必须调用此函数才能开始事件处理，调用该方法进入程序的主循环直到调用exit（）结束。
                        # 主事件循环从窗口系统接收事件，并将其分派给应用程序小部件。如果没有该方法，那么在运行的时候还没有进入程序的主循环就直接结束了，
                        # 所以不运行的时候窗口会闪退。
                        # app.exec_()在退出时会返回状态代码，不用sys.exit(app.exec_()),只使用app.exec_()，程序也可以正常运行，但是关闭窗口后进程却不会退出。
                        # sys.exit是为了窗口被关闭了系统能得到通知
