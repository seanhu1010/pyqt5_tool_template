#!/usr/bin/envpython
# -*- coding:utf-8-*-

"""
工具主函数
"""
import sys
import logging
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from common.unilogging import logger
from some_tool.toollib.dummy_tool import ping_server
from some_tool.ui.mainwindow_light import Ui_MainWindow
from some_tool.ui import resources_rc


class QTextBrowserHandler(logging.Handler):
    """
    自定义的日志处理器，用于将日志信息输出到QTextBrowser控件。
    """

    def __init__(self, text_browser):
        """
        初始化函数，设置文本浏览器和日志级别对应的颜色。
        """
        super().__init__()
        self.text_browser = text_browser
        self.level_colors = {
            'DEBUG': '#A9A9A9',  # 灰白色（亮黑色）
            'INFO': '#00FF00',  # 绿色
            'WARNING': '#FFA500',  # 橘黄色
            'ERROR': '#FF0000',  # 红色
            'CRITICAL': '#FF0000',  # 红色
        }

    def emit(self, record):
        """
        处理日志记录，将其格式化并输出到文本浏览器。
        """
        msg = self.format(record)
        color = self.level_colors.get(record.levelname, '#000000')  # 默认为黑色
        html = f'<p style="color: {color}">{msg}</p>'
        cursor = self.text_browser.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.text_browser.setTextCursor(cursor)
        self.text_browser.append(html)
        self.text_browser.ensureCursorVisible()


class FunctionThread(QThread):
    """
    自定义的线程类，用于在新线程中运行函数。
    """

    def __init__(self, func, *args, **kwargs):
        """
        初始化函数，设置要运行的函数和参数。
        """
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """
        线程运行函数，调用设置的函数并处理可能的异常。
        """
        try:
            self.func(*self.args, **self.kwargs)
        except Exception as e:
            logger.error(f'发生未知错误：{e}')


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    主窗口类，继承自QMainWindow和Ui_MainWindow。
    """

    def __init__(self, *args, parent=None, **kwargs):
        """
        初始化函数，设置UI，初始化定时器，绑定按钮，初始化线程列表。
        """
        super(MainWindow, self).__init__(*args, parent, **kwargs)
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start(1000)  # 每1000ms（即1秒）更新一次

        # 日志处理
        self.handler = QTextBrowserHandler(self.textBrowser)
        logger.add(self.handler)

        # 绑定button
        self.callButton.clicked.connect(self.start_ping)
        self.recallButton.clicked.connect(self.start_ping)

        # 初始化线程列表
        self.threads = []

        # 绑定button
        self.stopButton.clicked.connect(self.stop_all_threads)

    def recurring_timer(self):
        """
        定时器回调函数，更新显示的时间。
        """
        current_time = QTime.currentTime()
        text = current_time.toString('hh:mm:ss')
        self.labelShowTime.setText(text)

    def start_ping(self):
        """
        启动ping操作的函数，创建新线程运行ping_server函数。
        """
        thread = FunctionThread(ping_server, '127.0.0.1', 200)
        thread.start()
        self.threads.append(thread)

    def stop_all_threads(self):
        """
        停止所有线程的函数，遍历线程列表并终止每个线程。
        """
        for thread in self.threads:
            thread.terminate()
        self.threads = []


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 加载全局qss样式
    # with open('ui/mainwindow.qss', 'r') as f:
    #     style = f.read()
    #     app.setStyleSheet(style)

    # 从资源文件中加载字体
    font_id = QFontDatabase.addApplicationFont(":/fonts/OPPOSans-B-2.ttf")

    # 检查字体是否加载成功
    if font_id != -1:
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            # 创建一个 QFont 对象
            font = QFont(font_families[0], 10)

            # 设置全局字体
            app.setFont(font)
    else:
        print("Failed to load font.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
