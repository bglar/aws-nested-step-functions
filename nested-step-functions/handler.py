def get_personal_data(event, context):
    return {
        "name": "Sheldon Cooper",
        "dob": "1980-04-04",
        "nationality": "Kenyan",
        "gender": "Male",
    }


def get_gender(event, context):
    person_data = event['AWS_STEP_FUNCTIONS_STARTED_BY_EXECUTION_INPUT']
    return {"gender": person_data["gender"]}
