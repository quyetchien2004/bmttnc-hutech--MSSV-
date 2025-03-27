import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_CaesarCipher

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CaesarCipher()
        self.ui.setupUi(self)

        # Kết nối nút bấm với hàm xử lý
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)  # Encrypt
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)  # Decrypt

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plainTextEdit.toPlainText(),  # Đúng tên widget
            "key": self.ui.plainTextEdit_2.toPlainText()  # Đúng tên widget
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_3.setPlainText(data["encrypted_message"])  # Đúng tên widget

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_3.toPlainText(),  # Đúng tên widget
            "key": self.ui.plainTextEdit_2.toPlainText()  # Đúng tên widget
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data["decrypted_message"])  # Đúng tên widget

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())