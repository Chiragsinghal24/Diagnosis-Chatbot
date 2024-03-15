import pickle
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import json
from django.views.decorators.csrf import csrf_exempt
from .respond import func
# Create your views here.
orgn="any"
problem="any"
body_part="any"
med_history="any"
gender="any"
duration="any"
@csrf_exempt
def serve(request):
    global org
    global problem
    global body_part
    global med_history
    global gender
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
        if orgn=="Chest" or "Stomach" or "Breath":
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
     if intent=="Problem":
        problems=data["queryResult"]["outputContexts"][0]["parameters"]["Symptoms"]
        print("Problem is: ",problems)
        problem=problems[0]
        print("Extracted problem is: ",problem)
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
     if intent=="skin":
        problems=data["queryResult"]["outputContexts"][0]["parameters"]["Symptoms.original"]
        problem=problems[0]
        print("Problem is: ",problem)
        duration=data["queryResult"]["outputContexts"][0]["parameters"]["duration.original"]
        print("Duration is: ",duration)
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
        # duration=data["queryResult"]["outputContexts"][0]["parameters"]["duration.original"]
        # print("Duration is: ",duration)
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
        print("Organ is: ",orgn)
        print("Problem is ",problem)
        print("Body Part is: ",body_part)
        print("Medical history is: ",med_history)
        print("Gender is: ",gender)
        print("Duration is: ",duration)
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
        return JsonResponse(response)

