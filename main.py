from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QMessageBox
from gevent.libev.corecext import sys

from MainWindow import Ui_MainWindow


class MainWin(QMainWindow,Ui_MainWindow):

    def __init__(self,):
        super(MainWin, self).__init__()
        self.setupUi(self)
        #self.setup_table_view()
        self.connect_sql()


        self.pushButton_close_win.clicked.connect(self.close)

        self.pushButton_user_manage.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(0))
        self.pushButton_lib_manage.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(1))

    def connect_sql(self):
        database = QSqlDatabase.addDatabase("QMYSQL")
        database.setHostName("127.0.0.1")
        database.setUserName("root")
        database.setPassword("wang2008hao")
        database.setPort(3306)
        database.setDatabaseName("libmanage")
        if not database.open():

            print(database.lastError().text())
           # QMessageBox.warning("错误！")
        print(database.drivers())

        model = QSqlTableModel()
        model.setTable("userinfo")
        self.tableView_userinfo.setModel(model)

        model.select()
        model.setHeaderData(0, Qt.Horizontal, "编号")
        model.setHeaderData(1, Qt.Horizontal, "密码")
        model.setHeaderData(2, Qt.Horizontal, "姓名")
        model.setHeaderData(3, Qt.Horizontal, "性别")
        model.setHeaderData(4, Qt.Horizontal, "年龄")
        model.setHeaderData(5, Qt.Horizontal, "电话")
        model.setHeaderData(6, Qt.Horizontal, "电子邮箱")
        model.setHeaderData(7, Qt.Horizontal, "地址")


def setup_table_view(self):
       # self.tableView_userinfo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        model = QSqlTableModel()
        model.setTable("userinfo")

        model.select()
        model.setHeaderData(0, Qt.Horizontal, "编号")
        model.setHeaderData(1, Qt.Horizontal, "密码")
        model.setHeaderData(2, Qt.Horizontal, "姓名")
        model.setHeaderData(3, Qt.Horizontal, "性别")
        model.setHeaderData(4, Qt.Horizontal, "年龄")
        model.setHeaderData(5, Qt.Horizontal, "电话")
        model.setHeaderData(6, Qt.Horizontal, "电子邮箱")
        model.setHeaderData(7, Qt.Horizontal, "地址")







if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
