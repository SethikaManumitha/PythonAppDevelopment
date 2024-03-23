#import necessary libraries
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QHBoxLayout,QVBoxLayout,QPushButton,QLineEdit

#Main App
class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.title = "Calculator"
        self.setWindowTitle(self.title)
        self.resize(250,300)


        #create widgets
        self.EditField = QLineEdit()
        self.grid = QGridLayout()

        self.buttons = ["7","8","9","/",
                "4","5","6","*",
                "1","2","3","-",
                "0",".","=","+"
        ]

        self.clear = QPushButton("AC")
        self.delete = QPushButton("DEL")

        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button,row,col)
            col +=1

            if col>3:
                col = 0
                row += 1
        
        master_layout = QVBoxLayout()
        button_row = QHBoxLayout()
       
      
        master_layout.addWidget(self.EditField)
        master_layout.addLayout(self.grid)
        master_layout.addLayout(button_row)
        self.setLayout(master_layout)
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)
    
    def button_click(self):
        button = app.sender()
        text = button.text()
        if text == "=":
            symbol = self.EditField.text()
            
            try: 
                res = eval(symbol)
                self.EditField.clear()
                self.EditField.setText(str(res))
            
            except Exception as e:
                print(f"Error {e}")

        elif text == "AC":
            self.EditField.clear()

        elif text == "DEL":
            current_value  =self.EditField.text()
            self.EditField.setText(current_value[:-1])
        
        else:
            current_value = self.EditField.text()
            self.EditField.setText(current_value + text)
    
#run app
if __name__ in "__main__":
    app = QApplication([])
    main_Window = CalcApp()
    main_Window.show()
    app.exec_()


    