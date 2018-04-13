import csv

maxHealthScore = 1000
featureWeights_dict={}

def initialize():
    reader = csv.reader(open('../datasets/feature_weights.csv'))
    for row in reader:
        value=[]
        split_row= row[0].split('\t')
        key=split_row[0]
        value=split_row[1:]
        featureWeights_dict[key]=value
    print(featureWeights_dict)

def getHealthScore(input_dict):
    healthScore = 0
    for key in input_dict:
        weight = float(featureWeights_dict[key][0])
        value = maxHealthScore
        if featureWeights_dict[key][1]=='negative' :
            value = value - (value*input_dict[key][0]/input_dict[key][1])
        elif featureWeights_dict[key][1]=='positive' :
            value = value - (value*(input_dict[key][1]-input_dict[key][0]-1)/input_dict[key][1])
        value = value * weight
        input_dict[key] = value  #optional
        healthScore = healthScore + value
    return healthScore
    
def getCostSavings(healthScore,totalHealthCost):
    savings = (maxHealthScore - healthScore)/maxHealthScore
    return savings*totalHealthCost

def preprocessData():
    

if __name__ == "__main__":
    initialize()
    input_dict = {}
    input_dict['age']=[1,3] #1 means out of healthy age range
    input_dict['bmi']=[2,3] #1 means out of healthy BMI range
    input_dict['ailments']=[0,3] #0 means no ailments 
    input_dict['tobacco']=[1,2] #binary
    input_dict['smoke']=[1,2]
    input_dict['drink']=[1,2]
    input_dict['exercise']=[2,3] #more exercise
    input_dict['travel_time']=[1 ,3]
    input_dict['sleep_time']=[2,3]
    input_dict['job_type']=[1,3] #moderate risky job
    preprocessData()
    healthScore = getHealthScore(input_dict)
    totalHealthCost = 500
    savings = getCostSavings(healthScore,totalHealthCost)
    print("Health Score is ",healthScore)
    print("Savings is ",savings)
