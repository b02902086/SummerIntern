from watson_developer_cloud import NaturalLanguageClassifierV1
import json
import sys

natural_language_classifier = NaturalLanguageClassifierV1(username='021a2087-a56b-4296-b5c1-d29f44be4987',password='2Tzpri7E1omT')


classes = natural_language_classifier.remove(sys.argv[1])
print(json.dumps(classes, indent=2))