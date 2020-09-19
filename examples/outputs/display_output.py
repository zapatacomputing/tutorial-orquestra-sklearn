import json
import pandas as pd

import json
with open('./examples/outputs/tutorial-1-84deb2de-d2bd-442a-ab16-5621e098d8d8.json') as f:
    data = json.load(f)

steps = list(data.keys())

for step in steps:
    result = data[step]['result']
    print("Predictions")
    for prediction in result['predictions']:
        print(prediction['predictions'])
    print()
    print("Accuracy")
    print(result["accuracy"])
