import requests


def presidents():
    url = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'

    # Get the data about the presidents
    response = requests.get(url)

    # Read that data into a variable
    json_data = response.json()

    # Populate list with President names from Text entries in Related Topics
    pres_list = []
    related_topics = json_data['RelatedTopics']
    for text in related_topics:
        pres_list.append(text["Text"])

    # Printed list to check if all the presidents are listed
    print(pres_list)
    return pres_list

presidents()