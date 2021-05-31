# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LED_FND.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# UI class
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(288, 313)
        self.label_LED0 = QtWidgets.QLabel(window)
        self.label_LED0.setGeometry(QtCore.QRect(51, 131, 43, 73))
        self.label_LED0.setText("")
        self.label_LED0.setPixmap(QtGui.QPixmap("./image_file/LED_ON.png"))
        self.label_LED0.setObjectName("label_LED0")
        self.label_LED0.setEnabled(False)
        self.label_LED1 = QtWidgets.QLabel(window)
        self.label_LED1.setGeometry(QtCore.QRect(190, 131, 43, 73))
        self.label_LED1.setText("")
        self.label_LED1.setPixmap(QtGui.QPixmap("./image_file/LED_ON.png"))
        self.label_LED1.setObjectName("label_LED1")
        self.label_LED1.setEnabled(False)
        self.led0_btn = QtWidgets.QPushButton(window)
        self.led0_btn.setGeometry(QtCore.QRect(31, 210, 85, 30))
        self.led0_btn.setObjectName("led0_btn")
        self.led1_btn = QtWidgets.QPushButton(window)
        self.led1_btn.setGeometry(QtCore.QRect(170, 210, 85, 30))
        self.led1_btn.setObjectName("led1_btn")
        self.pushButton = QtWidgets.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(80, 260, 99, 30))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(window)
        self.widget.setGeometry(QtCore.QRect(31, 11, 229, 109))
        self.widget.setObjectName("widget")
        self.verticalLayout_FND = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_FND.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_FND.setObjectName("verticalLayout_FND")
        self.label_FND = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Sans serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_FND.setFont(font)
        self.label_FND.setText("")
        self.label_FND.setPixmap(QtGui.QPixmap("./image_file/FND.png"))
        self.label_FND.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FND.setObjectName("label_FND")
        self.verticalLayout_FND.addWidget(self.label_FND)
        self.label_help = QtWidgets.QLabel(self.widget)
        self.label_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_help.setObjectName("label_help")
        self.verticalLayout_FND.addWidget(self.label_help)
        self.lineEdit_FND = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_FND.setObjectName("lineEdit_FND")
        self.verticalLayout_FND.addWidget(self.lineEdit_FND)

        self.retranslateUi(window)
        # signal -> slot
        self.pushButton.clicked.connect(window.close)
        self.led0_btn.clicked.connect(LED0_Cntl)
        self.led1_btn.clicked.connect(LED1_Cntl)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "FND CNTL"))
        self.led0_btn.setText(_translate("window", "LED0"))
        self.led1_btn.setText(_translate("window", "LED1"))
        self.pushButton.setText(_translate("window", "종  료"))
        self.label_help.setText(_translate("window", "Input Datar(0~999999)"))

if __name__=="__main__":
    # add
    import sys
    import RPi.GPIO as GPIO     # GPIO 모듈 입포트
    import time                 # 시간 관련 모듈
    import threading
    
    # =========================== 하드웨어 설정 =================================
    GPIO.setmode(GPIO.BOARD)

    # 1. LED 설정 
    led0_state = False
    led1_state = False
    LED0, LED1 = 11, 13
    GPIO.setup((LED0, LED1), GPIO.OUT)

    # 2. FND 설정
    data = '123456'
    FND_DATA = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x27,
                0x7F,0x67,0x77,0x7C,0x39,0x5E,0x79,0x71]
    FND_DATA_PIN = [37,35,33,31,29,23,21,19]   # A~DP
    FND_DIGIT_PIN = [32, 24, 22, 18, 16, 12]        # D5 ~ D0
    GPIO.setup(FND_DATA_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(FND_DIGIT_PIN, GPIO.OUT, initial=GPIO.HIGH)
    
    # 사용자함수
    def button_test():
        print('Button Test')
        
    def LED0_Cntl():
        global led0_state
        if led0_state==False:
            ui.label_LED0.setEnabled(True)
            led0_state = True
        else:
            ui.label_LED0.setEnabled(False)
            led0_state = False

    def LED1_Cntl():
        global led1_state
        if led1_state==False:
            ui.label_LED1.setEnabled(True)
            led1_state = True
        else:
            ui.label_LED1.setEnabled(False)
            led1_state = False
            
    def FND_disp(a):
        global data
        print("숫자가 입력됐습니다.")
        data = entry_FND.get()
        print(type(data), data)

    def FND_Display(num6):
        #num6_list = list(str(num6))
        num6_list = list("%06d" % num6)
        # print(num6_list)

        for i in range(6):
            GPIO.output(FND_DIGIT_PIN[i], GPIO.LOW)  # digit 이동
            for j in range(8):
                GPIO.output(FND_DATA_PIN[j], FND_DATA[int(num6_list[i])] & (0x01<<j))
            time.sleep(0.001)
            GPIO.output(FND_DIGIT_PIN[i], GPIO.HIGH)

    # 쓰레드 함수
    def Thread_FND6():
        global data
        while True:
            FND_Display(int(data))
            
            if thread_stop==True:
                break
            
    def Thread_LED0():
        while True:
            if led0_state==True:
                GPIO.output(LED0, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(LED0, GPIO.LOW)
                time.sleep(0.3)
            else:
                GPIO.output(LED0, GPIO.LOW)
                
            if thread_stop==True:
                break

    def Thread_LED1():
        while True:
            if led1_state==True:
                GPIO.output(LED1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LED1, GPIO.LOW)
                time.sleep(0.5)
            else:
                GPIO.output(LED1, GPIO.LOW)
            
            if thread_stop==True:
                break
    try:
        thread_stop = False
        t1 = threading.Thread(target=Thread_FND6)
        t2 = threading.Thread(target=Thread_LED0)
        t3 = threading.Thread(target=Thread_LED1)
        
        t1.start()
        t2.start()
        t3.start()

        #=========================== 윈도우 창 설정 =================================
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_window()      # 객체 생성
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())    
    
    except KeyboardInterrupt:
        print("키보드 예외")
        
    finally:
        thread_stop = True
        t1.join()   # 쓰레드가 종료 될때까지 대기
        print("Cleanup")
        GPIO.cleanup()

    
    