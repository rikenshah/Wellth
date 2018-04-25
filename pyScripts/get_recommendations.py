'''
  Generates recommendation for the user based on
  bmi, smoking, tobacco usage, alcohol consumption, exercise
  travel time, sleep time, job type.
'''
import csv, re

featureWeights_dict={}

healthy_bmi = 0
moderate_travel = 1
excess_travel = 2
low_sleep = 0
moderate_sleep = 1
no_exercise = 0
moderate_exercise = 1
optimal_exercise = 2

def preprocessData(data):
    # print("Recoomendation preprocess")
    # print(data)
    data["exercise"] = [data["exercise"],3]
    data["travel_time"] = [data["travel_time"],3]
    data["sleep_time"] = [data["sleep_time"],3]
    data["drink"] = [1 if data["drink"] else 0,2]   
    data["tobacco"] = [1 if data["tobacco"] else 0,2]
    data["smoke"] = [1 if data["smoke"] else 0,2]

    """Bag of words to identify past ailments and dangerous job types"""

    ailments=set(['heart','brain','kidney','liver','breating','asthema'])
    job_type=set(['army','defence','factory'])
    #pattern = re.compile("\s+|^\s+|\s*,*\s*|\s+$")
    pattern = re.compile("\s+,*\s*")
    current_ailments = set([ x for x in pattern.split(data["ailments"]) if x])
    current_jobtype = set([ x for x in pattern.split(data["job_type"]) if x])
    data["ailments"] = [1 if current_ailments.intersection(ailments) else 0,2]
    data["job_type"] = [1 if current_jobtype.intersection(job_type) else 0,2]

    """Identifying Healthy BMI & Age range"""
    
    data["age"]=[0 if data["age"]>18 and data["age"]<45 else 1,2]
    data["bmi"]=data["weight"]/(data["height"]*data["height"])*703
    data["bmi"]=[0 if data["bmi"]>18.5 and data["bmi"]<24.9 else 1,2]
    # print("preprocess",data)
    return data

def initialize_feature_weights():
    reader = csv.reader(open('pyScripts/feature_weights.csv'))
    for row in reader:
        value=[]
        split_row= row[0].split('\t')
        key=split_row[0]
        value=split_row[1:]
        featureWeights_dict[key]=value
    # print(featureWeights_dict)
    return featureWeights_dict

#Calculates the number of points healthscore will improve, rounded to 2 decimals
def getPointsForImprovement(current,levels, weight, maxHealthScore):
    return (round((float(weight) * maxHealthScore * (current/levels)) , 2))
    
def getBmiRec(bmi_data):
    if bmi_number != healthy_bmi:
        return ("If you get your bmi (body-mass-index) in the healthly range "
    "(18.5 - 24. 9) your healthscore will improve 100 points.")
    return None

def getDrinkRec(drinks):
    if drinks: #drinks alcohol
        return ("If you stop drinking alcohol your healthscore will improve by "
    " 50 points.")
    return None

def getExerciseRec(exercise):
    if exercise == no_exercise:
        return ("If start exercising 6 hours a week your healthscore will improve "
        " 17 points.")
    elif exercise == moderate_exercise:
        return ("If you exercise more than 15 hours a week "
        " your healthscore will improve 17 points.")
    return None

def getSmokeRec(smokes):
    if smokes:
        return ("If you quit smoking your healthscore will improve 50 points.")
    return None

def getTobaccoRec(uses_tobacco):
    if uses_tobacco:
        return ("If you stop using tobacco your healthscore will improve 50 points.")
    return None

def getTravelRec(travel_time):
    if travel_time == excess_travel:
        return ("If you reduce your travel_time to under 10 hours "
        "your healthscore will improve 17 points.")
    elif travel_time == moderate_travel:
        return ("If you reduce your travel_time to under 5 hours "
        "your healthscore will improve 17 points.")
    return None

def getSleepRec(sleep):
    if sleep == low_sleep:
        return ("If you increase sleep to more than 6 hours a day "
        "your healthscore will improve 17 points.")
    elif sleep == moderate_sleep:
        return ("If you increase your sleep to more than 8 hours a day "
        "your healthscore will improve 17 points.")
    return None

#Calculates improvement for a key
def getRecommendationPointsForKey(data, featureWeight, maxHealthScore):
    if featureWeight[1] == 'negative':
        return getNegativeRecommendation(data, featureWeight[0], maxHealthScore)
    return getPositiveRecommendation(data, featureWeight[0], maxHealthScore)
#Calculates improvement for a key that has a negative relationship
def getNegativeRecommendation(data, weight, maxHealthScore):
    if data[0] == 0:
        return None
    return getPointsForImprovement(data[0],data[1], weight, maxHealthScore)
    
#Calculates improvement for a key that has a positive relationship
def getPositiveRecommendation(data, weight, maxHealthScore):
    if data[0] != 2:
        print("New method")
        print(type(weight))
        print(weight)
        print(data)
        # return getPointsForImprovement(data[1], weight, maxHealthScore)
        return float(weight)*((data[1]-data[0]-1)/data[1])*maxHealthScore
    return None


def initializeStrDic():
    return{"smoke" : ["", "stop smoking"], "exercise" : ["increase your exercise to atleast 6 hours a week", "increase your exercise to atleast 15 hours a week"], "sleep_time": ["increase the amount you sleep to atleast 6 hours a day","increase the amount you sleep to above 8 hours a day"], "bmi": ["", "get your bmi in the healthy range (18.5 - 24 .9)"],"drink": ["", "stop drinking"], "tobacco": ["", "stop using tobacco"], "travel_time" : ["", "reduce the travel time to less than 5 hours","reduce the travel to less than 10 hours"]}

def processRecommendations(data, maxHealthScore):
    '''
    recs = {}
    recs["bmi"] = getBmiRec(data["bmi"], featureWeights["bmi"], maxHealthScore)
    recs["drink"] = getDrinkRec(data["drink"][0], featureWeights["drink"], maxHealthScore)
    recs["exercise"] = getExerciseRec(data["exercise"][0], featureWeights["exercise"], maxHealthScore)
    recs["smoke"] = getSmokeRec(data["smoke"][0], featureWeights["smoke"], maxHealthScore)
    recs["tobacco"] = getTobaccoRec(data["tobacco"][0], featureWeights["tobacco"], maxHealthScore)
    recs["travel_time"] = getTravelRec(data["travel_time"][0], 
    featureWeights["travel_time"], maxHealthScore)
    recs["sleep_time"] = getSleepRec(data["sleep_time"][0], featureWeights["sleep_time"], maxHealthScore )
    '''

    print("processRecommendations")
    data = preprocessData(data)
    print(data)
    all_recommendations = []
    print("end")
    featureWeights = initialize_feature_weights()
    points = 0.0
    resultStrings = []
    recStrDic = initializeStrDic()    
    print("recStrDict : ",recStrDic)
    for key in ["exercise","sleep_time","drink","tobacco","smoke","bmi","travel_time"]:
        result = getRecommendationPointsForKey(data[key], featureWeights[key], maxHealthScore)
        if result is not None:
            points += result
            print("Result is ",result);
            resultStrings.append(recStrDic[key][data[key][0]])
            all_recommendations.append(getRecommendationString([recStrDic[key][data[key][0]]],result))

    all_recommendations.append(getRecommendationString(resultStrings, points))

    # for key in ["exercise","sleep_time","drink","tobacco","smoke","bmi","travel_time"]:
    #     all_recommendations.append(getRecommendationString([recStrDic[key][data[key][0]]],getRecommendationPointsForKey(data[key], featureWeights[key], maxHealthScore)))
    all_recommendations = [all_recommendations[-1]]+all_recommendations[0:len(all_recommendations)-1]
    return all_recommendations,round((points/maxHealthScore*data["healthcare_costs"]),2)
    
def getRecommendationString(resultStrings, points):
  recommendationString = "If you "
  resultStringsLength = len(resultStrings)
  if resultStringsLength == 0:
    return ["You are in good shape."]
  for index in (range(resultStringsLength - 1)):
    recommendationString += (resultStrings[index] + ", ")
  recommendationString += ("and " + resultStrings[resultStringsLength -1] + 
  " your healthscore will improve by " + str(round(points, 2)) + " points.")
  return recommendationString
  
    
if __name__ == "__main__":
    data = {}
    data["exercise"] = [0,3]
    data["travel_time"] = [0,3]
    data["sleep_time"] = [0,3]
    data["drink"] = [1,2]   
    data["tobacco"] = [1,2]
    data["smoke"] = [1,2]
    data["bmi"] = [1,2]
    
    featureWeights = {'age': ['0.1', 'negative'], 'bmi': ['0.2', 'negative'], 
    'ailments': ['0.2', 'negative'], 'tobacco': ['0.1', 'negative'], 'smoke': ['0.1', 'negative'],
    'drink': ['0.1', 'negative'], 'exercise': ['0.05', 'positive'], 'travel_time': ['0.05', 'negative'], 
    'sleep_time': ['0.05', 'positive'], 'job_type': ['0.05', 'negative']}
    
    print(processRecommendations(data, 1000))
