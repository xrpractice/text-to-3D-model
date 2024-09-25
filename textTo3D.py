import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("MESHY_API_KEY")

headers = {
        "Authorization": api_key
}

def getModelID(prompt,style):

    payload = {
       "mode": "preview",
        "prompt": prompt,
        "art_style": style,
        "negative_prompt": "low quality"
    }

    response = requests.post(
        "https://api.meshy.ai/v2/text-to-3d",
        headers=headers,
        json=payload,
    )
    response.raise_for_status()

    task_id = response.json().get('result') 
    print(f"Task ID: {task_id}")
    return task_id

def downloadModelInObjFormat(model_task_id, folder_path):
    response_model = requests.get(
        f"https://api.meshy.ai/v2/text-to-3d/{model_task_id}", #019209f8-34fa-75a3-8fd8-f827cca0b4b5
        headers=headers,
    )

    response_model.raise_for_status()
    #print(response_model.json())

    result_url = response_model.json()['model_urls']['obj']

    print(result_url)
    result_response = requests.get(result_url)
    result_response.raise_for_status()

    output_file = os.path.join(folder_path, 'result.obj')  
    with open(output_file, 'wb') as file:
        file.write(result_response.content)

    return response_model.json() 
