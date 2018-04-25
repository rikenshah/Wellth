import csv
import json
import re
import os

maxHealthScore = 1000
featureWeights_dict={}

def initialize():
    reader = csv.reader(open('pyScripts/feature_weights.csv'))
    for row in reader:
        value=[]
        split_row= row[0].split('\t')
        key=split_row[0]
        value=split_row[1:]
        featureWeights_dict[key]=value
    print(featureWeights_dict)

def getHealthScore(input_dict):
    healthScore = 0
    for key in featureWeights_dict:
        weight = float(featureWeights_dict[key][0])
        value = maxHealthScore
        if featureWeights_dict[key][1]=='negative' :
            value = value - (value*input_dict[key][0]/input_dict[key][1])
        elif featureWeights_dict[key][1]=='positive' :
            value = value - (value*(input_dict[key][1]-input_dict[key][0]-1)/input_dict[key][1])
        value = value * weight
        input_dict[key] = value  #optional
        healthScore = healthScore + value
    # savings = getCostSavings(healthScore,input_dict["healthcare_costs"])
    # return round(healthScore,2),round(savings,2)
    return round(healthScore,2)
    
def getCostSavings(improvementPoints,healthcare_costs):
    savings = (improvementPoints)/maxHealthScore
    return savings*healthcare_costs

def preprocessData(data):
    # print("in preprocess",data)
    initialize()
    # data["exercise"] = [data["exercise"],3]
    # data["travel_time"] = [data["travel_time"],3]
    # data["sleep_time"] = [data["sleep_time"],3]
    # data["drink"] = [1 if data["drink"] else 0,2]   
    # data["tobacco"] = [1 if data["tobacco"] else 0,2]
    # data["smoke"] = [1 if data["smoke"] else 0,2]
    # """Bag of words to identify past ailments and dangerous job types"""

    # ailments=set(['heart','brain','kidney','liver','breating','asthema'])
    # job_type=set(['army','defence','factory'])
    # #pattern = re.compile("\s+|^\s+|\s*,*\s*|\s+$")
    # pattern = re.compile("\s+,*\s*")
    # current_ailments = set([ x for x in pattern.split(data["ailments"]) if x])
    # current_jobtype = set([ x for x in pattern.split(data["job_type"]) if x])
    # data["ailments"] = [1 if current_ailments.intersection(ailments) else 0,2]
    # data["job_type"] = [1 if current_jobtype.intersection(job_type) else 0,2]

    # """Identifying Healthy BMI & Age range"""
        # data["age"]=[0 if data["age"]>18 and data["age"]<45 else 1,2]
    # data["bmi"]=data["weight"]/(data["height"]*data["height"])
    # data["bmi"]=[0 if data["bmi"]>18.5 and data["bmi"]<24.9 else 1,2]
    # print("preprocess",data)
    return getHealthScore(data)

if __name__ == "__main__":
    initialize()
    input_dict = {}
    input_dict['age']=45 #1 means out of healthy age range
    input_dict['height']= 1.8 #1 means out of healthy BMI range
    input_dict['weight']=80
    input_dict['ailments']="heart ailments" #0 means no ailments 
    input_dict['tobacco']=False #binary
    input_dict['smoke']=True
    input_dict['drink']= True
    input_dict['exercise']=1 #more exercise
    input_dict['travel_time']=1
    input_dict['sleep_time']=1
    input_dict['healthcare_costs']=500
    input_dict['job_type']="" #moderate risky job
    result = preprocessData(input_dict)
    print("Health Score is ",result[0])
    print("Savings is ",result[1])
