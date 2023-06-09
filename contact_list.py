# Form implementation generated from reading ui file 'contact_list1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2

from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

class Bdd_interact:
    def __init__(self):
        self.bdd_name = "contact_list_bdd"
        self.connect = sqlite3.connect(self.bdd_name)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            first_name TEXT,
            last_name TEXT,
            telephone TEXT,
            e_mail TEXT,
            address TEXT
            )""")
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            raise e
    
    def get_contact(self, contact):
        self.cursor.execute("""SELECT * FROM contact WHERE id = ?""", (contact[0], ))
        find_contact = self.cursor.fetchone()
        self.connect.commit()
        return find_contact

    def get_all_contact(self):
        self.cursor.execute("""SELECT * FROM contact""")
        contact_list = self.cursor.fetchall()
        self.connect.commit()
        return contact_list

    def add_contact(self, contact):
        self.cursor.execute("""INSERT INTO contact(first_name, last_name, telephone, e_mail, address) VALUES(?, ?, ?, ?, ?)""", (contact.first_name, contact.last_name, contact.telephone, contact.e_mail, contact.address))
        self.connect.commit()
        return contact
    
    def update_contact(self, contact):
        self.cursor.execute("""UPDATE contact SET first_name = ?, last_name = ?, telephone = ?, e_mail = ?, address = ? WHERE id = ?""", (contact[1], contact[2], contact[3], contact[4], contact[5], contact[0]))
        self.connect.commit()
        return contact
        
    def delete_contact(self, contact):
        self.cursor.execute("""DELETE FROM contact WHERE id = ?""", (contact[0], ))
        self.connect.commit()
        return contact
    
    def delete_table(self):
        self.cursor.execute("""DROP TABLE contact""")
        self.connect.commit()

class Contact:
    def __init__(self, first_name: str="", last_name: str="", telephone: str="", e_mail: str="", address: str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.e_mail = e_mail
        self.address = address

class Ui_Form(object):
    def create_contact(self):
        contact_obj = Contact(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text())
        self.bdd_interact.add_contact(contact_obj)
        self.list_contact()

    def update_contact(self):
        if hasattr(self, 'current_contact'):
            contact = (self.current_contact[0], self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text())
            self.bdd_interact.update_contact(contact)
        self.list_contact()

    def populate_fields(self, item):
        contact_name = item.text()
        for c in self.all_contact:
            if c[1] + " " + c[2]  == contact_name:
                self.current_contact = self.bdd_interact.get_contact(c)
                break
        self.lineEdit.setText(self.current_contact[1])
        self.lineEdit_2.setText(self.current_contact[2])
        self.lineEdit_3.setText(self.current_contact[3])
        self.lineEdit_4.setText(self.current_contact[4])
        self.lineEdit_5.setText(self.current_contact[5])
    
    def list_contact(self):
        self.listWidget.clear()
        self.all_contact = self.bdd_interact.get_all_contact()
        for c in self.all_contact:
            self.listWidget.addItem(c[1] + " " + c[2])

    def delete_contact(self):
        if hasattr(self, 'current_contact'):
            self.bdd_interact.delete_contact(self.current_contact)
        self.clear_fields()
        self.list_contact()

    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

    def setupUi(self, Form):
        self.bdd_interact = Bdd_interact()
        Form.setObjectName("Form")
        Form.resize(359, 415)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form) # field first_name
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form) # field last_name
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form) # field telephone
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form) # field e-mail
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_9.addWidget(self.lineEdit_4)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_5, 4, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form) # field address
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_11.addWidget(self.lineEdit_5)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout_6, 5, 0, 1, 1)

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton = QtWidgets.QPushButton(parent=Form) # add button
        self.pushButton.clicked.connect(self.create_contact)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_12.addWidget(self.pushButton)

        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form) # update button
        self.pushButton_4.clicked.connect(self.update_contact)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_15.addWidget(self.pushButton_4)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form) # delete button
        self.pushButton_3.clicked.connect(self.delete_contact)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_14.addWidget(self.pushButton_3)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form) # clear fields button
        self.pushButton_2.clicked.connect(self.clear_fields)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_13.addWidget(self.pushButton_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)

        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.gridLayout.addLayout(self.verticalLayout_7, 6, 0, 1, 1)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.listWidget = QtWidgets.QListWidget(parent=Form) # field list
        self.listWidget.itemDoubleClicked.connect(self.populate_fields)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_8.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout_8, 7, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Contact List"))
        self.label_2.setText(_translate("Form", "First Name :"))
        self.label_3.setText(_translate("Form", "Last Name :"))
        self.label_4.setText(_translate("Form", "Telephone : "))
        self.label_5.setText(_translate("Form", "E-mail :       "))
        self.label_6.setText(_translate("Form", "Address :    "))
        self.pushButton.setText(_translate("Form", "Add Contact"))
        self.pushButton_4.setText(_translate("Form", "Update Contact"))
        self.pushButton_3.setText(_translate("Form", "Delete Contact"))
        self.pushButton_2.setText(_translate("Form", "Clear Fields"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.list_contact()
    sys.exit(app.exec())
