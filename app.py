from flask import Flask, render_template, request
import os
import model 
app = Flask(__name__)


@app.route("/")
def helloworld():
    return render_template("index2.html")


@app.route("/predict", methods=["POST"])
def predict():
     if 'file' not in request.files:
        return render_template("index.html")+'No file part'

     file = request.files['file']
     if file.filename == '':
        return 'No selected file'

    # Save the uploaded file
     file_path = os.path.join(os.getcwd(),"uploads", file.filename)
     file.save(file_path)
     
    # Now call your prediction function passing the file_path
     prediction = model.predict_tumor(file_path)
     if  (prediction==1):
         return render_template("pred.html")
     elif (prediction ==0):
         return  render_template("healthy.html")
         
     else :
         return "ERROR 404"


if __name__ == "main":
    app.run(debug=True)
