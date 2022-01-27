import os

class CreateSelectTextFile():

    def wrtite_txt_file(self, flagDictionary):

        # flagDictionary 파라미터에서 Value값 얻기

        # 1. flagDictionary 에서 excel의 Value값(선택 O: 1 선택 X: 0 )
        excel_value = flagDictionary['excel']

        # 2. flagDictionary 에서 DB의 Value값(선택 O: 1 선택 X: 0 )
        DB_value = flagDictionary['DB']

        # 엑셀 및 DB의 선택 txt 파일에 저장

        # 1. setting.txt 파일을 저장하는 디렉토리 만들기

        path = "C:/Users/cusoft/Desktop/test/setting"

        cstf = CreateSelectTextFile()
        cstf.makedirs(path)

        # 2. path에 지정된 디렉토리에 setting.txt파일 만들기

        f = open(path+"/select_setting.txt", "w")


        # flag값
        if excel_value == 1 : #엑셀에 체크가 되어 있는 경우

            excel_string = "True"

        else: #엑셀에 체크가 되어있지 않는 경우

            excel_string = "False"

        if DB_value == 1 : # DB에 체크가 되어 있는 경우

            db_string = "True"

        else: # DB에 체크가 되어있지 않는 경우

            db_string = "False"


        #리스트로 txt file에 한번에 넣기
        lines = ["Excel:"+ excel_string+"\n", "Database:"+db_string+"\n"]
        f.writelines(lines)



    def makedirs(self,path):
        try:
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise