#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib2
import json
from Person import Person

url_get_members = "http://api.komstek.no/api/users"

def get_members():
    members = []
    getMembers = (urllib2.urlopen(url_get_members).read())

    for person in json.loads(getMembers):
        members.append(Person(  person['_id'],
                                person['name'].encode('utf-8'),
                                person['bluetooth_address'],
                                person['color'],
                                person['room']))
    return members
