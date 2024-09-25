from flask import Flask, render_template, request, send_file
import textTo3D
import os

app = Flask(__name__)


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  

@app.route('/', methods=['GET', 'POST'])
def index():
    modelID = None
    modelJSON = None

    if request.method == 'POST':
        if 'promptForm' in request.form:
            prompt = request.form.get('prompt')
            style = request.form.get('style')
            modelID = textTo3D.getModelID(prompt,style)

        elif 'ModelForm' in request.form:
            modelId = request.form.get('modelId')
            modelJSON = textTo3D.downloadModelInObjFormat(modelId, UPLOAD_FOLDER) 
            file_path = os.path.join(UPLOAD_FOLDER, 'result.obj')

            return send_file(file_path, as_attachment=True, download_name='model.obj')

    return render_template('index.html', modelID=modelID, modelJSON=modelJSON)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
