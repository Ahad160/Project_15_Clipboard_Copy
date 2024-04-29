def Google_Drive_API(files,Api):
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    # Set up the service account credentials
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = Api

    Credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=Credentials)

    # Extract the folder ID from the URL
    Folder_URL = 'https://drive.google.com/drive/folders/17LJ0X3cGcktqCUaqOIvLfvY-z8Q9erkJ'
    
    Folder_ID = Folder_URL.split('/')[-1]

    # Upload a File to Google Drive within the specified folder
    File_Metadata = {
        'name': "Log",  # Name for the uploaded File
        'parents': [Folder_ID],  # ID of the target folder
    }
    Upload=files
    Media = MediaFileUpload(Upload, mimetype='Text/txt')
    File = drive_service.files().create(body=File_Metadata, media_body=Media).execute()
    
    print(f'File ID: {File.get("id")}')
    # print("File Upload Completed")




