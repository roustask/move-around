# -*- coding: utf-8 -*-
import sys

from PySide2.QtCore import QUrl
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2.QtWidgets import QFileDialog
from PySide2 import QtCore, QtWidgets, QtGui


class AccessMapScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.toilets_checkbox = QtWidgets.QCheckBox("Toilets")
        self.parkings_checkbox = QtWidgets.QCheckBox("Parkings")
        self.obstacles_checkbox = QtWidgets.QCheckBox("Obstacles")

        self.layout = QtWidgets.QVBoxLayout()

        # self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.quickWidget = QQuickWidget(QUrl('src/ui/access-map.qml'))
        self.layout.addWidget(self.quickWidget)

        self.checkbox_layout = QtWidgets.QHBoxLayout()
        self.checkbox_layout.addWidget(self.toilets_checkbox)
        self.checkbox_layout.addWidget(self.parkings_checkbox)
        self.checkbox_layout.addWidget(self.obstacles_checkbox)

        self.layout.addLayout(self.checkbox_layout)

        self.setLayout(self.layout)
        self.resize(400, 300)


class ChoosePhotographScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_input_file = QtWidgets.QToolButton()
        self.text_edit_photograph = QtWidgets.QLineEdit()
        self.button_submit_report = QtWidgets.QPushButton("Choose Photograph")
        self.preview_photograph = QtWidgets.QLabel()

        self.button_input_file.clicked.connect(self.on_input_file_clicked)
        self.button_submit_report.clicked.connect(self.on_choose_photograph_clicked)

        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout1.addWidget(self.button_input_file)
        self.layout1.addWidget(self.text_edit_photograph)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.layout1)
        self.layout.addWidget(self.button_submit_report)
        self.layout.addWidget(self.preview_photograph)
        self.setLayout(self.layout)
        self.resize(400, 300)

    def on_input_file_clicked(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.')

        if filename:
            self.text_edit_photograph.setText(filename)
            self.photograph = QtGui.QPixmap(filename)
            self.photograph = self.photograph.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
            self.preview_photograph.setPixmap(self.photograph)
            self.preview_photograph.setScaledContents(True)

    def on_choose_photograph_clicked(self):
        issue_description_screen = IssueDescriptionScreen()
        app.show_screen(issue_description_screen)


class ChooseLocationScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_choose_location = QtWidgets.QPushButton("Choose Location")
        self.button_choose_location.clicked.connect(self.on_choose_location_clicked)
        self.layout = QtWidgets.QVBoxLayout()

        # self.horizontal_layout = QtWidgets.QHBoxLayout()

        self.quickWidget = QQuickWidget(QUrl('src/ui/choose-location.qml'))
        self.layout.addWidget(self.quickWidget)
        self.layout.addWidget(self.button_choose_location)
        self.setLayout(self.layout)
        self.resize(400, 300)

    def on_choose_location_clicked(self):
        choose_photograph_screen = ChoosePhotographScreen()
        app.show_screen(choose_photograph_screen)


class IssueDescriptionScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit_description = QtWidgets.QTextEdit()
        self.button_submit_report = QtWidgets.QPushButton("Submit Report")
        self.button_submit_report.clicked.connect(self.on_submit_clicked)
        

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text_edit_description)
        self.layout.addWidget(self.button_submit_report)
        self.setLayout(self.layout)
        self.resize(400, 300)

    def on_submit_clicked(self):
        ms = MainScreen()
        app.show_screen(ms)
        if not self.text_edit_description.toPlainText():
            self.show_popup()
            app.show_screen(IssueDescriptionScreen())

    def show_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Αδυναμία Αποστολής Αναφοράς")
        msg.setText("Δεν έχει εισαχθεί περιγραφή. Παρακαλώ συμπληρώστε ξανά.")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.exec_()

class MainScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.welcome_message = QtWidgets.QLabel("Welcome to Move-around!")
        self.button_report_issue = QtWidgets.QPushButton("Report Issue")
        self.button_access_map = QtWidgets.QPushButton("Access Map")

        self.button_report_issue.clicked.connect(self.on_report_issue_clicked)
        self.button_access_map.clicked.connect(self.on_access_map_clicked)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.welcome_message)
        self.layout.addWidget(self.button_report_issue)
        self.layout.addWidget(self.button_access_map)
        self.setLayout(self.layout)
        self.resize(400, 300)

    def on_report_issue_clicked(self):
        choose_location_screen = ChooseLocationScreen()
        app.show_screen(choose_location_screen)

    def on_access_map_clicked(self):
        access_map_screen = AccessMapScreen()
        app.show_screen(access_map_screen)


class Application(QtWidgets.QWidget):
    def __init__(self, ):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.widget = None
        self.setLayout(self.layout)
        self.resize(400, 300)

    def show_screen(self, widget):
        if self.widget is not None:
            self.layout.removeWidget(self.widget)
            self.widget.close()

        self.widget = widget
        self.layout.addWidget(self.widget)
        self.layout.update()


if __name__=='__main__':
    qapp = QtWidgets.QApplication([])

    app = Application()
    app.resize(400, 300)
    app.show()

    main_screen = MainScreen()
    app.show_screen(main_screen)

    sys.exit(qapp.exec_())
