from googleapiclient.discovery import build
API_KEY = 'AIzaSyDeTZtBjfbMiRpHPUowdw7vfvXAk-kmrAc'
API = 'Api you want to load'
VERSION = 'dont know what tgis is'
SERVICE = build(API, VERSION, developerKey=API_KEY)
