#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash

# new imports for creating anti forgery state token
# login_session acts like a dictionary for the user to store info in

from flask import session as login_session

# need to recieve code sent back from the callback method
# IMPORTS FOR THIS STEP
# stores client Id, client secret and other OAuth 2.0 parameters

from oauth2client.client import flow_from_clientsecrets

# if we run into an erryor trying to exchange an authorization code
# for an access token. This catches the error

from oauth2client.client import FlowExchangeError
from flask import make_response
import random
import string
import datetime
import httplib2

# converting in memory python to json (java script object notation)

import json

# apache 2 HTTP library

import requests

engine = create_engine('postgresql://catalog:password@54.160.150.235/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()