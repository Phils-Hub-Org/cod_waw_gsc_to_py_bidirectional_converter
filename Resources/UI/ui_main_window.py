# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowYohhKK.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)
import Resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 720)
        MainWindow.setMinimumSize(QSize(1120, 720))
        MainWindow.setStyleSheet(u"/* Central Widget */\n"
"QWidget#centralwidget {\n"
"    background-color: #1e1e1e;  /* Dark gray background */\n"
"}\n"
"\n"
"/* QMenuBar */\n"
"QMenuBar {\n"
"    background-color: #2e2e2e;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text */\n"
"    border-bottom: 1px solid #5b5e60;  /* Light gray border for separation */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent; /* Transparent background */\n"
"    padding: 6px 6px;             /* Padding for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"}\n"
"\n"
"QMenuBar::item:selected {          /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenuBar::item:pressed {           /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"/* QMen"
                        "u */\n"
"QMenu {\n"
"    background-color: #2e2e2e;     /* Dark gray background for menus */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent; /* Transparent background for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"	padding: 6px;\n"
"    margin-left: 6px;             /* Padding for each menu item */\n"
"}\n"
"\n"
"QMenu::item:selected {             /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue background on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::item:pressed {              /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue background on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #5b5e60;     /* Light gray separator between items */\n"
"}\n"
"\n"
"/* QMenu::indicato"
                        "r (checkboxes and radio buttons in menus) */\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    background-color: #2e2e2e;     /* Dark gray background for indicators */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"    border-radius: 2px;            /* Slightly rounded corners */\n"
"}\n"
"\n"
"QMenu::indicator:checked {\n"
"    background-color: #4a90e2;     /* Light blue when checked */\n"
"    border-color: #3d78b2;         /* Darker blue border when checked */\n"
"}\n"
"\n"
"QMenu::indicator:unchecked {\n"
"    background-color: #2e2e2e;     /* Keep the dark gray when unchecked */\n"
"    border-color: #5b5e60;         /* Light gray border when unchecked */\n"
"}\n"
"\n"
"/* QToolBar */\n"
"QToolBar {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    padding: 4px;                   /* Padding inside the toolbar */\n"
"    spacing: 4px;                   /* Spacing between too"
                        "lbar buttons */\n"
"}\n"
"\n"
"QToolBar::handle {\n"
"    background-color: #5b5e60;      /* Light gray handle for draggable toolbars */\n"
"    width: 10px;                    /* Width of the handle */\n"
"	height: 10px;\n"
"    margin: 4px;                    /* Margin around the handle */\n"
"}\n"
"\n"
"QToolBar::separator {\n"
"    background-color: #5b5e60;      /* Light gray for separators */\n"
"    width: 1px;                     /* Thickness of the separator */\n"
"    height: 24px;                   /* Height of the separator */\n"
"    margin: 6px;                    /* Space around the separator */\n"
"}\n"
"\n"
"QToolBar::item {\n"
"    padding: 4px;                   /* Padding for individual toolbar items */\n"
"}\n"
"\n"
"/* QStatusBar */\n"
"QStatusBar {\n"
"    background-color: #2e2e2e;   /* Dark gray background */\n"
"    border-top: 1px solid #5b5e60; /* Light gray top border for separation */\n"
"    color: #ffffff;              /* White text */\n"
"    font-size: 13px;             /* Sli"
                        "ghtly smaller font for the status bar */\n"
"    padding: 6px;                /* Padding inside the status bar */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;                /* No border around individual status items */\n"
"    padding: 0px 5px;            /* Padding between status bar items */\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"    color: #ffffff;              /* White text for any QLabel inside the status bar */\n"
"    background-color: transparent; /* Ensure QLabel in status bar matches the bar's background */\n"
"}\n"
"\n"
"QStatusBar::indicator {\n"
"    background-color: #4a90e2;   /* Optional indicator styling, e.g., for icons or status signals */\n"
"    border-radius: 4px;          /* Rounded corners for any indicator elements */\n"
"}\n"
"\n"
"/* Scroll Area Styling (optional) */\n"
"QScrollArea {\n"
"    background-color: transparent; /* Transparent to match the central widget */\n"
"    border: none;                  /* No border */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    back"
                        "ground-color: #3c3f41;    /* Darker gray for scroll bar background */\n"
"    width: 12px;                  /* Scroll bar width */\n"
"    margin: 22px 0 22px 0;        /* Top and bottom margins */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5b5e60;    /* Slightly lighter gray for scroll handle */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;             /* Remove arrows */\n"
"}\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    color: #ffffff;             /* White text */\n"
"    font-size: 14px;            /* Set font size */\n"
"}\n"
"\n"
"/* QFrame */\n"
"QFrame {\n"
"    background-color: #2e2e2e;  /* Dark gray for frames */\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #2e2e2e;  /* Dark gray background for input fields */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rou"
                        "nded corners */\n"
"    padding: 6px;               /* Padding for text input area */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border when focused */\n"
"    background-color: #333333;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #2b2b2b;  /* Darker gray background for text area */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 0px;         /* No rounded corners */\n"
"    padding: 10px;              /* Comfortable padding for text input */\n"
"    font-size: 13px;            /* Slightly smaller font */\n"
"    line-height: 1.4;           /* Adjust line spacing for readability */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border on focus */\n"
"    background-color: #3a3a3a;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
""
                        "    background-color: #3c3f41;  /* Dark gray background */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"    padding: 6px 12px;          /* Padding for comfortable button size */\n"
"    font-size: 14px;            /* Button text size */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4a90e2;  /* Light blue on hover */\n"
"    border-color: #3d78b2;      /* Darker blue border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;  /* Darker blue on press */\n"
"    border-color: #2a5f92;      /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* QRadioButton */\n"
"QRadioButton {\n"
"    color: #ffffff;              /* White text */\n"
"    font-size: 14px;             /* Font size for readability */\n"
"    spacing: 5px;                /* Space between radio button and label */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;         "
                        "        /* Size of the radio button */\n"
"    height: 16px;\n"
"    background-color: #2e2e2e;   /* Dark gray background for the indicator */\n"
"    border: 1px solid #5b5e60;   /* Light gray border */\n"
"    border-radius: 8px;          /* Circular radio button */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: #4a90e2;   /* Light blue on hover */\n"
"    border-color: #3d78b2;       /* Darker blue border on hover */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4a90e2;   /* Light blue when checked */\n"
"    border-color: #3d78b2;       /* Darker blue border when checked */\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue on press */\n"
"    border-color: #2a5f92;       /* Even darker border on press */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue when checked and pressed */\n"
"    border-color: #2a5f92;       /* Even darker border when"
                        " checked and pressed */\n"
"}\n"
"\n"
"/* QToolButton */\n"
"QToolButton {\n"
"    background-color: #3c3f41;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text/icon */\n"
"    border: 1px solid #5b5e60;    /* Light gray border */\n"
"    border-radius: 4px;           /* Rounded corners */\n"
"    padding: 6px 12px;            /* Padding for comfortable button size */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #4a90e2;    /* Light blue background on hover */\n"
"    border-color: #3d78b2;        /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #3d78b2;    /* Darker blue background on press */\n"
"    border-color: #2a5f92;        /* Even darker border when pressed */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #3d78b2;    /* Darker blue when checked */\n"
"    border-color: #2a5f92;        /* Border color when checked */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #2e2e2e;    "
                        "/* Dark gray when disabled */\n"
"    color: #777777;               /* Lighter gray text/icon for disabled state */\n"
"    border-color: #5b5e60;        /* Keep the border color same as normal state */\n"
"}\n"
"\n"
"/* QToolButton::menu-button */\n"
"QToolButton::menu-button {\n"
"    background-color: #3c3f41;      /* Dark gray background for menu button */\n"
"    border: 1px solid #5b5e60;      /* Light gray border for menu button */\n"
"    padding: 4px;                   /* Padding for the menu button */\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"    background-color: #4a90e2;      /* Light blue on hover */\n"
"    border-color: #3d78b2;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton::menu-button:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
"    border-color: #2a5f92;          /* Even darker border on press */\n"
"}\n"
"")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {margin: 6px;}")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"QFrame {margin: 0px;}")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 9)
        self.gsc_code_input_area = QPlainTextEdit(self.frame_5)
        self.gsc_code_input_area.setObjectName(u"gsc_code_input_area")
        self.gsc_code_input_area.setFrameShape(QFrame.Shape.NoFrame)
        self.gsc_code_input_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.gsc_code_input_area.setTabStopDistance(16.000000000000000)

        self.horizontalLayout_4.addWidget(self.gsc_code_input_area)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.convert_gsc_to_py_btn = QPushButton(self.frame)
        self.convert_gsc_to_py_btn.setObjectName(u"convert_gsc_to_py_btn")
        icon = QIcon()
        icon.addFile(u":/888EAC-20px/ICONS/888EAC-20px/arrow-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.convert_gsc_to_py_btn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.convert_gsc_to_py_btn)

        self.convert_py_to_gsc_btn = QPushButton(self.frame)
        self.convert_py_to_gsc_btn.setObjectName(u"convert_py_to_gsc_btn")
        icon1 = QIcon()
        icon1.addFile(u":/888EAC-20px/ICONS/888EAC-20px/arrow-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.convert_py_to_gsc_btn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.convert_py_to_gsc_btn)


        self.horizontalLayout_4.addWidget(self.frame)

        self.python_code_input_area = QPlainTextEdit(self.frame_5)
        self.python_code_input_area.setObjectName(u"python_code_input_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.python_code_input_area.sizePolicy().hasHeightForWidth())
        self.python_code_input_area.setSizePolicy(sizePolicy1)
        self.python_code_input_area.setFrameShape(QFrame.Shape.NoFrame)
        self.python_code_input_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.python_code_input_area.setTabStopDistance(16.000000000000000)

        self.horizontalLayout_4.addWidget(self.python_code_input_area)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1120, 29))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Phils-Hub - GSC > Py Bidirectional Converter", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GSC", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PYTHON", None))
        self.gsc_code_input_area.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste gsc code here to convert to python", None))
#if QT_CONFIG(tooltip)
        self.convert_gsc_to_py_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Convert gsc to py", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.convert_py_to_gsc_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Convert py to gsc", None))
#endif // QT_CONFIG(tooltip)
        self.python_code_input_area.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste python code here to convert to gsc", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

