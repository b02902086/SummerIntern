import json
import sys
from watson_developer_cloud import NaturalLanguageClassifierV1
natural_language_classifier = NaturalLanguageClassifierV1(username='aeb5ab44-e7d9-471d-a33c-5a373577f6d6',password='KuHALDJPT3GZ')


with open(sys.argv[2], 'rb') as training_data:
  classifier = natural_language_classifier.create(
    training_data=training_data,
    name=sys.argv[1],
    language='en'
  )
print(json.dumps(classifier, indent=2))