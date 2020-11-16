import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox


class Ui_TicTacToe(object):
    comp_input_to_win = [
        [4, 8, 2, 6, 1, 3],
        [4, 7, 0, 2],
        [4, 6, 0, 8, 5, 1],
        [4, 5, 0, 6],
        [0, 2, 6, 8, 1, 3, 5, 7],
        [4, 3, 2, 8],
        [4, 2, 0, 8, 3, 7],
        [4, 1, 6, 8],
        [4, 0, 6, 2, 5, 7, 3, 1]
    ]

    comp_input_defend = [
        [0, 4, 8], [4, 8, 0], [0, 8, 4], [2, 4, 6], [2, 6, 4], [4, 6, 2],
        [0, 1, 2], [1, 2, 0], [0, 2, 1], [3, 4, 5], [3, 5, 4], [4, 5, 3], [6, 7, 8], [7, 8, 6], [6, 8, 7],
        [0, 3, 6], [0, 6, 3], [3, 6, 0], [1, 4, 7], [4, 7, 1], [1, 7, 4], [2, 5, 8], [5, 8, 2], [2, 8, 5]
    ]
    x_corner = [[0, 8], [2, 6]]
    game_option = 1
    winner = None
    is_game_running = True
    list_of_o = []
    list_of_x = []
    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']
    # Whose turn is it
    current_player = 'X'
    scoreX = 0
    scoreY = 0
    scoreD = 0

    def setupUi(self, TicTacToe):
        TicTacToe.setObjectName("TicTacToe")
        TicTacToe.resize(500, 500)
        TicTacToe.setMinimumSize(QtCore.QSize(400, 450))
        TicTacToe.setMaximumSize(QtCore.QSize(400, 450))
        TicTacToe.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(TicTacToe)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 316))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/blank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_0.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_0.setText("")
        self.pushButton_0.setIcon(icon)
        self.pushButton_0.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 325, 151, 100))
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(20, 360, 151, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.score.setFont(font)
        self.score.setObjectName("score")
        TicTacToe.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TicTacToe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        TicTacToe.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TicTacToe)
        self.statusbar.setObjectName("statusbar")
        TicTacToe.setStatusBar(self.statusbar)
        self.actionSingle_Player = QtWidgets.QAction(TicTacToe)
        self.actionSingle_Player.setObjectName("actionSingle_Player")
        self.actionMulti_Player = QtWidgets.QAction(TicTacToe)
        self.actionMulti_Player.setObjectName("actionMulti_Player")
        self.actionHow_to_Play = QtWidgets.QAction(TicTacToe)
        self.actionHow_to_Play.setObjectName("actionHow_to_Play")
        self.actionAbout_Game = QtWidgets.QAction(TicTacToe)
        self.actionAbout_Game.setObjectName("actionAbout_Game")
        self.actionExit = QtWidgets.QAction(TicTacToe)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSingle_Player)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMulti_Player)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionHow_to_Play)
        self.menuAbout.addAction(self.actionAbout_Game)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(TicTacToe)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe)

        self.pushButton_0.clicked.connect(lambda: self.click_button(0, icon, icon1, icon2))
        self.pushButton_1.clicked.connect(lambda: self.click_button(1, icon, icon1, icon2))
        self.pushButton_2.clicked.connect(lambda: self.click_button(2, icon, icon1, icon2))
        self.pushButton_3.clicked.connect(lambda: self.click_button(3, icon, icon1, icon2))
        self.pushButton_4.clicked.connect(lambda: self.click_button(4, icon, icon1, icon2))
        self.pushButton_5.clicked.connect(lambda: self.click_button(5, icon, icon1, icon2))
        self.pushButton_6.clicked.connect(lambda: self.click_button(6, icon, icon1, icon2))
        self.pushButton_7.clicked.connect(lambda: self.click_button(7, icon, icon1, icon2))
        self.pushButton_8.clicked.connect(lambda: self.click_button(8, icon, icon1, icon2))

        self.actionSingle_Player.triggered.connect(lambda: self.game_mode('single'))
        self.actionMulti_Player.triggered.connect(lambda:self.game_mode('multi'))
        self.actionExit.triggered.connect(lambda:self.exit_program())
        self.actionHow_to_Play.triggered.connect(lambda:self.how_to_play())
        self.actionAbout_Game.triggered.connect(lambda: self.About_Game())

    def exit_program(self):
        QCoreApplication.instance().quit()

    def game_mode(self, opt):
        if opt == 'multi':
            self.game_option = 1
        else:
            self.game_option = 0

    def retranslateUi(self, TicTacToe):
        _translate = QtCore.QCoreApplication.translate
        TicTacToe.setWindowTitle(_translate("TicTacToe", "Tic-Tac_toe"))
        TicTacToe.setWindowIcon(QtGui.QIcon("Resources/cross.png"))
        self.label.setText(_translate("TicTacToe", "Player X turn"))
        self.score.setText(_translate("TicTacToe", "0"))
        self.menuFile.setTitle(_translate("TicTacToe", "File"))
        self.menuAbout.setTitle(_translate("TicTacToe", "About"))
        self.actionSingle_Player.setText(_translate("TicTacToe", "Single Player"))
        self.actionSingle_Player.setStatusTip(_translate("TicTacToe", "Single Player"))
        self.actionMulti_Player.setText(_translate("TicTacToe", "Multi Player"))
        self.actionMulti_Player.setStatusTip(_translate("TicTacToe", "Multi Player"))
        self.actionHow_to_Play.setText(_translate("TicTacToe", "How to Play"))
        self.actionHow_to_Play.setStatusTip(_translate("TicTacToe", "How to Play"))
        self.actionAbout_Game.setText(_translate("TicTacToe", "About Game"))
        self.actionAbout_Game.setStatusTip(_translate("TicTacToe", "About Game"))
        self.actionExit.setText(_translate("TicTacToe", "Exit"))

    def flip_player(self, pos, icon, icon1, icon2):
        self.is_game_running = True
        if self.current_player == 'X' and self.is_game_running:
            self.list_of_x.append(pos)
            self.board[pos] = 'X'
            self.check_for_winner(icon)
            if self.is_game_running:
                self.current_player = "O"
            if self.game_option == 1 and self.current_player == 'O':
                comp_pos = self.computer_turn()
                self.board[comp_pos] = 'O'
                self.list_of_o.append(comp_pos)
                self.comp_click_button(comp_pos, icon1, icon2)
                self.check_for_winner(icon)
                self.current_player = "X"
        else:
            self.list_of_o.append(pos)
            self.board[pos] = 'O'
            self.check_for_winner(icon)
            self.current_player = "X"
        if self.game_option == 1:
            self.label.setText("Your are playing with computer")
        else:
            self.label.setText(f'Player {self.current_player} turns')
        self.score.setText(f'X: {self.scoreX} | O wins: {self.scoreY} | Draw: {self.scoreD}')
        self.label.adjustSize()
        self.score.adjustSize()

    def computer_turn(self):
        # computer occupied list
        empty_list = []

        for i in range(len(self.board)):
            if self.board[i] == '-':
                empty_list.append(i)

        # random number from the empty list for 1st move
        if len(empty_list) > 7:
            comp_input = 4
            if self.board[comp_input] == '-':
                return comp_input
            else:
                comp_input = random.choice([0, 2, 6, 8])
                return comp_input
        else:
            move = self.computer_move(empty_list)
            return move

    def computer_move(self, empty_list):
        count_list_x = len(self.list_of_x) - 1
        count_list_o = len(self.list_of_o) - 1

        if count_list_o > 0:
            # best for win
            for x in self.comp_input_defend:
                for y in self.list_of_o:
                    for z in self.list_of_o:
                        if (y == x[0] and z == x[1]) or (y == x[0] and z == x[1]):
                            if self.board[x[2]] == '-':
                                print('win')
                                return x[2]

        if count_list_x > 0:
            # best if x in center
            for x in self.comp_input_defend:
                for y in self.list_of_x:
                    for z in self.list_of_x:
                        if (y == x[0] and z == x[1]) or (y == x[0] and z == x[1]) :
                            if self.board[x[2]] == '-':
                                print('defend')
                                return x[2]

        if count_list_x > 0:
            # best if o in center
            for x in self.list_of_x:
                for y in self.list_of_x:
                    for z in self.x_corner:
                        if (x == z[0] and y == z[1]) or (x == z[1] and y == z[0]):
                            x_even = [1, 3, 5, 7]
                            random.shuffle(x_even)
                            for x_odd in x_even:
                                if self.board[x_odd] == '-':
                                    print('defend')
                                    return x_odd

        for i in self.list_of_o:
            for comp_no in self.comp_input_to_win[i]:
                if self.board[comp_no] == '-':
                    print('last')
                    return comp_no
        return random.choice(empty_list)

    def click_button(self, pos, icon, icon1, icon2):
        if pos not in self.list_of_x and pos not in self.list_of_o:
            if pos == 0:
                if self.current_player == 'X':
                    self.pushButton_0.setIcon(icon1)
                else:
                    self.pushButton_0.setIcon(icon2)
            elif pos == 1:
                if self.current_player == 'X':
                    self.pushButton_1.setIcon(icon1)
                else:
                    self.pushButton_1.setIcon(icon2)
            elif pos == 2:
                if self.current_player == 'X':
                    self.pushButton_2.setIcon(icon1)
                else:
                    self.pushButton_2.setIcon(icon2)
            elif pos == 3:
                if self.current_player == 'X':
                    self.pushButton_3.setIcon(icon1)
                else:
                    self.pushButton_3.setIcon(icon2)
            elif pos == 4:
                if self.current_player == 'X':
                    self.pushButton_4.setIcon(icon1)
                else:
                    self.pushButton_4.setIcon(icon2)
            elif pos == 5:
                if self.current_player == 'X':
                    self.pushButton_5.setIcon(icon1)
                else:
                    self.pushButton_5.setIcon(icon2)
            elif pos == 6:
                if self.current_player == 'X':
                    self.pushButton_6.setIcon(icon1)
                else:
                    self.pushButton_6.setIcon(icon2)
            elif pos == 7:
                if self.current_player == 'X':
                    self.pushButton_7.setIcon(icon1)
                else:
                    self.pushButton_7.setIcon(icon2)
            elif pos == 8:
                if self.current_player == 'X':
                    self.pushButton_8.setIcon(icon1)
                else:
                    self.pushButton_8.setIcon(icon2)
            self.flip_player(pos, icon, icon1, icon2)

    def comp_click_button(self, pos, icon1, icon2):
        if pos == 0:
            if self.current_player == 'X':
                self.pushButton_0.setIcon(icon1)
            else:
                self.pushButton_0.setIcon(icon2)
        elif pos == 1:
            if self.current_player == 'X':
                self.pushButton_1.setIcon(icon1)
            else:
                self.pushButton_1.setIcon(icon2)
        elif pos == 2:
            if self.current_player == 'X':
                self.pushButton_2.setIcon(icon1)
            else:
                self.pushButton_2.setIcon(icon2)
        elif pos == 3:
            if self.current_player == 'X':
                 self.pushButton_3.setIcon(icon1)
            else:
                self.pushButton_3.setIcon(icon2)
        elif pos == 4:
            if self.current_player == 'X':
                self.pushButton_4.setIcon(icon1)
            else:
                self.pushButton_4.setIcon(icon2)
        elif pos == 5:
            if self.current_player == 'X':
                self.pushButton_5.setIcon(icon1)
            else:
                self.pushButton_5.setIcon(icon2)
        elif pos == 6:
            if self.current_player == 'X':
                self.pushButton_6.setIcon(icon1)
            else:
                self.pushButton_6.setIcon(icon2)
        elif pos == 7:
            if self.current_player == 'X':
                self.pushButton_7.setIcon(icon1)
            else:
                self.pushButton_7.setIcon(icon2)
        elif pos == 8:
            if self.current_player == 'X':
                self.pushButton_8.setIcon(icon1)
            else:
                self.pushButton_8.setIcon(icon2)

    def check_for_winner(self, icon):
        # check row
        if self.check_rows():
            self.winner = self.current_player
        # check column
        elif self.check_column():
            self.winner = self.current_player
        # check diagonals
        elif self.check_diagonal():
            self.winner = self.current_player
        else:
            self.check_if_tie(icon)
        if self.winner is not None:
            self.show_popup(icon)

    def check_if_tie(self, icon):
        if self.board.count('X') + self.board.count('O') > 8:
            self.show_popup(icon)

    def check_rows(self):
        if self.board[0] == self.board[1] == self.board[2] != '-':
            return self.current_player
        elif self.board[3] == self.board[4] == self.board[5] != '-':
            return self.current_player
        elif self.board[6] == self.board[7] == self.board[8] != '-':
            return self.current_player
        return None

    def check_column(self):
        if self.board[0] == self.board[3] == self.board[6] != '-':
            return self.current_player
        elif self.board[1] == self.board[4] == self.board[7] != '-':
            return self.current_player
        elif self.board[2] == self.board[5] == self.board[8] != '-':
            return self.current_player
        return None

    def check_diagonal(self):
        if self.board[0] == self.board[4] == self.board[8] != '-':
            return self.current_player
        elif self.board[2] == self.board[4] == self.board[6] != '-':
            return self.current_player
        return None

    def how_to_play(self):
        msg = QMessageBox()
        msg.setWindowTitle('How to Play')
        msg.setWindowIcon(QtGui.QIcon("Resources/cross.png"))
        with open('Resources/hot_to.txt', 'r') as f:
            text = f.read()
            msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        x = msg.exec_()

    def About_Game(self):
        msg = QMessageBox()
        msg.setWindowTitle('About Game')
        msg.setWindowIcon(QtGui.QIcon("Resources/cross.png"))
        with open('Resources/about.txt', 'r') as f:
            text = f.read()
            msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        x = msg.exec_()

    def show_popup(self, icon):
        msg = QMessageBox()
        msg.setWindowTitle('winner')
        msg.setWindowIcon(QtGui.QIcon("Resources/cross.png"))
        if self.winner is not None:
            msg.setText(f'Player {self.winner} wins.')
            if self.winner == 'X':
                self.scoreX += 1
            else:
                self.scoreY += 1
        else:
            self.scoreD +=1
            msg.setText(f'Draw !')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        x = msg.exec_()
        self.list_of_o = []
        self.list_of_x = []
        self.board = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-']
        self.pushButton_0.setIcon(icon)
        self.pushButton_1.setIcon(icon)
        self.pushButton_2.setIcon(icon)
        self.pushButton_3.setIcon(icon)
        self.pushButton_4.setIcon(icon)
        self.pushButton_5.setIcon(icon)
        self.pushButton_6.setIcon(icon)
        self.pushButton_7.setIcon(icon)
        self.pushButton_8.setIcon(icon)
        self.winner = None
        self.current_player = 'X'
        self.is_game_running = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TicTacToe = QtWidgets.QMainWindow()
    ui = Ui_TicTacToe()
    ui.setupUi(TicTacToe)
    TicTacToe.show()
    sys.exit(app.exec_())