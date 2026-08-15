import sys
import os
import subprocess
import webbrowser

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QMessageBox,
    QScrollArea,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class HelpWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def open_email(self, email):
        try:
            webbrowser.open(f"mailto:{email}")
        except Exception as e:
            QMessageBox.warning(
                self,
                "Unable to Open Email",
                f"Could not open your email application.\n\n{e}"
            )

    def open_dashboard(self):
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dashboard_path = os.path.join(base_dir, "test.py")

            if not os.path.exists(dashboard_path):
                QMessageBox.warning(
                    self,
                    "File Not Found",
                    "The dashboard file could not be found."
                )
                return

            subprocess.Popen([sys.executable, dashboard_path], cwd=base_dir)
            self.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Could not open the dashboard.\n\n{e}"
            )

    def create_email_card(self, name, email):
        card = QFrame()
        card.setStyleSheet(
            """
            QFrame {
                background-color: #243547;
                border: 1px solid #32475e;
                border-radius: 10px;
            }
            """
        )

        layout = QHBoxLayout(card)
        layout.setContentsMargins(18, 12, 18, 12)

        icon = QLabel("✉")
        icon.setFont(QFont("Segoe UI", 18))
        icon.setStyleSheet("color: #3498db; border: none;")
        icon.setFixedWidth(35)
        layout.addWidget(icon)

        text_layout = QVBoxLayout()
        name_label = QLabel(name)
        name_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        name_label.setStyleSheet("color: #ffffff; border: none;")

        email_label = QLabel(email)
        email_label.setFont(QFont("Segoe UI", 10))
        email_label.setStyleSheet("color: #8c9fae; border: none;")

        text_layout.addWidget(name_label)
        text_layout.addWidget(email_label)
        layout.addLayout(text_layout)

        layout.addStretch()

        contact_button = QPushButton("Contact")
        contact_button.setFixedSize(90, 36)
        contact_button.setStyleSheet(
            """
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0062a3;
            }
            """
        )
        contact_button.clicked.connect(lambda: self.open_email(email))
        layout.addWidget(contact_button)

        return card

    def create_faq(self, question, answer):
        card = QFrame()
        card.setStyleSheet(
            """
            QFrame {
                background-color: #1e2d3b;
                border: 1px solid #2c4053;
                border-radius: 8px;
            }
            """
        )

        layout = QVBoxLayout(card)
        layout.setContentsMargins(15, 12, 15, 12)

        question_label = QLabel(question)
        question_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        question_label.setStyleSheet("color: #ffffff; border: none;")

        answer_label = QLabel(answer)
        answer_label.setWordWrap(True)
        answer_label.setFont(QFont("Segoe UI", 9))
        answer_label.setStyleSheet("color: #8c9fae; border: none;")

        layout.addWidget(question_label)
        layout.addWidget(answer_label)

        return card

    def init_ui(self):
        self.setWindowTitle("Help & Support")
        self.resize(900, 700)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #1a2936;
                color: #ffffff;
                font-family: 'Segoe UI';
            }
            QScrollBar:vertical {
                background: #15222e;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #32475e;
                border-radius: 4px;
            }
            """
        )

        # Base Layout
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(0, 0, 0, 0)

        # Scrollable Outer Shell
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        scroll_content = QWidget()
        main_layout = QVBoxLayout(scroll_content)
        main_layout.setContentsMargins(35, 25, 35, 25)
        main_layout.setSpacing(18)

        # Header
        header = QFrame()
        header.setStyleSheet(
            """
            QFrame {
                background-color: #15222e;
                border-radius: 12px;
                border: 1px solid #243547;
            }
            """
        )

        header_layout = QVBoxLayout(header)
        header_layout.setContentsMargins(25, 20, 25, 20)

        title = QLabel("Help & Support")
        title.setFont(QFont("Segoe UI", 25, QFont.Weight.Bold))
        title.setStyleSheet("color: #ffffff; border: none;")

        subtitle = QLabel("Need help with the Classroom Management System?")
        subtitle.setFont(QFont("Segoe UI", 11))
        subtitle.setStyleSheet("color: #8c9fae; border: none;")

        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        main_layout.addWidget(header)

        # Contacts Section
        support_title = QLabel("Contact & Support")
        support_title.setFont(QFont("Segoe UI", 15, QFont.Weight.Bold))
        support_title.setStyleSheet("color: #ffffff;")
        main_layout.addWidget(support_title)

        support_text = QLabel(
            "For technical problems, account issues, attendance problems, "
            "or general questions about the application, contact one of "
            "the support members below."
        )
        support_text.setWordWrap(True)
        support_text.setFont(QFont("Segoe UI", 10))
        support_text.setStyleSheet("color: #8c9fae;")
        main_layout.addWidget(support_text)

        emails = [
            ("Support Team", "irajmadhav061@gmail.com"),
            ("Support Team", "hellopratik2021@gmail.com"),
            ("Support Team", "kaflealdrin@gmail.com"),
            ("Support Team", "pandeyaayush978@gmail.com"),
        ]

        for name, email in emails:
            main_layout.addWidget(self.create_email_card(name, email))

        # FAQ Section
        faq_title = QLabel("Quick Help")
        faq_title.setFont(QFont("Segoe UI", 15, QFont.Weight.Bold))
        faq_title.setStyleSheet("color: #ffffff;")
        main_layout.addWidget(faq_title)

        faqs = [
            (
                "Attendance is not being marked.",
                "Make sure the barcode/QR scanner is connected and that "
                "the attendance system is running properly."
            ),
            (
                "The application is not opening.",
                "Restart the application and make sure all required Python "
                "files are located in the correct project folder."
            ),
            (
                "I need further assistance.",
                "Use the Contact buttons above to send an email directly "
                "to the support team."
            )
        ]

        for q, a in faqs:
            main_layout.addWidget(self.create_faq(q, a))

        # Footer Button
        footer = QHBoxLayout()
        footer.addStretch()

        back_button = QPushButton("← Back to Dashboard")
        back_button.setFixedSize(180, 42)
        back_button.setStyleSheet(
            """
            QPushButton {
                background-color: #243547;
                color: #ffffff;
                border: 1px solid #32475e;
                border-radius: 7px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2d4358;
                border-color: #3498db;
            }
            """
        )
        back_button.clicked.connect(self.open_dashboard)
        footer.addWidget(back_button)

        main_layout.addLayout(footer)

        scroll_area.setWidget(scroll_content)
        root_layout.addWidget(scroll_area)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())
