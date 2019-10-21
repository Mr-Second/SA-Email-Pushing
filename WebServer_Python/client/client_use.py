from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsDropShadowEffect, QHeaderView, QTableWidgetItem, QMessageBox
from UI.client import Ui_Form


class Client(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Client, self).__init__(parent)
        self.setupUi(self)

        # 控制无边窗口移动
        self.m_flag = None
        self.m_Position = None
        self.init()

    def init(self):
        # 设置窗体无边框
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowOpacity(1)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(6, 6)
        shadow.setBlurRadius(10)
        shadow.setColor(QtGui.QColor(43, 43, 43))
        self.Frame.setGraphicsEffect(shadow)

        # 设置模态对话框
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.infoTable.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

    # 以下三个函数用于控制无边框的窗口移动
    # --------------------------------------------------------------------------------
    # 重载鼠标按压事件

    def mousePressEvent(self, *args, **kwargs):
        event = args[0]
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

        # 重载鼠标移动事件

    def mouseMoveEvent(self, *args, **kwargs):
        QMouseEvent = args[0]
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

        # 重载鼠标释放事件

    def mouseReleaseEvent(self, *args, **kwargs):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    # --------------------------------------------------------------------------------

    def addRow(self):
        item = QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEditable)
        rowIndex = self.infoTable.rowCount()
        self.infoTable.setRowCount(rowIndex+1)
        self.infoTable.setItem(rowIndex, 0, item)
        pass

    def delRow(self):
        rowIndex = self.infoTable.rowCount()-1
        if rowIndex >= 0:
            print(rowIndex)
            self.infoTable.removeRow(rowIndex)
        pass

    def closeWin(self):
        exit(0)

    def clearAll(self):
        self.payloadInput.setText("")
        self.infoTable.setRowCount(0)

    def sendResquest(self):
        if self.infoTable.rowCount() == 0:
            QMessageBox.critical(self, "Error", "Please Add at least one target Address to send!", QMessageBox.Ok)
            return
        elif len(self.payloadInput.toPlainText()) == 0:
            QMessageBox.critical(self, "Error", "Please write down the words you want to send", QMessageBox.Ok)
            return

        if self.serverChoice.currentText() == "Soap":  # 根据选择框选择不同的服务
            self.soapService()  # soap服务
        else:
            self.restService()  # rest服务

    '''
    首先判断是否是一行，如果是一行则调用sendEmail函数，否则调用sendEmaliBatch函数
    不管是在调用哪种函数之前都会先调用validateEmailAddress(_validateEmailAddress)函数
    来判断邮件的格式是否合法，对于sendEmaliBatch函数，如果其中有非法的函数，会将其剔除，
    并在最后界面的status上显示Error
    '''
    def soapService(self):
        from client.Soap_func import sendEmail, sendEmaliBatch, validateEmailAddress

        rowCount = self.infoTable.rowCount()
        if rowCount == 1:
            _url = self.infoTable.item(0, 1).text()
            _payload = self.payloadInput.toPlainText()
            if validateEmailAddress(_url=_url):
                flag = sendEmail(_url=_url, _payload=_payload)
                if flag:
                    self.infoTable.item(0, 0).setText("Success")
                    self.infoTable.update()
                    self.infoTable.viewport().update()
                    QMessageBox.information(self, "Tip", "Succeed to send the Email", QMessageBox.Ok)
                    return
                else:
                    self.infoTable.item(0, 0).setText("Error")
                    self.infoTable.update()
                    self.infoTable.viewport().update()
                    QMessageBox.information(self, "Tip", "Fail to send the Email,Please check the Address you input!",
                                            QMessageBox.Ok)
                    return
            else:
                QMessageBox.information(self, "Tip", "The mail is invalid! Please check the Email", QMessageBox.Ok)
                return
        else:
            _url = []
            _validRow = []  # 有效邮件
            _invalidRow = []  # 无效邮件
            for i in range(0, rowCount):
                if self.infoTable.item(i, 1): # 空行省略
                    curUrl = self.infoTable.item(i, 1).text()
                    if len(curUrl) != 0 and validateEmailAddress(curUrl):  # 先检查邮件的地址是否合法
                        _url.append(curUrl)
                        _validRow.append(i)
                    else:
                        _invalidRow.append(i)
            _payload = self.payloadInput.toPlainText()
            flag = sendEmaliBatch(_url=_url, _payload=_payload)
            if flag:
                for i in _validRow:
                    self.infoTable.item(i, 0).setText("Success")
                for i in _invalidRow:
                    self.infoTable.item(i, 0).setText("Error")
                self.infoTable.update()
                self.infoTable.viewport().update()
                QMessageBox.information(self, "Tip", "Succeed to send the Email(Which are valid)", QMessageBox.Ok)
                return
            else:
                for i in range(rowCount):
                    self.infoTable.item(i, 0).setText("Error")
                self.infoTable.update()
                self.infoTable.viewport().update()
                QMessageBox.information(self, "Tip", "Fail to send the Email,Please check the Address you input!",
                                        QMessageBox.Ok)
                return

    '''
    基本结构与soapService函数相同，只是调用的函数库不同
    '''
    def restService(self):
        from client.Rest_func import _sendEmail, _sendEmaliBatch, _validateEmailAddress

        rowCount = self.infoTable.rowCount()
        if rowCount == 1:
            _url = self.infoTable.item(0, 1).text()
            _payload = self.payloadInput.toPlainText()
            if _validateEmailAddress(_url=_url):
                flag = _sendEmail(_url=_url, _payload=_payload)
                if flag:
                    self.infoTable.item(0, 0).setText("Success")
                    self.infoTable.update()
                    self.infoTable.viewport().update()
                    QMessageBox.information(self, "Tip", "Succeed to send the Email", QMessageBox.Ok)

                    return
                else:
                    self.infoTable.item(0, 0).setText("Error")
                    self.infoTable.update()
                    self.infoTable.viewport().update()
                    QMessageBox.information(self, "Tip", "Fail to send the Email,Please check the Address you input!",
                                            QMessageBox.Ok)
                    return
            else:
                QMessageBox.information(self, "Tip", "The mail is invalid! Please check the Email", QMessageBox.Ok)
                return
        else:
            _url = []
            _validRow = []  # 有效邮件
            _invalidRow = []  # 无效邮件
            for i in range(0, rowCount):
                if self.infoTable.item(i, 1):  # 空行省略
                    curUrl = self.infoTable.item(i, 1).text()
                    if len(curUrl) != 0 and _validateEmailAddress(curUrl):  # 先检查邮件的地址是否合法
                        _url.append(curUrl)
                        _validRow.append(i)
                    else:
                        _invalidRow.append(i)
            _payload = self.payloadInput.toPlainText()
            flag = _sendEmaliBatch(_url=_url, _payload=_payload)
            if flag:
                for i in _validRow:
                    self.infoTable.item(i, 0).setText("Success")
                for i in _invalidRow:
                    self.infoTable.item(i, 0).setText("Error")
                self.infoTable.update()
                self.infoTable.viewport().update()
                QMessageBox.information(self, "Tip", "Succeed to send the Email(Which are valid)", QMessageBox.Ok)
                return

            else:
                for i in range(rowCount):
                    self.infoTable.item(i, 0).setText("Error")
                self.infoTable.update()
                self.infoTable.viewport().update()
                QMessageBox.information(self, "Tip", "Fail to send the Email,Please check the Address you input!",
                                        QMessageBox.Ok)
                return


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = Client()
    myWin.show()
    sys.exit(app.exec_())
