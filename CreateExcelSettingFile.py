
import os

class CreateExcelSettingFile:

    def craete_excel_setting_file(self,excel_path):

        excel_path_value = excel_path
        path = "C:/Users/cusoft/Desktop/test/setting"
        f = open(path + "/excel_setting.txt", "w")
        lines = ["Excel:" + excel_path_value + "\n"]
        f.writelines(lines)