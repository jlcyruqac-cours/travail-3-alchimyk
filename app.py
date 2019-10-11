#!/usr/bin/python
# -*- coding: latin-1 -*-

# app.py by Jean-Sébastien St-Pierre STPJ15018206, October 2019
# This is the logic implementation for the basic flask server

from flask import Flask, request, render_template, jsonify
import re, json, datetime
from datetime import *
import requests


app = Flask(__name__)

# Basic default route
@app.route('/', methods = ['GET'])
def accueil():
	titre = "Les astres chuchottent à votre oreille!"	
	return render_template('index.html', titre = titre)
	

@app.route('/horoscope', methods = ['GET', 'POST'])
def horoscope():
	
	# Data processing
	if request.method == 'POST':
		name = request.form['inputName']
		fstName = request.form['inputFstName']
		bthDate = request.form['inputDOB']
		validated = (validateInput(name, fstName, bthDate))
		mysign = getSign(bthDate)
		requestHoroscope = getAztro(mysign)
		myHoroscope = format(requestHoroscope.json()["description"])
		
		return json.dumps({'name':name, 'fstName': fstName, 'bthDate': bthDate,
		 'ErrorCodes': validated, 'sign': mysign, 'horoscope': myHoroscope})
		
	else :
		return render_template('index.html', titre = titre)


def validateInput(name, fname, bdate):
	#Regex server-side validation for alphanumeric-only user input
	namePattern = "[a-zA-Z- ]+$"
	bdatePattern = "^((0|1)\\d{1})/((0|1|2|3)\\d{1})/((19|20)\\d{2})"
	validationError = []

	if not name:
		validationError.append("Le champ 'nom' est vide!\n")
	else:
		if not re.match(namePattern, name):
			validationError.append(name + " est un nom invalide!\n")

	if not fname:
		validationError.append("Le champ 'prénom' est vide!\n")
	else:
		if not re.match(namePattern, fname):
			validationError.append(fname + " est un nom invalide!\n")

	if not bdate:
		validationError.append("Le champ 'date de naissance' est vide!\n")
	else:
		m, d, y = bdate.split('/')
		dateObj = date(int(y), int(m), int(d))
		if dateObj > date.today():
			validationError.append("Vous ne pouvez pas être né dans le futur\n")

		elif not re.match(bdatePattern, bdate):
			validationError.append(bdate + " est une date de naissance invalide!\n")

	return validationError

def getSign(date):
	month, d, y = date.split('/')
	day = int(d)
	if month == '12': 
		astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'

	elif month == '01': 
		astro_sign = 'Capricorn' if (day < 20) else 'aquarius'

	elif month == '02': 
		astro_sign = 'Aquarius' if (day < 19) else 'pisces'

	elif month == '03': 
		astro_sign = 'Pisces' if (day < 21) else 'aries'

	elif month == '04': 
		astro_sign = 'Aries' if (day < 20) else 'taurus'

	elif month == '05': 
		astro_sign = 'Taurus' if (day < 21) else 'gemini'

	elif month == '06': 
		astro_sign = 'Gemini' if (day < 21) else 'cancer'

	elif month == '07': 
		astro_sign = 'Cancer' if (day < 23) else 'leo'

	elif month == '08': 
		astro_sign = 'Leo' if (day < 23) else 'virgo'

	elif month == '09': 
		astro_sign = 'Virgo' if (day < 23) else 'libra'

	elif month == '10': 
		astro_sign = 'Libra' if (day < 23) else 'scorpio'

	elif month == '11': 
		astro_sign = 'scorpio' if (day < 22) else 'sagittarius'

	return astro_sign

def getAztro(asign):
	params = (
		('sign', asign),
		('day', 'today'),
		)

	return requests.post('https://aztro.sameerkumar.website/', params=params)

# Error 404 management for any invalid GET request
@app.errorhandler(404)
def myErrorHandle(e):
	titre = "Erreur 404!  Page non trouvée!"
	message = "La page " + request.base_url + " n'existe pas!"
	return render_template('page404.tpl', titre = titre, message = message)
	
	
# App launcher in https mode with SSL keys ID
if __name__ == '__main__':
	#app.run(debug=True, ssl_context=('travail3_cert.crt', 'travail3_pv.key'))
	app.run(debug=True)