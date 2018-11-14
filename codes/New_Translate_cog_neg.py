import sys

start = int(sys.argv[1])
end = int(sys.argv[2])


import numpy as np
import pandas as pd
import os
import re
import time

dir_name = 'Train Neg Data/'
Reviews = np.array(pd.read_csv(dir_name+'neg_reviews.csv', header=None))
Labels = np.array(pd.read_csv(dir_name+'neg_Labels.csv', header=None))

import os, requests, uuid, json

base_url = 'https://api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'
params = '&to=hi'
constructed_url = base_url + path + params

headers = {
    'Ocp-Apim-Subscription-Key': '0782b74625944c55bd63fa9dfd84af21',
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}



Translated_list = []

for i in range(start, end):
	body = [{ 'text' : Reviews[i][0][:3000] }]
	request = requests.post(constructed_url, headers=headers, json=body)
	response = request.json()
	translated = response[0]['translations'][0]['text']
	tup = (Reviews[i][0], translated, Labels[i][0] )
	print(tup)
	Translated_list.append(tup)


Translated_list_pandas = pd.DataFrame(Translated_list)
name = 'Results_neg/' + str(start) + '_' + str(end) + '.csv'
Translated_list_pandas.to_csv(name,  header=None, index=False)
