import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class BrowserTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)


class TabBar(QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

    def close_tab(self, index):
        self.parent().close_tab(index)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tabs = []
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        self.new_tab()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # newtabs
        new_tab_btn = QAction('+', self)
        new_tab_btn.triggered.connect(self.new_tab)
        navbar.addAction(new_tab_btn)

        # close tabs
        close_tab_btn = QAction('×', self)
        close_tab_btn.triggered.connect(self.close_current_tab)
        navbar.addAction(close_tab_btn)

        # back button
        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.current_browser().back)
        navbar.addAction(back_btn)

        # forward button
        forward_btn = QAction('→', self)
        forward_btn.triggered.connect(self.current_browser().forward)
        navbar.addAction(forward_btn)

        # reload button
        reload_btn = QAction('↻', self)
        reload_btn.triggered.connect(self.current_browser().reload)
        navbar.addAction(reload_btn)

        # home button
        home_btn = QAction('🏠', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # fb button
        facebook_btn = QAction('f', self)
        facebook_btn.triggered.connect(self.navigate_home2)
        navbar.addAction(facebook_btn)

        # history button
        history_btn = QAction('H', self)
        history_btn.triggered.connect(self.show_history)
        navbar.addAction(history_btn)

        # instagram button
        insta_btn = QAction('I', self)
        insta_btn.triggered.connect(self.insta_gram)
        navbar.addAction(insta_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.history = []

    def current_browser(self):
        return self.current_tab().browser

    def current_tab(self):
        return self.tab_widget.currentWidget()

    # homepage
    def navigate_home(self):
        self.current_browser().setUrl(QUrl('https://google.com'))

    # facebook page
    def navigate_home2(self):
        self.current_browser().setUrl(QUrl('https://facebook.com'))

    # instagram page
    def insta_gram(self):
        self.current_browser().setUrl(QUrl('https://instagram.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.current_browser().setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def add_to_history(self, q):
        self.history.append(q.toString())

    def new_tab(self):
        tab = BrowserTab()
        index = self.tab_widget.addTab(tab, "New Tab")
        self.tab_widget.setCurrentIndex(index)

    def close_current_tab(self):
        index = self.tab_widget.currentIndex()
        if index != -1:
            self.tabs.pop(index)
            self.tab_widget.removeTab(index)

    def show_history(self):
        # Create a dialog to display the history
        dialog = QDialog(self)
        dialog.setWindowTitle("History")

        layout = QVBoxLayout()

        # Create a list widget to display the history items
        history_list = QListWidget(dialog)
        history_list.addItems(self.history)

        layout.addWidget(history_list)
        dialog.setLayout(layout)

        # Show the dialog
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
