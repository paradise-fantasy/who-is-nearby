#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib
import urllib2
import json
from Person import Person

url_get_members = "http://paradise-backend.herokuapp.com/api/members"
url_post_presence = "http://paradise-backend.herokuapp.com/api/bluetooth-events"

def get_members():
    members = []
    #r = requests.get(url_get_members)
    getMembers = (urllib2.urlopen(url_get_members).read())

    for person in json.loads(getMembers):
        members.append(Person(  person['id'],
                                person['name'].encode('utf-8'),
                                person['bluetooth_address'],
                                person['color'],
                                person['room']))
    return members

def post_presence(person):
    eventtype = "PERSON_ENTERED" if person.isPresent() else "PERSON_LEFT";
    r = requests.post(url_post_presence, data={"type": eventtype, "subject":person.name})
    # Should add some check if r.status_code is 200 and so on.
