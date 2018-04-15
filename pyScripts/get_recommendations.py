'''
  Generates recommendation for the user based on
  bmi, smoking, tobacco usage, alcohol consumption, exercise
  travel time, sleep time, job type.
'''
healthy_bmi = 0
moderate_travel = 1
excess_travel = 2
low_sleep = 0
moderate_sleep = 1
no_exercise = 0
moderate_exercise = 1
optimal_exercise = 2
def getBmiRec(bmi_number):
    
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
def processRecommendations(data):
    recs = {}
    recs["bmi"] = getBmiRec(data["bmi"][0])
    recs["drink"] = getDrinkRec(data["drink"][0])
    recs["exercise"] = getExerciseRec(data["exercise"][0])
    recs["smoke"] = getSmokeRec(data["smoke"][0])
    recs["tobacco"] = getTobaccoRec(data["tobacco"][0])
    recs["travel_time"] = getTravelRec(data["travel_time"][0])
    recs["sleep_time"] = getSleepRec(data["sleep_time"][0])
    return recs
if __name__ == "__main__":
    data = {}
    data["exercise"] = [0,3]
    data["travel_time"] = [0,3]
    data["sleep_time"] = [0,3]
    data["drink"] = [1,2]   
    data["tobacco"] = [1,2]
    data["smoke"] = [1,2]
    data["bmi"] = [1,2]
    print (processRecommendations(data))
    