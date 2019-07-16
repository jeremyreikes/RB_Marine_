import pandas as pd

def get_animal_data():
    all_animals_url = 'https://0162ago2m5.execute-api.us-east-2.amazonaws.com/prod/life'
    individual_animal_url = 'https://0162ago2m5.execute-api.us-east-2.amazonaws.com/prod/life/{}/track'

    req = requests.get(all_animals_url)
    info = pd.read_json(req.text)

    animals = pd.DataFrame(info)
    all_ping_data = pd.DataFrame()
    for i in range(0, 500):
        response = requests.get(individual_animal_url.format(i))
        if response.status_code == 200:
            current_pings = pd.read_json(response.text)
            current_pings['id'] = current_pings['id'].apply(lambda x: i)
            all_ping_data = pd.concat([all_ping_data, current_pings], axis=0)
    animal_data = pd.merge(all_ping_data, animals, on='id', how='left')
    return animal_data
