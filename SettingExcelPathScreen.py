from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from CreateExcelSettingFile import CreateExcelSettingFile




class SettingExcelPathScreen:

    def draw_GUI_screen(self):

        self.window = Tk()
        self.window.title("Excel 경로 설정 화면 ")  # 메인 화면 타이틀 제목 설정
        self.window.geometry("800x640")  # 메인 화면 크기 설정
        self.window.resizable(False, False)  # 가로값 x 세로값 변경 불가

        nextButton = Button(self.window, text="  확인  ", command=self.next_Click, height=3, width=20)  # Next 버튼
        nextButton.place(x=338, y=500)  # OK 버튼 위치

    def next_Click(self):

        messagebox.showinfo("알림창", "엑셀 패스 선택 버튼 입니다.")
        self.window.dirName = filedialog.askdirectory()
        # root.file = filedialog.askopenfile(initialdir='path', title='select file', filetypes=(('jpeg files', '*.jgp'), ('all files', '*.*')))
        string_excel_path = self.window.dirName
        create_excel_setting_file = CreateExcelSettingFile()
        create_excel_setting_file.craete_excel_setting_file(string_excel_path)
