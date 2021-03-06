# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 700)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        Form.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.le_search = QtWidgets.QLineEdit(Form)
        self.le_search.setMaximumSize(QtCore.QSize(250, 16777215))
        self.le_search.setObjectName("le_search")
        self.verticalLayout_2.addWidget(self.le_search)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tb_emps = QtWidgets.QTableWidget(Form)
        self.tb_emps.setObjectName("tb_emps")
        self.tb_emps.setColumnCount(8)
        self.tb_emps.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        item.setFont(font)
        self.tb_emps.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_emps.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_emps.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_emps.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_emps.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_emps.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_emps.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_emps.setHorizontalHeaderItem(7, item)
        self.horizontalLayout.addWidget(self.tb_emps)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_depts = QtWidgets.QComboBox(Form)
        self.cb_depts.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_depts.setObjectName("cb_depts")
        self.cb_depts.addItem("")
        self.verticalLayout.addWidget(self.cb_depts)
        self.bt_add_dept = QtWidgets.QPushButton(Form)
        self.bt_add_dept.setObjectName("bt_add_dept")
        self.verticalLayout.addWidget(self.bt_add_dept)
        self.bt_del_dept = QtWidgets.QPushButton(Form)
        self.bt_del_dept.setObjectName("bt_del_dept")
        self.verticalLayout.addWidget(self.bt_del_dept)
        self.bt_add_emp = QtWidgets.QPushButton(Form)
        self.bt_add_emp.setObjectName("bt_add_emp")
        self.verticalLayout.addWidget(self.bt_add_emp)
        self.bt_del_emp = QtWidgets.QPushButton(Form)
        self.bt_del_emp.setObjectName("bt_del_emp")
        self.verticalLayout.addWidget(self.bt_del_emp)
        self.bt_export = QtWidgets.QPushButton(Form)
        self.bt_export.setObjectName("bt_export")
        self.verticalLayout.addWidget(self.bt_export)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.bt_exit = QtWidgets.QPushButton(Form)
        self.bt_exit.setObjectName("bt_exit")
        self.verticalLayout.addWidget(self.bt_exit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HR-System"))
        self.label.setText(_translate("Form", "HR-System"))
        self.le_search.setPlaceholderText(_translate("Form", "search by name"))
        item = self.tb_emps.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Emp.ID"))
        item = self.tb_emps.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Emp.Name"))
        item = self.tb_emps.horizontalHeaderItem(2)
        item.setText(_translate("Form", "E-mail"))
        item = self.tb_emps.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Hire Date"))
        item = self.tb_emps.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Job ID"))
        item = self.tb_emps.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Salary"))
        item = self.tb_emps.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Dept. ID"))
        self.cb_depts.setItemText(0, _translate("Form", "Select Department"))
        self.bt_add_dept.setText(_translate("Form", "Add Department"))
        self.bt_del_dept.setText(_translate("Form", "Delete Department"))
        self.bt_add_emp.setText(_translate("Form", "Add Employee"))
        self.bt_del_emp.setText(_translate("Form", "Delete Employee"))
        self.bt_export.setText(_translate("Form", "Export"))
        self.bt_exit.setText(_translate("Form", "Exit"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
