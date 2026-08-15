#student panel
import sys
import os
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QTableWidget, QTableWidgetItem, QHeaderView, QFrame, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont
from database import process_scan 


class BarcodeListenerThread(QThread):
    scan_received = pyqtSignal(str)

    def run(self):
        print("==================================================")
        print(" Smartboard Barcode Attendance Listener (Active) ")
        print("==================================================")
        print("Listening for scans... (Press Ctrl+C to stop)\n")

        while True:
            try:
                scanned_code = sys.stdin.readline().strip()
                if scanned_code:
                    process_scan(scanned_code)
                    self.scan_received.emit(scanned_code)
            except (KeyboardInterrupt, Exception):
                print("\nShutting down attendance listener.")
                break


class ClassroomDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.start_listener()

    def start_listener(self):
        self.listener_thread = BarcodeListenerThread()
        self.listener_thread.start()

    def open_cal(self):
        cal_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cal.py")
        subprocess.Popen([sys.executable, cal_path], cwd=os.path.dirname(cal_path))
        self.close()

    def open_db(self):
        subprocess.Popen([sys.executable, "database.py"])
        self.close()

    def open_help(self):
        # Launch help.py and completely terminate test.py
        help_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "help.py")
        subprocess.Popen([sys.executable, help_path], cwd=os.path.dirname(help_path))
        QApplication.quit()
        sys.exit()

    def handle_logout(self):
        reply = QMessageBox.question(self, 'Confirm Logout', 'Are you sure you want to log out?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            admin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "adminpage.py")
            subprocess.Popen([sys.executable, admin_path], cwd=os.path.dirname(admin_path))
            self.close()
            QApplication.quit()
            sys.exit()
            

        if reply == QMessageBox.StandardButton.Yes:
            # Launch adminpage.py and completely terminate test.py
            admin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "adminpage.py")
            subprocess.Popen([sys.executable, admin_path], cwd=os.path.dirname(admin_path))
            QApplication.quit()
            sys.exit()

    def init_ui(self):
        self.setWindowTitle("Classroom Display System")
        self.resize(1100, 650)
        self.setStyleSheet("background-color: #1a2936; color: #ffffff; font-family: 'Segoe UI', sans-serif;")
        
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        sidebar = QFrame()
        sidebar.setFixedWidth(70)
        sidebar.setStyleSheet("background-color: #15222e; border-right: 1px solid #243547;")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)
        sidebar_layout.setSpacing(15)
        
        btn_bell = QPushButton("🔔")
        btn_home = QPushButton("🏠")
        btn_cal = QPushButton("📅")
        btn_group = QPushButton("👥")
        btn_settings = QPushButton("⚙️")
        
        btn_cal.clicked.connect(self.open_cal)
        
        nav_buttons = [btn_bell, btn_home, btn_cal, btn_group, btn_settings]
        for btn in nav_buttons:
            btn.setFixedSize(50, 45)
            btn.setFont(QFont("Segoe UI", 12))
            btn.setStyleSheet(
                "QPushButton { background-color: transparent; color: #8c9fae; border-radius: 8px; border: none; } "
                "QPushButton:hover { background-color: #243547; color: #ffffff; }"
            )
            sidebar_layout.addWidget(btn)
            
        btn_home.setStyleSheet("background-color: #2a3e52; color: #3498db; border-radius: 8px;")
        sidebar_layout.addStretch()
        main_layout.addWidget(sidebar)
        
        # Main Area
        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(30, 20, 30, 20)
        content_layout.setSpacing(15)
        
        # Top Banner
        top_banner = QHBoxLayout()
        class_title = QLabel("Class 10 A")
        class_title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        class_title.setStyleSheet("color: #ffffff;")
        
        time_box = QVBoxLayout()
        clock_lbl = QLabel("09:35 AM")
        clock_lbl.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        clock_lbl.setStyleSheet("color: #a4b3c1;")
        
        date_lbl = QLabel("Friday, 09 May 2025")
        date_lbl.setFont(QFont("Segoe UI", 10))
        date_lbl.setStyleSheet("color: #6a7e90;")
        
        time_box.addWidget(clock_lbl)
        time_box.addWidget(date_lbl)
        
        attend_box = QFrame()
        attend_box.setStyleSheet("background-color: #243547; border-radius: 10px; padding: 5px;")
        attend_layout = QHBoxLayout(attend_box)
        
        btn_db = QPushButton("📱")
        btn_db.setFixedSize(40, 40)
        btn_db.setFont(QFont("Segoe UI", 18))
        btn_db.setStyleSheet(
            "QPushButton { background-color: transparent; border: none; border-radius: 6px; } "
            "QPushButton:hover { background-color: #1a2936; }"
        )
        btn_db.clicked.connect(self.open_db)
        
        att_txt = QLabel("Mark Your Attendance\nScan your code to mark present.")
        att_txt.setStyleSheet("color: #8c9fae; font-size: 11px;")
        
        attend_layout.addWidget(btn_db)
        attend_layout.addWidget(att_txt)
        
        top_banner.addWidget(class_title)
        top_banner.addStretch()
        top_banner.addLayout(time_box)
        top_banner.addSpacing(20)
        top_banner.addWidget(attend_box)
        content_layout.addLayout(top_banner)
        
        # Dashboard Cards
        top_cards_layout = QHBoxLayout()
        top_cards_layout.setSpacing(15)
        
        curr_card = QFrame()
        curr_card.setStyleSheet("background-color: #243547; border-radius: 12px;")
        curr_layout = QVBoxLayout(curr_card)
        curr_layout.setContentsMargins(20, 15, 20, 15)
        
        curr_head = QHBoxLayout()
        curr_title = QLabel("Currently")
        curr_title.setFont(QFont("Segoe UI", 11))
        curr_title.setStyleSheet("color: #8c9fae;")
        
        badge = QLabel("Ongoing")
        badge.setStyleSheet("background-color: #1e3d34; color: #2ecc71; border-radius: 10px; padding: 4px 8px; font-weight: bold; font-size: 10px;")
        
        curr_head.addWidget(curr_title)
        curr_head.addStretch()
        curr_head.addWidget(badge)
        
        period_lbl = QLabel("Period 2  •  09:30 AM - 10:15 AM")
        period_lbl.setStyleSheet("color: #6a7e90; font-size: 11px; margin-top: 4px;")
        
        subj_lbl = QLabel("Mathematics")
        subj_lbl.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        subj_lbl.setStyleSheet("color: #ffffff;")
        
        teacher_lbl = QLabel("Ms. Karki")
        teacher_lbl.setStyleSheet("color: #a4b3c1; font-size: 12px;")
        
        curr_layout.addLayout(curr_head)
        curr_layout.addWidget(period_lbl)
        curr_layout.addWidget(subj_lbl)
        curr_layout.addWidget(teacher_lbl)
        
        sub_card = QFrame()
        sub_card.setStyleSheet("background-color: #243547; border-radius: 12px;")
        sub_layout = QVBoxLayout(sub_card)
        sub_layout.setContentsMargins(20, 15, 20, 15)
        
        sub_title = QLabel("Today's Substitutions")
        sub_title.setFont(QFont("Segoe UI", 11))
        sub_title.setStyleSheet("color: #8c9fae;")
        
        sub_msg1 = QLabel("No substitutions for today.")
        sub_msg1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub_msg1.setStyleSheet("color: #6a7e90; margin-top: 15px;")
        
        sub_msg2 = QLabel("Enjoy your classes!")
        sub_msg2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub_msg2.setStyleSheet("color: #a4b3c1; font-size: 11px;")
        
        sub_layout.addWidget(sub_title)
        sub_layout.addWidget(sub_msg1)
        sub_layout.addWidget(sub_msg2)
        sub_layout.addStretch()
        
        top_cards_layout.addWidget(curr_card, 1)
        top_cards_layout.addWidget(sub_card, 1)
        content_layout.addLayout(top_cards_layout)
        
        # Schedule Table
        table_container = QFrame()
        table_container.setStyleSheet("background-color: #243547; border-radius: 12px;")
        table_box_layout = QVBoxLayout(table_container)
        table_box_layout.setContentsMargins(15, 15, 15, 15)
        
        table_head = QHBoxLayout()
        routine_lbl = QLabel("Today's Routine")
        routine_lbl.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        routine_lbl.setStyleSheet("color: #ffffff;")
        
        full_sched_lbl = QLabel("View Full Schedule")
        full_sched_lbl.setStyleSheet("color: #3498db; font-size: 11px; font-weight: bold;")
        
        table_head.addWidget(routine_lbl)
        table_head.addStretch()
        table_head.addWidget(full_sched_lbl)
        table_box_layout.addLayout(table_head)
        
        table = QTableWidget(7, 4)
        table.setHorizontalHeaderLabels(["Period", "Time", "Subject", "Teacher"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setVisible(False)
        table.setShowGrid(False)
        table.setStyleSheet(
            "QTableWidget { background-color: transparent; color: #e1e8ed; border: none; } "
            "QHeaderView::section { background-color: transparent; color: #6a7e90; font-weight: bold; border: none; padding-bottom: 8px; } "
            "QTableWidget::item { padding: 6px; border-bottom: 1px solid #1a2936; } "
            "QTableWidget::item:selected { background-color: #2c4257; color: #ffffff; }"
        )
        
        data = [
            ("1", "08:15 AM - 09:00 AM", "Science", "Mr. Thapa"),
            ("2", "09:30 AM - 10:15 AM", "Mathematics", "Ms. Karki"),
            ("3", "10:30 AM - 11:15 AM", "English", "Mr. Sharma"),
            ("4", "11:30 AM - 12:15 PM", "Social Studies", "Ms. Rai"),
            ("5", "12:30 PM - 01:15 PM", "Computer", "Mr. Adhikari"),
            ("6", "01:30 PM - 02:15 PM", "Nepali", "Ms. Gurung"),
            ("7", "02:30 PM - 03:15 PM", "Arts", "Mr. Limbu")
        ]
        
        for row, period in enumerate(data):
            for col, item in enumerate(period):
                table.setItem(row, col, QTableWidgetItem(item))
                
        table.selectRow(1)
        table_box_layout.addWidget(table)
        content_layout.addWidget(table_container)
        
        # Footer Section
        footer = QFrame()
        footer.setStyleSheet("background-color: #15222e; border-radius: 8px;")
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(15, 8, 15, 8)
        
        quote_lbl = QLabel("Discipline is the bridge between goals and achievement.")
        quote_lbl.setStyleSheet("color: #8c9fae; font-size: 11px;")
        
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(10)
        
        btn_help = QPushButton("❓ Help")
        btn_help.setStyleSheet(
            "QPushButton { background-color: #243547; color: #ffffff; border-radius: 6px; padding: 5px 12px; font-size: 11px; border: none; } "
            "QPushButton:hover { background-color: #34495e; }"
        )
        btn_help.clicked.connect(self.open_help)

        btn_logout = QPushButton("🚪 Logout")
        btn_logout.setStyleSheet(
            "QPushButton { background-color: #c0392b; color: #ffffff; border-radius: 6px; padding: 5px 12px; font-size: 11px; border: none; font-weight: bold; } "
            "QPushButton:hover { background-color: #e74c3c; }"
        )
        btn_logout.clicked.connect(self.handle_logout)

        actions_layout.addWidget(btn_help)
        actions_layout.addWidget(btn_logout)

        footer_layout.addWidget(quote_lbl)
        footer_layout.addStretch()
        footer_layout.addLayout(actions_layout)
        
        content_layout.addWidget(footer)
        main_layout.addWidget(content_area)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClassroomDashboard()
    window.show()
    sys.exit(app.exec())
