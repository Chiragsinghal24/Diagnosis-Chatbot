import pandas as pd
from sklearn.preprocessing import LabelEncoder
def refine_heart():
  heart=pd.read_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Heart Disease.csv")
  X=heart['Sex']
  Y=heart['Symptoms']
  Z=heart['Medical History']
  W=heart['Severity']
  le_sex=LabelEncoder()
  le_sym=LabelEncoder()
  le_medh=LabelEncoder()
  le_sev=LabelEncoder()
  A=le_sex.fit_transform(X)
  B=le_sym.fit_transform(Y)
  C=le_medh.fit_transform(Z)
  D=le_sev.fit_transform(W)
  heart['scaled_sex']=A
  heart['scaled_symptoms']=B
  heart['scaled_history']=C
  heart['scaled_severity']=D
  print(heart.head(4))
  heart.to_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Heart Disease.csv",index=False)
def refine_lung():
  lung=pd.read_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Lung Disease.csv")
  X=lung['Sex']
  Y=lung['Symptoms']
  Z=lung['Medical History']
  W=lung['Severity']
  le_sex=LabelEncoder()
  le_sym=LabelEncoder()
  le_medh=LabelEncoder()
  le_sev=LabelEncoder()
  A=le_sex.fit_transform(X)
  B=le_sym.fit_transform(Y)
  C=le_medh.fit_transform(Z)
  D=le_sev.fit_transform(W)
  lung['scaled_sex']=A
  lung['scaled_symptoms']=B
  lung['scaled_history']=C
  lung['scaled_severity']=D
  print(lung.head(4))
  lung.to_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Lung Disease.csv",index=False)

def refine_skin():
  skin=pd.read_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Skin Diseases.csv")
  X=skin['Sex']
  Y=skin['Skin Problem']
  Z=skin['Location on Body']
  W=skin['Severity']
  le_sex=LabelEncoder()
  le_sym=LabelEncoder()
  le_medh=LabelEncoder()
  le_sev=LabelEncoder()
  A=le_sex.fit_transform(X)
  B=le_sym.fit_transform(Y)
  C=le_medh.fit_transform(Z)
  D=le_sev.fit_transform(W)
  skin['scaled_sex']=A
  skin['scaled_skin_problem']=B
  skin['scaled_location']=C
  skin['scaled_severity']=D
  print(skin.head(4))
  skin.to_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Skin Disease.csv",index=False)

def refine_stomach():
  stomach=pd.read_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Stomach Disease.csv")
  X=stomach['Sex']
  Y=stomach['Symptoms']
  Z=stomach['Medical History']
  W=stomach['Severity']
  le_sex=LabelEncoder()
  le_sym=LabelEncoder()
  le_medh=LabelEncoder()
  le_sev=LabelEncoder()
  A=le_sex.fit_transform(X)
  B=le_sym.fit_transform(Y)
  C=le_medh.fit_transform(Z)
  D=le_sev.fit_transform(W)
  stomach['scaled_sex']=A
  stomach['scaled_symptoms']=B
  stomach['scaled_history']=C
  stomach['scaled_severity']=D
  print(stomach.head(4))
  stomach.to_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Stomach Disease.csv",index=False)

refine_heart()
refine_lung()
refine_skin()
refine_stomach()
