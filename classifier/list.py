import json
import sys
from watson_developer_cloud import NaturalLanguageClassifierV1
natural_language_classifier = NaturalLanguageClassifierV1(username='aeb5ab44-e7d9-471d-a33c-5a373577f6d6',password='KuHALDJPT3GZ')


classifiers = natural_language_classifier.list()
print(json.dumps(classifiers, indent=2))