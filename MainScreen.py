from cgitb import text
from tkinter import *
from tkinter import messagebox
from CreatSelectTextFile import CreateSelectTextFile
from ServerLogDBSettingScreen import ServerLogDBSettingScreen

class MainScreen :

    # 생성자 호출
    def __init__(self):

        self.window = Tk()
        self.window.title("AutoLoggingSetting")  # 메인 화면 타이틀 제목 설정
        self.window.geometry("600x440")  # 메인 화면 크기 설정
        self.window.resizable(False, False)  # 가로값 x 세로값 변경 불가


        #체크 박스 만들기
        self.chkvar = IntVar()  # chkvar 에 int 형으로 값을 저장
        chkbox = Checkbutton(self.window, text = "Excel로 저장하기"  ,variable = self.chkvar)  # root라는 창에 체크 박스 생성
        chkbox.place(x = 250, y=130)

        self.chkvar1 = IntVar()  # chkvar1에 int 형으로 값을 저장
        chkbox1 = Checkbutton(self.window, text = "DB에 저장하기" ,variable = self.chkvar1)  # root라는 창에 체크박스 생성
        chkbox1.place(x= 250, y=180)  # 체크박스 배치

        OkButton = Button(self.window, text="다음", command=self.setting_Click, height=3, width=20)  # 다음 버튼
        OkButton.place(x= 238, y=300)  # 다음 버튼 위치

        self.window.mainloop()

    def setting_Click(self):

        #엑셀 체크 flag 값 불러오기
        excel_Flag = self.chkvar.get()
        print(excel_Flag)

        #DB 체크 flag 값 불러오기
        DB_Flag = self.chkvar1.get()
        print(DB_Flag)


        #파라미터로 넘겨줄 딕셔너리 생성
        flag_dic = {'excel':excel_Flag, 'DB':DB_Flag}

        # CreateSelectTextFile 클래스 객체 생성
        cst = CreateSelectTextFile
        cst.wrtite_txt_file(self, flag_dic)

        # 기존 GUI창 종료
        self.window.destroy()

        # directX DB 접속 정보를 등록 할 수 있는 GUI 화면 연결
        out_db_setting = ServerLogDBSettingScreen()
        out_db_setting.draw_GUI_screen()
        




#메인 화면 호출
ms = MainScreen()
