import pickle
from django.http import JsonResponse
from sklearn.preprocessing import LabelEncoder
def heart_data(data):
     sex=data["sex"]
     symptoms=data["symptoms"]
     history=data["history"]
     df=pd.read_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Heart Disease.csv")
     le_sex=LabelEncoder()
     le_symp=LabelEncoder()
     le_his=LabelEncoder()
     se=[]
     se.append(sex)
     symp=[]
     symp.append(symptoms)
     his=[]
     his.append(history)
     
     scaled_sex=le_sex.fit_transform(se)
     scaled_symptoms=le_symp.fit_transform(symp)
     scaled_history=le_his.fit_transform(his)
     with open("C:/MedTech_DJ_Backend/med_backend/medical/heart_model.pkl","rb") as f:
        model=pickle.load(f,encoding='utf-8')
     print(model)
     return JsonResponse({"message":"Hello from the backend"})