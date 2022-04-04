web: sh setup.sh && streamlit run app.py


st.text('')
st.text('')
st.markdown("""**Cirrhosis, also known as liver cirrhosis or hepatic cirrhosis, and end-stage liver disease, is the impaired liver function caused by the formation of scar tissue known as fibrosis due to damage caused by liver disease.[9] Damage causes tissue repair and subsequent formation of scar tissue, which over time can replace normal functioning tissue, leading to the impaired liver function of cirrhosis.[9][10] The disease typically develops slowly over months or years.[1] Early symptoms may include tiredness, weakness, loss of appetite, unexplained weight loss, nausea and vomiting, and discomfort in the right upper quadrant of the abdomen.[2] As the disease worsens, symptoms may include itchiness, swelling in the lower legs, fluid build-up in the abdomen, 
jaundice, bruising easily, and the development of spider-like blood vessels in the skin.**""")

st.image('OIP (6).jpg',width=300)
st.text('')
st.text('')
st.subheader('About the dataset:-')
st.text('')
st.text(' ')
st.markdown("""**The following data contains the information collected from the Mayo Clinic trial in primary biliary cirrhosis (PBC) of the liver conducted between 1974 and 1984. A description of the clinical background for the trial and the covariates recorded here is in Chapter 0, especially Section 0.2 of Fleming and Harrington, Counting
Processes and Survival Analysis, Wiley, 1991. A more extended discussion can be found in Dickson, et al., Hepatology 10:1-7 (1989) and in Markus, et al., N Eng J of Med 320:1709-13 (1989).
A total of 424 PBC patients, referred to Mayo Clinic during that ten-year interval, met eligibility criteria for the randomized placebo-controlled trial of the drug D-penicillamine. The first 312 cases in the dataset participated in the randomized trial and contain largely complete data. The additional 112 cases did not participate in the clinical trial but consented to have basic measurements recorded and to be followed for survival. Six of those cases were lost to follow-up
 shortly after diagnosis, so the data here are on an additional 106 cases as well as the 312 randomized participants**""")

st.text(' ')
st.text(' ')

st.subheader('Working of the model:-')
def user_input_features():
  Sex=st.selectbox('Gender of the patient:-',['M','F'])
  Ascites=st.selectbox('Ascites(presence of ascites)',['Y','N'])
  Hepatomegaly=st.selectbox('Hepatomegaly(presence of hepatomegaly)',['Y','N'])
  Spiders=st.selectbox('**Spiders**: presence of spiders ',['Y','N'])
  Edema=st.selectbox('**Endema**: presence of endema ',['N','Y','S'])
  Bilirubin=st.slider('Bilirubin: serum bilirubin in [mg/dl]',1,28,key=int)
  Cholesterol=st.slider('serum cholesterol in [mg/dl]',120,1775,key=int)
  Albumin=st.slider(' Albumin: albumin in [gm/dl]',0,5,key=int)
  Copper=st.slider('Copper: urine copper in [ug/day]',4,588,key=int)
  Alk_Phos=st.slider(' Alk_Phos: alkaline phosphatase in [U/liter]',192,13862,key=int)
  Tryglicerides=st.slider(' Triglycerides: triglicerides in [mg/dl]',65,598,key=int)
  Platelets=st.slider('platelets per cubic [ml/1000]',200,600,key=int)
  Prothrombin=st.slider('Prothrombin: prothrombin time in seconds [s]',9,18,key=int)
  Stage=st.selectbox('Stage of the patient:-',[1,2,3,4])
  data = {
            'Sex':Sex,
            'Ascites': Ascites,
            'Hepatomegaly': Hepatomegaly,
            'Spiders': Spiders,
            'Edema':Edema,
            'Bilirubin':Bilirubin,
            'Cholesterol': Cholesterol,
          'Albumin': Albumin,
            'Copper':Copper,
            'Alk_Phos':Alk_Phos,
          'Tryglicerides':Tryglicerides,
            'Platelets':Platelets,
            'Prothrombin':Prothrombin,
          'Stage':Stage
            }
  features = pd.DataFrame(data, index=[0])
  return features
df = user_input_features()

st.write(df)
df['Sex']=df['Sex'].replace({'F':1,'M':0})
df['Ascites']=df['Ascites'].replace({'Y':1,'N':0})
df['Hepatomegaly']=df['Hepatomegaly'].replace({'Y':1,'N':0})
df['Spiders']=df['Spiders'].replace({'Y':1,'N':0})
df['Edema']=df['Edema'].replace({'N':0,'S':1,'Y':2})

reg=['Prothrombin','Platelets','Tryglicerides','Alk_Phos','Copper','Bilirubin','Cholesterol']

#-----------------------------------------------------------------------------------------------
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()
df[reg]=pd.DataFrame(scale.fit_transform(df[reg]),columns=reg)
#------------------------------------------------------------------------------------------------

from sklearn.preprocessing import PowerTransformer

power=PowerTransformer(method='yeo-johnson')
df[reg]=pd.DataFrame(power.fit_transform(df[reg]),columns=reg)

from sklearn.impute import SimpleImputer

impute=SimpleImputer(strategy='most_frequent')
col=['Ascites','Hepatomegaly','Spiders','Stage']

df[col]=pd.DataFrame(impute.fit_transform(df[col]),columns=col)
df[col]=df[col].dropna()

impute=SimpleImputer(strategy='median')


df=pd.DataFrame(impute.fit_transform(df),columns=df.columns)
model1=joblib.load('cirrhosis.h5')
result=model1.predict_proba(df)
one=np.argmax(result)
res={0:'C (censored)',1:'CL (censored due to liver tx)',2:'D (death)'}
a=res[one]
st.subheader(a)
