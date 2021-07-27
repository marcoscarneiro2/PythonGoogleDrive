from Google import Create_Service

CLIENT_SECRET_FILE = 'Api_key.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

tipoArquivo = ['documentos','fotos']

"""
for tipoArquivo in tipoArquivo:
    file_metadata = {
        'name': tipoArquivo,
        'mimeType': 'application/vnd.google-apps.folder',
        #'parents':[]
    }
    service.files().create(body=file_metadata).execute()
"""