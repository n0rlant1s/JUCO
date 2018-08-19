from clarifai.rest import ClarifaiApp

app = ClarifaiApp()
model = app.public_models.general_model
response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')


concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])
