import os
from DbdataDecryption import DbdataDecryption

class SaveDataBaseSettingFile():

    def wrtite_txt_file(self, insertValueList):

        # insertValueList 파라미터 List값 저장
        db_value_list =[]
        db_value_list = insertValueList

        # 1. db_value_list 에서 value 값 변수 저장
        ip_value = db_value_list[0]
        id_value = db_value_list[1]
        pw_value = db_value_list[2] # < ----- 암호화 과정 필요
        db_name_value = db_value_list[3]

        # 엑셀 및 DB의 선택 txt 파일에 저장

        # 1. setting.txt 파일을 저장하는 디렉토리 만들기

        path = "C:/Users/cusoft/Desktop/test/setting" # <------ 이 부분 나중에 상대 경로로 바꿀 예정, 폴더를 따로 만들어서 관리할지도 고민 해보자...

        cstf = SaveDataBaseSettingFile()
        cstf.makedirs(path)

        # 2. path에 지정된 디렉토리에 setting.txt파일 만들기

        f = open(path+"/save_db_setting.txt", "w")


        # DB 설정 암호화 (현재는 PW만)
        dbdata_encryption = DbdataDecryption()
        ip_value_encr = dbdata_encryption.encrypt(ip_value)
        id_value_encr = dbdata_encryption.encrypt(id_value)
        pw_string_value = dbdata_encryption.encrypt(pw_value)
        db_name_value_encr = dbdata_encryption.encrypt(db_name_value)

        #리스트로 txt file에 한번에 넣기
        lines = ["IP:"+ ip_value_encr+"\n", "Database:"+id_value_encr+"\n", "Password:"+pw_string_value+"\n", "DB_Name:"+db_name_value_encr+"\n"]
        f.writelines(lines)



    def makedirs(self,path):
        try:
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise