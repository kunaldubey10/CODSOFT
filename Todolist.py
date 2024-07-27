import sys
from PyQt5.QtWidgets import QApplication, QLineEdit,QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.resize(700, 500)

        screen_geometry = QApplication.desktop().screenGeometry()
        self.move((screen_geometry.width() - self.width()) // 2, (screen_geometry.height() - self.height()) // 2)


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.label = QLabel("To-Do List", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Raleway", 16, QFont.Bold)) 
        self.label.setFont(self.label.font())  
        self.label.setStyleSheet("font-size: 18pt;") 
        

        self.task_entry = QLineEdit(self)
        self.add_button = QPushButton("Add Task", self)
        self.add_button.setFont(self.add_button.font())
        self.add_button.setStyleSheet("font-size: 12pt;")
        self.task_list = QListWidget(self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.task_entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_list)
        central_widget.setLayout(layout)

        self.add_button.clicked.connect(self.add_task)

        self.task_list.itemDoubleClicked.connect(self.remove_task)

    def add_task(self):
        task = self.task_entry.text()
        if task:
            item = QListWidgetItem(task)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked) 
            self.task_list.addItem(item)
            self.task_entry.clear()
    def remove_task(self, item):
        row = self.task_list.row(item)
        self.task_list.takeItem(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
