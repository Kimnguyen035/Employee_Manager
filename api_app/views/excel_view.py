from .views import *

class ExcelView(ViewSet):
    def excel_convert_json(self, request):
        link_file = "TemplateImportWorkDay_T04.2023.xlsx"
        df = pd.read_excel(link_file)
        data_dict_ = df.to_dict(orient="records")
        return response_data(data_dict_)