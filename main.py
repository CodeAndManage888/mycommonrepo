import requests

def get_drugs_for_disease(disease):
    api_url = "https://api.fda.gov/drug/label.json"
    # Construct the query parameters
    query = {
        "search": f'indications_and_usage:"{disease}"',
        "limit": "25"  # Retrieve the top 25 results
    }
    # Make the GET request to the OpenFDA API
    response = requests.get(api_url, params=query)
    # Parse the JSON response
    data = response.json()

    # Check if the response contains results
    if 'results' in data:
        drugs = []
        for item in data['results']:
            if 'openfda' in item and 'brand_name' in item['openfda']:
                drug_info = {
                    'Brand Name': item['openfda']['brand_name'][0],
                    'Efficacy Info': item.get('clinical_studies', 'No clinical studies info available')
                }
                drugs.append(drug_info)
        return drugs
    else:
        return "No results found."

# Example usage
disease = "diabetes"
drugs = get_drugs_for_disease(disease)
for drug in drugs:
    print(f"Drug: {drug['Brand Name']}")