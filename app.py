import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
import keras 
from keras.preprocessing.image import load_img,img_to_array 
import numpy as np
import tensorflow as tf
import streamlit as st
import time
from PIL import Image,ImageOps
import json



def processing(image,model):
  image=np.asarray(image)
  image_dims=np.expand_dims(image,axis=0)
  res=model.predict(image_dims)
  result=np.argmax(res)
  return result

st.title('Agri-EI 🍀')
st.text('         ')
st.text('         ')



selected=option_menu(menu_title='Main Page',
options=['About👨‍🏫','Practical👨‍💻','Hire me👨‍🎓'],
icons=['house','book','envelope'],orientation='horizontal',
)
st.text('   ')
st.text('   ')
st.text('   ')
st.text('   ')
if(selected=='About👨‍🏫'):
  st.header('About')
  st.image('images.jpg')
  st.markdown(""" **Plant diseases enormously affect the agricultural
  crop production and quality with huge economic losses to the
  farmers and the country. This in turn increases the market price
  of crops and food, which increase the purchase burden of
  customers. Therefore, early identification and diagnosis of plant
  diseases at every stage of plant life cycle is a very critical
  approach to protect and increase the crop yield.**""")

  st.markdown('**-----------------------------------------------------------------------------------------------**')
  st.header('Model')
  st.image('cnn1.png')
  st.markdown("""**The CNN-based network can be
  trained to discover diseases in plants by providing a large
  number of real-time images. In the case of lacking enough and
  good quality data or number of images, other techniques such
  as GANs can be used to generate the needed data for analysis
  and comparison with real-time data collected from the field.
  Both healthy and diseased plants and a future training model
  can be used to predict diseases in plants using plant leaf
  images**""")


  st.markdown('**#------------------------------------------------------------------------------------------------**')  


  st.header('Dataset:-')
  st.image('cnn2.png')
  st.markdown("""**The PlantVillage dataset is created to bring efficient solutions in order to detect 39 
  different plant diseases. It contains 61,486 images of plant leaves and backgrounds.
 It was created with six different augmentation techniques for creating more diverse datasets 
 with different background conditions. The augmentations used in this process were scaling
, rotation, noise injection, gamma correction, image flipping, and PCA color augmentation.**""")


#-----------------------------------------------------------------------------------------------------



elif(selected=='Practical👨‍💻'):
  st.header('Model Prediction')
  st.subheader('Please choose the plant to predict the disease')
  plant=st.radio('Please choose the plant to predict the disease:-',options=['Apple','Grape','Corn','Tomato','Potato'])
  st.text('    ')
  st.text('    ')
  st.text('    ')
  if(plant=='Potato'):
    classes=['Early Blight','Late Blight','Healthy']
    with st.spinner('Uploading the model for prediction'):
      model=tf.keras.models.load_model('Potato.h5')
    if model is not None:
      time.sleep(5)
      st.subheader('Please upload the picture of potato leaf:-')
      image_path=st.file_uploader('Upload the image here',type=['jpeg','png','jpg'])
    if image_path is not None:
      img=Image.open(image_path)
      img=ImageOps.fit(img,(150,150),Image.ANTIALIAS)
      result=processing(img,model)
      result=classes[result]
      with st.spinner('Analysing the picture'):
        time.sleep(5)
        st.image(image_path,caption=result)
        st.markdown('**The name of the type is:-**')
        st.balloons()
        st.subheader(result)

  elif(plant=='Tomato'):
    classes=['Bacterial Spot','Early blight','Late Blight','Leaf Mold','Septoria Leaf Spot','Spider Mites','Target Spot','Yellow leaf curl','Mosaic','Healthy']
    with st.spinner('Uploading the model for prediction'):
      model=tf.keras.models.load_model('Tomato.h5')
    if model is not None:
      time.sleep(5)
      st.subheader('Please upload the picture of Tomato leaf:-')
      image_path=st.file_uploader('Upload the image here',type=['jpeg','png','jpg'])
    if image_path is not None:
      img=Image.open(image_path)
      img=ImageOps.fit(img,(150,150),Image.ANTIALIAS)
      result=processing(img,model)
      result=classes[result]
      with st.spinner('Analysing the picture'):
        time.sleep(5)
        st.image(image_path,caption=result)
        st.markdown('**The name of the type is:-**')
        st.balloons()
        st.subheader(result)  


  elif(plant=='Grape'):
    classes=['Black Rot','Black Meales','Leaf Blight','Healthy']
    with st.spinner('Uploading the model for prediction'):
      model=tf.keras.models.load_model('Grape.h5')
    if model is not None:
      time.sleep(5)
      st.subheader('Please upload the picture of Grape leaf:-')
      image_path=st.file_uploader('Upload the image here',type=['jpeg','png','jpg'])
    if image_path is not None:
      img=Image.open(image_path)
      img=ImageOps.fit(img,(150,150),Image.ANTIALIAS)
      result=processing(img,model)
      result=classes[result]
      with st.spinner('Analysing the picture'):
        time.sleep(5)
        st.image(image_path,caption=result)
        st.markdown('**The name of the type is:-**')
        st.balloons()
        st.subheader(result)     

  
  elif(plant=='Apple'):
    classes=['Apple Scab','Black Rot','Cedar apple rust','Healthy']
    with st.spinner('Uploading the model for prediction'):
      model=tf.keras.models.load_model('Apple.h5')
    if model is not None:
      time.sleep(5)
      st.subheader('Please upload the picture of Apple leaf:-')
      image_path=st.file_uploader('Upload the image here',type=['jpeg','png','jpg'])
    if image_path is not None:
      img=Image.open(image_path)
      img=ImageOps.fit(img,(150,150),Image.ANTIALIAS)
      result=processing(img,model)
      result=classes[result]
      with st.spinner('Analysing the picture'):
        time.sleep(5)
        st.image(image_path,caption=result)
        st.markdown('**The name of the type is:-**')
        st.balloons()
        st.subheader(result)     

  elif(plant=='Corn'):
    classes=['Cercospara','Commorn Rust','Leaf Blight','Healthy']
    with st.spinner('Uploading the model for prediction'):
      model=tf.keras.models.load_model('Corn.h5')
    if model is not None:
      time.sleep(5)
      st.subheader('Please upload the picture of Corn leaf:-')
      image_path=st.file_uploader('Upload the image here',type=['jpeg','png','jpg'])
    if image_path is not None:
      img=Image.open(image_path)
      img=ImageOps.fit(img,(150,150),Image.ANTIALIAS)
      result=processing(img,model)
      result=classes[result]
      with st.spinner('Analysing the picture'):
        time.sleep(5)
        st.image(image_path,caption=result)
        st.markdown('**The name of the type is:-**')
        st.balloons()
        st.subheader(result) 


#---------------------------------------------------------------------

elif(selected=='Hire me👨‍🎓'):
  st.header('About me')
  st.markdown("""**I have recently graduate in 2021 and was not able to get a job in campus placement.So for last 3 months I have being reworking 
  for my passion in data science.I am currently doing internship upder Almabetter.**""")
  st.text(' ')
  st.text('  ')
  st.markdown('**A chance  would be appreciated 🙏**')
  st.text(' ')
  st.subheader('Contact:-')
  st.markdown('**Phone ☎️ :- 6202239544**')
  st.markdown('**Email 📧 :- rahuljha0610@gmail.com**')
  st.markdown('**Linkedin 🚦 :- [link](https://www.linkedin.com/in/rahul-jha-600047164/)**')
  
