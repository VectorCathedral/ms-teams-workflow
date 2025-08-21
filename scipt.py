import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_notes_teams(excel_sheet:str,slides:str):
    url=os.getenv('webhook_url')
    headers={
        'Content-Type': 'application/json'
    }

    with open(excel_sheet,'r') as file:
        for student in file:
            fullname,FirstJoin,LastLeave,Duration,studNum,Participant,Role=student.split(';')
            if fullname != 'Name':
                try:
                    payload ={
                        "studNum":f"{studNum}",
                        "message":f"Hey {fullname}👋Here's todays notes🎒📖This link expires in 30 days so please download ASAP🤙",
                        "url":f"{slides}"
                    }

                    response=requests.post(url=url,headers=headers,json=payload)

                except Exception as e:
                    print(f'Caught:{e}')
         
        
        
    return response.status_code

            
path='./attendence.csv'
notes_url='sharepoint url goes here'

send_notes_teams(excel_sheet=path,slides=notes_url)