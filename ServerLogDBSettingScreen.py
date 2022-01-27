from cgitb import text
from tkinter import *
from tkinter import messagebox
from DbdataDecryption import DbdataDecryption
from CreateDataBaseSettingFile import CreateDataBaseSettingFile
from SaveLogDBSettingScreen import SaveLogDBSettingScreen

class ServerLogDBSettingScreen():

    def draw_GUI_screen(self):

        self.window = Tk()
        self.window.title("Director Logging DB 설정 화면")  # 메인 화면 타이틀 제목 설정
        self.window.geometry("800x640")  # 메인 화면 크기 설정
        self.window.resizable(False, False)  # 가로값 x 세로값 변경 불가

        # 메인 화면 라벨 설정
        IPLabel = Label(self.window, text="데이터베이스 IP")  # 데이터 베이스 IP 라벨
        IPLabel.place(x=120, y=100)  # IPLabel의 위치

        IDLabel = Label(self.window, text="계정")  # 계정 라벨
        IDLabel.place(x=120, y=200)  # IDLabel 위치

        PWLabel = Label(self.window, text="패스워드")  # 비밀번호 라벨
        PWLabel.place(x=120, y=300)  # PWLabel 위치

        DBNameLabel = Label(self.window, text="DB명")  # DB명 라벨
        DBNameLabel.place(x=120, y=400)  # DBNameLabel 위치

        # 메인 화면 텍스트 박스 설정
        self.IPTextBox = Entry(self.window, width=50)  # 데이터 베이스 IP 텍스트 박스
        self.IPTextBox.place(x=300, y=100)  # 데이터 베이스 IP 텍스트 박스 위치

        self.IDTextBox = Entry(self.window, width=50)  # ID 텍스트 박스
        self.IDTextBox.place(x=300, y=200)  # ID 텍스트 박스 위치

        self.PWTextBox = Entry(self.window, width=50, show='*')  # 패스워드 텍스트 박스 위치
        self.PWTextBox.place(x=300, y=300)  # 패스워드 텍스트 박스 위치

        self.DBNameTextBox = Entry(self.window, width=50)  # 데이터베이스 위치
        self.DBNameTextBox.place(x=300, y=400)  # 데이터베이스 텍스트 박스 위치

        nextButton = Button(self.window, text="  확인  ", command = self.next_Click, height=3, width=20)  # Next 버튼
        nextButton.place(x=338, y=500)  # OK 버튼 위치

        self.window.mainloop()

    def next_Click(self):

        #각 텍스트 박스에서 value 값 가져오기
        IP = self.IPTextBox.get()  # IP값을 받아옴
        ID = self.IDTextBox.get()  # ID값을 받아옴
        PW = self.PWTextBox.get()  # PW값을 받아옴
        DBName = self.DBNameTextBox.get()  # DBName값을 받아옴


        #각 데이터 복호화 기능
        # db_decryption = DbdataDecryption();
        # PW = db_decryption.encrypt(PW)

        textList = []  # 입력값을 저장할 리스트 선언
        textList.append(IP)  # IP 값 입력
        textList.append(ID)  # ID 값 입력
        textList.append(PW)  # PW 값 입력
        textList.append(DBName)  # DBName 값 입력

        #로그 정보를 가지고 있는 데이터 베이스 세팅정보를 저장할 클래스 객체화
        creata_DB_setting = CreateDataBaseSettingFile()
        creata_DB_setting.wrtite_txt_file(textList)

        #GUI창 종료
        self.window.destroy()

        save_log_db_screen = SaveLogDBSettingScreen()
        save_log_db_screen.draw_GUI_screen()
