import sys
import polar_bar
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGroupBox, QFormLayout, QSpinBox, QDoubleSpinBox, QLabel, QLineEdit, QErrorMessage
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Personality Grapher'
        self.left = 100
        self.right = 100
        self.top = 10
        self.width = 500
        self.height = 500
        self.init_ui()

    def init_ui(self):
        # set window title, size and position
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.width, self.height)

        # create the main layout
        self.main_layout = QVBoxLayout()
        self.error_message = QErrorMessage()

        # add a form with spin boxes
        self.create_formbox()
        self.main_layout.addWidget(self.form_groupbox)

        # add an options box for the graph
        self.create_optionsbox()
        self.main_layout.addWidget(self.options_groupbox)

        # add render button
        render_button = QPushButton('Render Graph', self)
        render_button.setToolTip('Render the personality graph and display it')
        render_button.clicked.connect(self.render_click)
        self.main_layout.addWidget(render_button)

        # finally, display the window
        self.setLayout(self.main_layout)
        self.show()

    def create_formbox(self):
        self.form_groupbox = QGroupBox('Personality Traits')
        self.form_layout = QFormLayout()

        addrow_button = QPushButton('Add Trait', self)
        addrow_button.setToolTip('Add a new section to the graph')
        addrow_button.clicked.connect(self.addrow_click)

        self.form_layout.addRow(QLabel('Trait'), QLabel('Value'))
        self.form_layout.addRow(QLineEdit(), QDoubleSpinBox(decimals=5, maximum=10))
        self.form_layout.addRow(addrow_button)

        self.form_groupbox.setLayout(self.form_layout)

    def create_optionsbox(self):
        self.options_groupbox = QGroupBox('Graph Options')
        self.options_layout = QFormLayout()

        self.ceiling_text = QDoubleSpinBox(decimals=5, value=10.00)
        self.ceiling_text.valueChanged.connect(self.ceiling_changed)

        self.options_layout.addRow(QLabel('Graph Name'), QLineEdit())
        self.options_layout.addRow(QLabel('Max Value'), self.ceiling_text)
        self.options_layout.addRow(QLabel('Height/Width'), QSpinBox(value=6, minimum=1))
        self.options_layout.addRow(QLabel('Padding'), QSpinBox(value=4))
        self.options_layout.addRow(QLabel('Font Size'), QSpinBox(value=12, minimum=1))

        self.options_groupbox.setLayout(self.options_layout)

    # calls the render_graph function to render and then display the graph
    @pyqtSlot()
    def render_click(self):
        input_values = []
        input_names = []
        name = self.options_groupbox.children()[2].text().strip()
        padding = self.options_groupbox.children()[8].value()
        size = self.options_groupbox.children()[6].value()
        font = self.options_groupbox.children()[10].value()
        max = self.options_groupbox.children()[4].value()

        if len(self.form_groupbox.children()) == 3:
            # if the user has not added any sections, warn them
            self.error_message.showMessage('Cannot graph with no sections!')
        elif size < 1:
            self.error_message.showMessage('Height/Width must be greater than 0!')
        else:
            # get values from input boxes and pass them into graphing function
            children = self.form_groupbox.findChildren(QLineEdit)
            count = 0
            while count < len(children):
                input_names.append(children[count].text())
                count += 1
                input_values.append(float(children[count].text()))
                count += 1

            result = polar_bar.render_graph(name=name, section_names=input_names, value_list=input_values, padding=padding, max=max, size=size, font=font)
            if result is False:
                self.error_message.showMessage('Padding too big for Height/Width!')

    @pyqtSlot()
    def addrow_click(self):
        self.form_layout.insertRow(self.form_layout.rowCount() - 1, QLineEdit(), QDoubleSpinBox(decimals=5, maximum=float(self.ceiling_text.value())))

    @pyqtSlot()
    def ceiling_changed(self):
        for i in self.form_groupbox.findChildren(QDoubleSpinBox):
            i.setMaximum(float(self.ceiling_text.value()))


def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


main()
