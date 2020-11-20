import sys
from PyQt5 import QtWidgets

class USD_Controller:

    # Define all function here
    def open_file_from(self):
        self.label_from_filename.setText(self.get_file())
        self.label_from_filename.setVisible(True)

    def open_file_to(self):
        self.label_to_filename.setText(self.get_file())
        self.label_to_filename.setVisible(True)

    def get_file(self):
        the_file = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', 'c:\\')
        if the_file:
            return the_file[0]
        else:
            return 'Error...'

    def execute(self):
        print('EXECUTE!')
        print(self.combo_box.currentText())
        print(self.label_from_filename.text())
        print(self.label_to_filename.text())

    def build(self):
        # Create core objects
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        box = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # Set base settings
        window.setCentralWidget(box)
        box.setLayout(layout)

        # Create controls
        self.combo_box = QtWidgets.QComboBox()
        self.combo_box.addItems([
            "Animation",
            "Camera",
            "Fur",
            "Layout",
            "Lighting",
            "Model",
            "Shading",
            "VFX"
        ])

        button_select_file_from = QtWidgets.QPushButton('Select File...')
        button_select_file_from.clicked.connect(self.open_file_from)
        button_select_file_to = QtWidgets.QPushButton('Select File...')
        button_select_file_to.clicked.connect(self.open_file_to)

        button_execute = QtWidgets.QPushButton('EXECUTE')
        button_execute.clicked.connect(self.execute)

        label_from_file = QtWidgets.QLabel('FROM this file:')
        self.label_from_filename = QtWidgets.QLabel()
        self.label_from_filename.setEnabled(False)
        self.label_from_filename.setVisible(False)
        label_department = QtWidgets.QLabel('LAYER the:')
        label_to_file = QtWidgets.QLabel('ONTO this file:')
        self.label_to_filename = QtWidgets.QLabel()
        self.label_to_filename.setEnabled(False)
        self.label_to_filename.setVisible(False)
        label_confirm = QtWidgets.QLabel('Make sure your settings are correct before executing...')

        # Add controls
        layout.addWidget(label_from_file)
        layout.addWidget(self.label_from_filename)
        layout.addWidget(button_select_file_from)
        layout.addWidget(label_department)
        layout.addWidget(self.combo_box)
        layout.addWidget(label_to_file)
        layout.addWidget(self.label_to_filename)
        layout.addWidget(button_select_file_to)

        layout.addWidget(label_confirm)
        layout.addWidget(button_execute)

        window.show()
        sys.exit(app.exec_())

USD_Controller().build()