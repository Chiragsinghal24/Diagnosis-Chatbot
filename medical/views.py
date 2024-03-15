import pickle
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import json
from django.views.decorators.csrf import csrf_exempt
from .respond import func
from .heart import heart_data
from .stomach import stomach_data
from .lung import lung_data
from .skin import skin_data
# Create your views here.
i=0
li=[]
@csrf_exempt
def serve(request):
    # global orgn
    # global problem
    # global body_part
    # global med_history
    # global gender
    global i
    global li
    if request.method=='POST':
     data=json.loads(request.body.decode("utf-8"))
     intent=data["queryResult"]["intent"]["displayName"]
     if(intent=="Initial"):
        name=data["queryResult"]["outputContexts"][0]["parameters"]["name"]
        print("Name is: ",name)
        val=name[0]
        print("Value is: ",val)
        feed=func(val)
        response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [feed],
                        }
                    }
                ]
        }
        return JsonResponse(response)
     if intent=="Organ":
        org=data["queryResult"]["outputContexts"][0]["parameters"]["organ"]
        print("Organ is: ",org)
        orgn=org
        li.append(orgn)
        print("I is ",i)
        i=i+1
        if orgn=="Skin":
           message="Please tell that what you are exactly facing and where you are facing that along with how much time you are facing the problem"
           response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [message],
                        }
                    }
                ]
           }
           return JsonResponse(response)
        if orgn=="Chest" or orgn=="Stomach" or orgn=="Breath" or orgn=="Abdomen":
           message="Please tell that what your problem and what is your current medical history"
           response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [message],
                        }
                    }
                ]
           }
           return JsonResponse(response)
           
        else:
           message=f"Please elaborate your issue with the respective body part: {orgn} "
           response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [message],
                        }
                    }
                ]
           }
           return JsonResponse(response)
    #  if intent=="Problem":
    #     problems=data["queryResult"]["outputContexts"][0]["parameters"]["Symptoms"]
    #     print("Problem is: ",problems)
    #     problem=problems[0]
    #     print("Extracted problem is: ",problem)
    #     message=f" Tell your gender please for better understanding"
    #     response = {
    #             "fulfillmentMessages": [
    #                 {
    #                     "text": {
    #                         "text": [message],
    #                     }
    #                 }
    #             ]
    #     }
        return JsonResponse(response)
     if intent=="skin":
        problems=data["queryResult"]["outputContexts"][0]["parameters"]["Symptoms.original"]
        problem=problems[0]
        print("Problem is: ",problem)
        li.append(problem)
        print("I is : ",i)
        i=i+1
        body_part=data["queryResult"]["outputContexts"][0]["parameters"]["body-part"][0]
        li.append(body_part)
        print("I is: ",i)
        i=i+1
        duration=data["queryResult"]["outputContexts"][0]["parameters"]["duration.original"]
        print("Duration is: ",duration)
        li.append(duration)
        print("I is ",i)
        i=i+1
        message=f" Tell your gender please for better understanding"
        response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [message],
                        }
                    }
                ]
        }
        return JsonResponse(response)
     if intent=="other":
        problems=data["queryResult"]["outputContexts"][0]["parameters"]["Symptoms.original"]
        problem=problems[0]
        print("Problem is: ",problem)
        print("I is: ",i)
        i=i+1
        # duration=data["queryResult"]["outputContexts"][0]["parameters"]["duration.original"]
        # print("Duration is: ",duration)
        
        li.append(problem)
        medical_history=data["queryResult"]["parameters"]["Med-History"][0]
        li.append(medical_history)
        print("I is: ",i)
        i=i+1
        #medical_his=
        message=f" Tell your gender please for better understanding"
        response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [message],
                        }
                    }
                ]
        }
        return JsonResponse(response)
     if intent=="gender":
        gender=data["queryResult"]["parameters"]["sex"]
        message=f" This was the last intent"
        response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [message],
                        }
                    }
                ]
        }
        li.append(gender)
        print("I is: ",i)
        i=i+1
        if li[0]=="Skin":
         prediction=-1
         print("Organ is: ",li[0])
         print("Problem ",li[1])
         print("Body Part: ",li[2])
         print("Duration: ",li[3])
         print("Gender: ",li[4])
         print("Organ is : ",li[0])
         prediction=skin_data(li[1],li[2],li[4])
         print("Severity level is: ",prediction)
         li.clear()
         df=pd.read_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Skin Disease.csv")
        # print("Duration is: ",duration)
        #  message=f" This was the last intent"
         if prediction==1:
            prediction="Moderate"
         elif prediction==0:
            prediction="Mild"
         elif prediction==3:
            prediction="Uncertain"
         else:
            prediction="Severe"
         set=df[df["scaled_severity"]==prediction]
         message=f"By recieving and interprating on the parameters our prediction is that level of Skin related disease {prediction}"
         response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [message],
                        }
                    }
                ]
         }
         return JsonResponse(response)

        else:
         print("Organ is: ",li[0])
         print(li[1])
         print(li[2])
         print(li[3])
         prediction=-1
         if li[0]=="Chest" or li[0]=="Heart":
            prediction=-1
            print("Organ is: ",li[0])
            prediction=heart_data(li[1],li[2],li[3])
            print("Severeity level:  ",prediction)
            if prediction==0:
               prediction=="Critical"
            elif prediction==1:
               prediction="Low"
            elif prediction==2:
               prediction="Medium"
            else:
               prediction="severe"
            message=f"By recieving and interprating on the parameters our prediction is that level of Heart related disease {prediction}"
         elif li[0]=="Stomach" or li[0]=="Abdomen":
            prediction=-1
            print("Organ is: ",li[0])
            prediction=stomach_data(li[1],li[2],li[3])
            print("Severeity level:  ",prediction)
            if prediction==0:
              prediction="Low"
            elif prediction==1:
              prediction="Medium"
            else:
               prediction="severe"
            message=f"By recieving and interprating on the parameters our prediction is that level of Stomach related disease {prediction}"
         else:
            print("Organ is: ",li[0])
            prediction=lung_data(li[1],li[2],li[3])
            print("Severeity level:  ",prediction)
            if(prediction==3):
               prediction="Low"
            elif prediction==4 or prediction==6:
               prediction="Medium" 
            else:
               prediction="Severe"
            message=f"By recieving and interprating on the parameters our prediction is that level of Lung related disease {prediction}"
         gender=data["queryResult"]["parameters"]["sex"]
         response = {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [message],
                        }
                    }
                ]
          }
         li.clear()
         i=0
         return JsonResponse(response)

