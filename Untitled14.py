#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[12]:


def fetch_ae_data(drug_name):
    """Fetch adverse event data for a specific drug from the OpenFDA API."""
    url = f'https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:"{drug_name}"&limit=10'
    response = requests.get(url)
    data = response.json()
    return data


# In[13]:


def extract_ae_terms(data):
    """Extract adverse event terms from the fetched data."""
    ae_terms = []
    if 'results' in data:
        for result in data['results']:
            for ae in result['patient']['reaction']:
                ae_terms.append(ae['reactionmeddrapt'])
    return ae_terms


# In[14]:


def display_adverse_events(drug_name):
    """Fetch and display adverse events for a given drug."""
    print(f"Fetching adverse events for {drug_name}...")
    data = fetch_ae_data(drug_name)
    ae_terms = extract_ae_terms(data)
    if ae_terms:
        print(f"Adverse Events for {drug_name}:")
        for ae in ae_terms:
            print(f"- {ae}")
    else:
        print(f"No adverse events found for {drug_name}.")


# In[15]:


if __name__ == "__main__":
    drug_name = input("Enter the drug name: ")
    display_adverse_events(drug_name)


# In[ ]:




