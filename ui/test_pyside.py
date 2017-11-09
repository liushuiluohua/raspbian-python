#coding:utf-8
# 导入必须模块
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QLabel,QPushButton

def cmd_print_info():
    print "cmd_print"

# 主函数
if __name__ == '__main__':
    myApp = QApplication(sys.argv)  # 创建Label并设置它的属性
    button =QPushButton(u"按钮测试")
    button.clicked.connect(cmd_print_info) 
    appLabel = QLabel()
    appLabel.setText(u"<font color=red size=40>这是我的第一个PySide程序</font>")
    appLabel.setAlignment(Qt.AlignCenter)
    appLabel.setWindowTitle(u"PySide测试程序")
    appLabel.setGeometry(300, 300, 600, 300)
    appLabel.show()    # 显示这个Label
    button.show()      # 运行main application
    myApp.exec_()
    sys.exit()
