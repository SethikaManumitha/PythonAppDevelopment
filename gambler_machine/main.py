from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from random import choice

# Main app
app = QApplication([])
credit = 300
wins  = 0
title = "Gamblers Gambit"

# Create main window
main_window = QWidget()
main_window.setWindowTitle(title)
main_window.resize(400, 300)

# Widgets
title_label = QLabel(title)
title_label.setFont(QFont("Arial", 16))

moneyInfo = QLabel(f"${credit} left")
moneyInfo.setFont(QFont("Arial",15))

winCount = QLabel(f"won {wins} times")
winCount.setFont(QFont("Arial",15))

word_labels = [QLabel("?") for _ in range(3)]
for label in word_labels:
    label.setFont(QFont("Arial", 14))  # Increase font size for each word label

button = QPushButton("Click Me!!")

# Layouts
master_layout = QVBoxLayout()
row_layouts = [QHBoxLayout() for _ in range(4)]

# Add widgets to layouts
row_layouts[0].addWidget(moneyInfo)
row_layouts[0].addWidget(winCount,alignment=Qt.AlignRight)
row_layouts[1].addWidget(title_label, alignment=Qt.AlignCenter)
for label in word_labels:
    row_layouts[2].addWidget(label, alignment=Qt.AlignCenter)
row_layouts[3].addWidget(button)

for layout in row_layouts:
    master_layout.addLayout(layout)

main_window.setLayout(master_layout)

# Event handling functions
my_words = ["🍒", "💰", "😶", "🍒", "💰", "💰","😶","🍒","😶","😴","😴","😴","🍑","🍑","🍑"]

def set_random_word(labels):
    global credit,wins
    for label in labels:
        word = choice(my_words)
        label.setText(word)
    
    if len(set(label.text() for label in labels)) == 1:
        QMessageBox.information(main_window, "Congratulations!", "You win!")
        credit += 100
        moneyInfo.setText(f"${credit} left")
        wins += 1
        winCount.setText(f"won {wins} time")
    else:
        credit -= 10
        moneyInfo.setText(f"${credit} left")

    if credit == 0:
        QMessageBox.information(main_window, "Oh Oh!", "No More Money Left")


button.clicked.connect(lambda: set_random_word(word_labels))

# Show the app
main_window.show()
app.exec_()
