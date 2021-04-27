from csv import DictReader
import json


def build_dramp_to_pep_index():
    INDEX = {}

    with open("utils/full.csv") as csv_fd:
        reader = DictReader(csv_fd)
        
        pep_id = 2
        for row in reader:
            dramp_id = row["DRAMP_ID"][5:]
            INDEX[dramp_id] = pep_id

            pep_id += 1


    with open("static/js/dramp_to_pep_index.js", "w+") as index_fd:
        index_str = json.dumps(INDEX)
        contents = f"const DRAMP_TO_PEP = JSON.parse(\"{index_str}\");"
        index_fd.write(contents)


def build_pep_to_dramp_index():
    INDEX = {}

    with open("utils/full.csv") as csv_fd:
        reader = DictReader(csv_fd)
        
        pep_id = 2
        for row in reader:
            dramp_id = row["DRAMP_ID"][5:]
            INDEX[pep_id] = dramp_id

            pep_id += 1


    with open("static/js/pep_to_dramp.js", "w+") as index_fd:
        index_str = json.dumps(INDEX)
        contents = f"const DRAMP_TO_PEP = JSON.parse(\"{index_str}\");"
        index_fd.write(contents)


def build_pep_to_activity_index():
    INDEX = {}

    ACTIVITY_TO_ID = {
        "Anti-Gram+": 1,
        "Anti-Gram-": 2,
    }

    with open("utils/full.csv") as csv_fd:
        reader = DictReader(csv_fd)
        
        pep_id = 2
        for row in reader:
            activities = 0
            str_activities = row["Activity"].split(",")
            for str_activity in str_activities:
                str_activity = str_activity.strip()
                if str_activity:
                    if not ACTIVITY_TO_ID.get(str_activity):
                        continue

                    activities += ACTIVITY_TO_ID[str_activity]
            

            INDEX[pep_id] = activities
            pep_id += 1


    with open("static/js/pep_to_activity_index.js", "w+") as index_fd:
        index_str = json.dumps(INDEX)
        contents = f"const DRAMP_TO_PEP = JSON.parse(\"{index_str}\");"
        index_fd.write(contents)