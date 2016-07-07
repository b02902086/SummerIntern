import json
import sys
from watson_developer_cloud import NaturalLanguageClassifierV1
natural_language_classifier = NaturalLanguageClassifierV1(username='021a2087-a56b-4296-b5c1-d29f44be4987',password='2Tzpri7E1omT')


classifiers = natural_language_classifier.list()
print(json.dumps(classifiers, indent=2))