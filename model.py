
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
model = load_model('Main model.keras')  # Load your trained model here")

def predict_tumor(path):
    
     img = load_img(path,target_size=(224,224) )
     input_arr = img_to_array(img)/255

     print(input_arr.shape)
     input_arr = np.expand_dims(input_arr,axis =0)
     pred =( model.predict(input_arr) > 0.5).astype("int32")
     print(pred)
     if pred == 1:
        print("Suffering from Tumor")
     else:
        print("Person is Healthy")
     return pred[0][0]
    
if __name__ =="__main__":
    predict_tumor(
        "E:/tumor project/Preoperative-MRI-revealed-a-solid-tumor-in-the-right-frontal-lobe-T1-Gd-a-Enhanced.png"
    )
