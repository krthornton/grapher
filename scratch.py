import sys
import polar_bar
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Test window'
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

        # add a render button
        self.render_button = QPushButton('Render Graph', self)
        self.render_button.setToolTip('Render the personality graph and display it')
        self.render_button.move(200, 200)
        self.render_button.clicked.connect(self.render_click)

        # add some text boxes
        self.input_list = self.make_inputs(number=6,
                                           labels=['Understanding Feelings', 'Personality by Example', 'Language',
                                                   'Numbers', 'Analytical', 'Imaginative'], posx=20, posy=20,
                                           spacing=20, length=40, height=20)

        # finally, display the window
        self.show()

    # used to generate a list of input boxes and put them anywhere in the UI
    def make_inputs(self, number, labels, posx, posy, spacing, length, height):
        input_list = []
        for i in range(number):
            name_label = QLabel(self)
            name_label.setText(labels[i])
            max_label = QLabel(self)
            max_label.setText('/ 10')
            textbox = QLineEdit('', self)
            textbox.resize(length, height)

            name_label.move(posx, posy)
            posy += 20
            textbox.move(posx, posy)
            max_label.move((posx + length + 10), posy)

            posy += (spacing + height)
            input_list.append(textbox)

        return input_list

    # calls the render_graph function to render and then display the graph
    @pyqtSlot()
    def render_click(self):
        # print(self.textbox.text())
        input_values = []
        for i in self.input_list:
            input_values.append(int(i.text()))
        polar_bar.render_graph(value_list=input_values)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

"""
# text
    ax.text(6.22, 6.5, 'Understanding\nFeelings')
    ax.text(theta[1], 6.5, 'Personality by\nExample')
    ax.text(theta[2] + 0.2, 7.8, 'Language')
    ax.text(theta[3], 8.5, 'Numbers')
    ax.text(theta[4] - 0.22, 8.1, 'Analytical')
    ax.text(theta[5], 7, 'Imaginative')
"""