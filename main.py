import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MinimalBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webiny Browser")
        self.setGeometry(100, 100, 1024, 768)

        # Create the web view
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        # Create the navigation toolbar
        nav_toolbar = QToolBar()
        self.addToolBar(nav_toolbar)

        # Back button
        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.web_view.back)
        nav_toolbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('→', self)
        forward_btn.triggered.connect(self.web_view.forward)
        nav_toolbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('↻', self)
        reload_btn.triggered.connect(self.web_view.reload)
        nav_toolbar.addAction(reload_btn)

        # Address bar
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)
        nav_toolbar.addWidget(self.address_bar)

        # Update address bar when URL changes
        self.web_view.urlChanged.connect(self.update_address_bar)

        # Load a default page
        self.web_view.setUrl(QUrl("https://www.duckduckgo.com"))

    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.web_view.setUrl(QUrl(url))

    def update_address_bar(self, url):
        self.address_bar.setText(url.toString())

def main():
    app = QApplication(sys.argv)
    browser = MinimalBrowser()
    browser.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()