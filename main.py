import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class WebcamStreamApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam Stream")
        self.setGeometry(100, 100, 640, 480)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.video_label)
        self.central_widget.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30 milliseconds
        # self.video_path = 'vid.mp4'
        self.cap = cv2.VideoCapture(0)
        # self.cap = cv2.VideoCapture(self.video_path)

        

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(
                frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888
            )
            pixmap = QPixmap.fromImage(image)
            self.video_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebcamStreamApp()
    window.show()
    sys.exit(app.exec_())
