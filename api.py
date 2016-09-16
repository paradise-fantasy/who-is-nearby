#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
from Person import Person

def get_members():
    members = []
    getMembers = (urllib2.urlopen("http://paradise-backend.herokuapp.com/api/members").read())

    for person in json.loads(getMembers):
        members.append(Person(  person['id'],
                                person['name'].encode('utf-8'),
                                person['bluetooth_address'],
                                person['color'],
                                person['room']))
    return members
