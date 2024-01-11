import time
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QPixmap
from graphics import SimplePendulumRenderer
from simple_pendulum import SimplePendulumSimulation
from ui.main_window_ui import Ui_MainWindow
import sys
from PIL.ImageQt import ImageQt
from threading import Thread

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def test_anim(window: MainWindow):
    time.sleep(5)

    s = SimplePendulumSimulation(10, 1.5)
    g = SimplePendulumRenderer(length=10)
    d = window.ui.lblDisplay

    s.precalculate_positions(0.001)
    for pos in s.get_weight_coordinates():
        d.setPixmap(QPixmap.fromImage(ImageQt(g.draw_frame(pos))))
        time.sleep(0.1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    foo = Thread(target=test_anim, args=[window])
    foo.start()

    sys.exit(app.exec())