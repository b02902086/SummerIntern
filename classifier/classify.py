from watson_developer_cloud import NaturalLanguageClassifierV1
import json
import sys

natural_language_classifier = NaturalLanguageClassifierV1(username='aeb5ab44-e7d9-471d-a33c-5a373577f6d6',password='KuHALDJPT3GZ')

sentence = ''
for i in range(len(sys.argv)-2):
	sentence = sentence + sys.argv[i+2] + ' '
classes = natural_language_classifier.classify(sys.argv[1], sentence[:-1])
print(json.dumps(classes, indent=2))