class numerickeyboard(QWidget): 
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,16,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setFocusPolicy(QtCore.Qt.NoFocus)
        #lineedit = QtGui.QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,133,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,133,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,133,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,237,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,237,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,237,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,341,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,341,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,341,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,445,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,445,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kpo = QPushButton('.', self)
        kpo.setGeometry(670,445,297,100)
        kpo.setFont(QFont('Arial', 28))
        kpo.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kpo.clicked.connect(self.insert_text)
        
        kabc = QPushButton('abc', self)
        kabc.setGeometry(45,549,296,100)
        kabc.setFont(QFont('Arial', 24))
        kabc.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kabc.clicked.connect(self.change_abc)
        
        kspace = QPushButton('space', self)
        kspace.setGeometry(358,549,296,100)
        kspace.setFont(QFont('Arial', 24))
        kspace.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kspace.clicked.connect(self.space1)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(670,549,297,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
    def clear1(self):
        #self.entry.text=self.entry.text()[0:-2]
        print(self.entry.text()[0:-1])
        l=self.entry.text()[0:-1]
        self.entry.setText(l)
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    
    def enter1(self):
        if(self.previouswindow=='e_user' ):
            keydata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_employer'):
            keydata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_contact'):
            keydata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_designation'):
            keydata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='a_user' ):
            adduserdata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_employer'):
            adduserdata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_contact'):
            adduserdata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_designation'):
            adduserdata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()

    def change_abc(self):
        self.close()
        self.destroy()
        gc.collect()        

        self.capital_keyboard1=keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.capital_keyboard1.show()
    
class keyboard(QWidget):
    def __init__(self,mainwindowshow,previouswindow,entry_1):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entry_1=entry_1
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,16,200,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setMaxLength(self.length)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setText(self.entry_1)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton('q', self)
        q.setGeometry(59,149,82,100)
        q.setFont(QFont('Arial', 24))
        q.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton('w', self)
        self.w.setGeometry(149,149,82,100)
        self.w.setFont(QFont('Arial', 24))
        self.w.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton('e', self)
        self.e.setGeometry(240,149,82,100)
        self.e.setFont(QFont('Arial', 24))
        self.e.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton('r', self)
        self.r.setGeometry(331,149,82,100)
        self.r.setFont(QFont('Arial', 24))
        self.r.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('t', self)
        self.t.setGeometry(422,149,82,100)
        self.t.setFont(QFont('Arial', 24))
        self.t.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('y', self)
        self.y.setGeometry(513,149,82,100)
        self.y.setFont(QFont('Arial', 24))
        self.y.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('u', self)
        self.u.setGeometry(604,149,82,100)
        self.u.setFont(QFont('Arial', 24))
        self.u.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('i', self)
        self.i.setGeometry(695,149,82,100)
        self.i.setFont(QFont('Arial', 24))
        self.i.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton('o', self)
        self.o.setGeometry(786,149,82,100)
        self.o.setFont(QFont('Arial', 24))
        self.o.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton('p', self)
        self.p.setGeometry(877,149,82,100)
        self.p.setFont(QFont('Arial', 24))
        self.p.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.p.clicked.connect(self.insert_text)
        
        self.a = QPushButton('a', self)
        self.a.setGeometry(59,280,82,100)
        self.a.setFont(QFont('Arial', 24))
        self.a.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton('s', self)
        self.s.setGeometry(149,280,82,100)
        self.s.setFont(QFont('Arial', 24))
        self.s.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton('d', self)
        self.d.setGeometry(240,280,82,100)
        self.d.setFont(QFont('Arial', 24))
        self.d.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton('f', self)
        self.f.setGeometry(331,280,82,100)
        self.f.setFont(QFont('Arial', 24))
        self.f.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton('g', self)
        self.g.setGeometry(422,280,82,100)
        self.g.setFont(QFont('Arial', 24))
        self.g.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('h', self)
        self.h.setGeometry(513,280,82,100)
        self.h.setFont(QFont('Arial', 24))
        self.h.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton('j', self)
        self.j.setGeometry(604,280,82,100)
        self.j.setFont(QFont('Arial', 24))
        self.j.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('k', self)
        self.k.setGeometry(695,280,82,100)
        self.k.setFont(QFont('Arial', 24))
        self.k.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton('l', self)
        self.l.setGeometry(786,280,82,100)
        self.l.setFont(QFont('Arial', 24))
        self.l.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(':', self)
        self.col.setGeometry(877,280,82,100)
        self.col.setFont(QFont('Arial', 24))
        self.col.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.col.clicked.connect(self.insert_text)
        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,414,83,100)
        self.shift.setFont(QFont('Arial', 40))
        self.shift.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.shift.clicked.connect(self.shift1)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('z', self)
        self.z.setGeometry(149,413,82,100)
        self.z.setFont(QFont('Arial', 24))
        self.z.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('x', self)
        self.x.setGeometry(240,413,82,100)
        self.x.setFont(QFont('Arial', 24))
        self.x.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('c', self)
        self.c.setGeometry(331,413,82,100)
        self.c.setFont(QFont('Arial', 24))
        self.c.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('v', self)
        self.v.setGeometry(422,413,82,100)
        self.v.setFont(QFont('Arial', 24))
        self.v.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('b', self)
        self.b.setGeometry(513,413,82,100)
        self.b.setFont(QFont('Arial', 24))
        self.b.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('n', self)
        self.n.setGeometry(604,413,82,100)
        self.n.setFont(QFont('Arial', 24))
        self.n.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('m', self)
        self.m.setGeometry(695,413,82,100)
        self.m.setFont(QFont('Arial', 24))
        self.m.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(786,413,82,100)
        self.po.setFont(QFont('Arial', 24))
        self.po.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(clr, self)
        self.clear.setGeometry(877,413,82,100)
        self.clear.setFont(QFont('Arial', 24))
        self.clear.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.clear.clicked.connect(self.clear1)
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,538,180,100)
        self.change.setFont(QFont('Arial', 24))
        self.change.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.change.clicked.connect(self.change_numeric)
        
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(253,538,125,100)
        self.dash.setFont(QFont('Arial', 24))
        self.dash.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.dash.clicked.connect(self.insert_text)
        
        self.space = QPushButton('space', self)
        self.space.setGeometry(388,538,338,100)
        self.space.setFont(QFont('Arial', 24))
        self.space.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.space.clicked.connect(self.space1)
        
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(738,538,230,100)
        self.enter.setFont(QFont('Arial', 24))
        self.enter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.enter.clicked.connect(self.enter1)

    def insert_text(self,data):
            sender = self.sender()
##            print(sender.text())
##            cursor = self.entry.cursorPosition()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
##            print('cursor',cursor)
##            self.entry.cursorWordForward(True)
##            self.entry.setCursorPosition(2)
            #self.entry.setText(str(data))
            
    def clear1(self):
        #self.entry.text=self.entry.text()[0:-2]
        print(self.entry.text()[0:-1])
        l=self.entry.text()[0:-1]
        self.entry.setText(l)
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    def enter1(self):
        if(self.previouswindow=='e_user' ):
            keydata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_employer'):
            keydata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_contact'):
            keydata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_designation'):
            keydata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='a_user' ):
            adduserdata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_employer'):
            adduserdata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_contact'):
            adduserdata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_designation'):
            adduserdata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()

    def shift1(self):
        self.close()
        self.destroy()
        gc.collect()

        self.capital_keyboard1=capital_keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.capital_keyboard1.show()
    def change_numeric(self):
        self.close()
        self.destroy()
        gc.collect()
        self.numerickeyboard1=numerickeyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.numerickeyboard1.show()
        
        
            
class capital_keyboard(QWidget):
    def __init__(self,mainwindowshow,previouswindow,entry_small):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entrys=entry_small
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;')
        self.label.setGeometry(20,16,220,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black')
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setMaxLength(self.length)
        self.entry.setText(self.entrys)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton('Q', self)
        q.setGeometry(59,149,82,100)
        q.setFont(QFont('Arial', 24))
        q.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton('W', self)
        self.w.setGeometry(149,149,82,100)
        self.w.setFont(QFont('Arial', 24))
        self.w.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton('E', self)
        self.e.setGeometry(240,149,82,100)
        self.e.setFont(QFont('Arial', 24))
        self.e.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton('R', self)
        self.r.setGeometry(331,149,82,100)
        self.r.setFont(QFont('Arial', 24))
        self.r.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('T', self)
        self.t.setGeometry(422,149,82,100)
        self.t.setFont(QFont('Arial', 24))
        self.t.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('Y', self)
        self.y.setGeometry(513,149,82,100)
        self.y.setFont(QFont('Arial', 24))
        self.y.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('U', self)
        self.u.setGeometry(604,149,82,100)
        self.u.setFont(QFont('Arial', 24))
        self.u.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('I', self)
        self.i.setGeometry(695,149,82,100)
        self.i.setFont(QFont('Arial', 24))
        self.i.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton('O', self)
        self.o.setGeometry(786,149,82,100)
        self.o.setFont(QFont('Arial', 24))
        self.o.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton('P', self)
        self.p.setGeometry(877,149,82,100)
        self.p.setFont(QFont('Arial', 24))
        self.p.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.p.clicked.connect(self.insert_text)
        
        self.a = QPushButton('A', self)
        self.a.setGeometry(59,280,82,100)
        self.a.setFont(QFont('Arial', 24))
        self.a.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton('S', self)
        self.s.setGeometry(149,280,82,100)
        self.s.setFont(QFont('Arial', 24))
        self.s.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton('D', self)
        self.d.setGeometry(240,280,82,100)
        self.d.setFont(QFont('Arial', 24))
        self.d.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton('F', self)
        self.f.setGeometry(331,280,82,100)
        self.f.setFont(QFont('Arial', 24))
        self.f.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton('G', self)
        self.g.setGeometry(422,280,82,100)
        self.g.setFont(QFont('Arial', 24))
        self.g.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('H', self)
        self.h.setGeometry(513,280,82,100)
        self.h.setFont(QFont('Arial', 24))
        self.h.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton('J', self)
        self.j.setGeometry(604,280,82,100)
        self.j.setFont(QFont('Arial', 24))
        self.j.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('K', self)
        self.k.setGeometry(695,280,82,100)
        self.k.setFont(QFont('Arial', 24))
        self.k.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton('L', self)
        self.l.setGeometry(786,280,82,100)
        self.l.setFont(QFont('Arial', 24))
        self.l.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(':', self)
        self.col.setGeometry(877,280,82,100)
        self.col.setFont(QFont('Arial', 24))
        self.col.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.col.clicked.connect(self.insert_text)
        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,414,83,100)
        self.shift.setFont(QFont('Arial', 40))
        self.shift.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.shift.clicked.connect(self.shift1)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('Z', self)
        self.z.setGeometry(149,413,82,100)
        self.z.setFont(QFont('Arial', 24))
        self.z.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('X', self)
        self.x.setGeometry(240,413,82,100)
        self.x.setFont(QFont('Arial', 24))
        self.x.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('C', self)
        self.c.setGeometry(331,413,82,100)
        self.c.setFont(QFont('Arial', 24))
        self.c.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('V', self)
        self.v.setGeometry(422,413,82,100)
        self.v.setFont(QFont('Arial', 24))
        self.v.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('B', self)
        self.b.setGeometry(513,413,82,100)
        self.b.setFont(QFont('Arial', 24))
        self.b.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('N', self)
        self.n.setGeometry(604,413,82,100)
        self.n.setFont(QFont('Arial', 24))
        self.n.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('M', self)
        self.m.setGeometry(695,413,82,100)
        self.m.setFont(QFont('Arial', 24))
        self.m.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(786,413,82,100)
        self.po.setFont(QFont('Arial', 24))
        self.po.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(clr, self)
        self.clear.setGeometry(877,413,82,100)
        self.clear.setFont(QFont('Arial', 24))
        self.clear.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.clear.clicked.connect(self.clear1)
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,538,180,100)
        self.change.setFont(QFont('Arial', 24))
        self.change.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.change.clicked.connect(self.change_numeric)
        
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(253,538,125,100)
        self.dash.setFont(QFont('Arial', 24))
        self.dash.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.dash.clicked.connect(self.insert_text)
        
        self.space = QPushButton('space', self)
        self.space.setGeometry(388,538,338,100)
        self.space.setFont(QFont('Arial', 24))
        self.space.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.space.clicked.connect(self.space1)
        
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(738,538,230,100)
        self.enter.setFont(QFont('Arial', 24))
        self.enter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.enter.clicked.connect(self.enter1)
    
    def insert_text(self,data):
            sender = self.sender()
##            print(sender.text())
##            cursor = self.entry.cursorPosition()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
##            print('cursor',cursor)
##            self.entry.cursorWordForward(True)
##            self.entry.setCursorPosition(2)
            #self.entry.setText(str(data))
            
    def clear1(self):
        #self.entry.text=self.entry.text()[0:-2]
        print(self.entry.text()[0:-1])
        l=self.entry.text()[0:-1]
        self.entry.setText(l)
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    def enter1(self):
        if(self.previouswindow=='e_user' ):
            keydata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_employer'):
            keydata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_contact'):
            keydata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_designation'):
            keydata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='a_user' ):
            adduserdata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_employer'):
            adduserdata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_contact'):
            adduserdata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_designation'):
            adduserdata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
    def shift1(self):
        self.close()
        self.destroy()
        gc.collect()

        self.keyboard1=keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.keyboard1.show()
    def change_numeric(self):
        self.close()
        self.destroy()
        gc.collect()
        self.numerickeyboard1=numerickeyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.numerickeyboard1.show()
