import json
import sys
from watson_developer_cloud import NaturalLanguageClassifierV1
natural_language_classifier = NaturalLanguageClassifierV1(username='021a2087-a56b-4296-b5c1-d29f44be4987',password='2Tzpri7E1omT')


with open(sys.argv[2], 'rb') as training_data:
  classifier = natural_language_classifier.create(
    training_data=training_data,
    name=argv[1],
    language='en'
  )
print(json.dumps(classifier, indent=2))