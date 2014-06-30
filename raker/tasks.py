# coding: utf-8
#
# Copyright (c) 2014 Tirith
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Jun 29, 2014, 15:00 PM
#
import os
import sys
from celery import Celery

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from raker.scraper import Facebook, Twitter
from raker import mongo
from raker.models import *
sys.path.pop(0)

app = Celery('tasks', broker='amqp://')


@app.task(ignore_result=True)
def scrap_profile(p_type, profile):
    print 'Processing profile %s' % profile

    if p_type == 'f':
        scrap = Facebook()
    elif p_type == 't':
        scrap = Twitter()

    scrap.connection()
    scrap.grab_user(profile)

    if scrap.profile['nm']:
        p = Profile(
            nm=scrap.profile['nm'],
            im=scrap.profile['im'],
            dc=scrap.profile['dc'],
            pi=scrap.profile['pi'],
            fr=scrap.profile['fr'],
            pr=scrap.profile['pr']
        )
        p.save()
