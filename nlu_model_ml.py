# -*- coding: utf-8 -*-
"""
Written by: Vijay Sanjos Alexander
Email: vijaysanjosalexander@gmail.com
Copyright (c) 2017, VSA.
License: MIT (see LICENSE for details)
"""

import sys
import os
import json
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as features
file_dir = "D:/Users/"
nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username= 'YOUR_USER_NAME',
    password= 'YOUR_PASSWORD')

for f in os.listdir(file_dir):
    if f.endswith(".txt"):
        path = os.path.join(file_dir, f)
        print "Parsing file: {}".format(path)
        # Open the work book
        book = open(path, 'r').read()
        response = nlu.analyze(text=book, features=[features.Entities(model='YOUR_CUSTOM_MODEL_ID / LEAVE_BLANK_FOR_WATSON_OPEN_MODEL'), features.Relations(model='YOUR_CUSTOM_MODEL_ID / LEAVE_BLANK_FOR_WATSON_OPEN_MODEL')])
        ff = os.path.splitext(f)[0]
        # Output file generated
        file_name = "{0}nlu_output-{1}.json".format(file_dir, ff)
        print "Writing to file: {}".format(file_name)
        nlu_file = open(file_name, 'w')
        nlu_text = json.dumps(response, indent=2)
        nlu_file.write(nlu_text)


