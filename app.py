#!/usr/bin/python
# -*- coding: latin-1 -*-

# app.py by Jean-Sébastien St-Pierre STPJ15018206, October 2019
# This is the logic implementation for the basic flask server

from flask import Flask, request, render_template, jsonify
import re, json


app = Flask(__name__)

# Basic default route
@app.route('/', methods = ['GET', 'POST'])
def accueil():
	titre = "Les astres chuchottent à votre oreille!"
	
	# Data processing
	if request.method == 'POST':
		print("beep")
		name = request.form.get('inputName')
		fstName = request.form.get('inputFstName')
		bthDate = request.form.get('inputDOB')
        #Regex server-side validation for alphanumeric-only user input
		# namePattern = "[a-zA-Z0-9- ]+$"
		# bthdatePattern = "^((0|1)\\d{1})/((0|1|2|3)\\d{1})/((19|20)\\d{2})"
		# if not re.match(pattern, answer):
		# 	return render_template('noWay.tpl', titre = "Nooooooo!", message = "Tu m'auras pas comme ça!!  ;)")
		# hashed = hashThisShit(answer, mode)
		# if hashed == secretHash:
		# 	verdict = "correspond"
		# else:
		# 	verdict = "ne correspond pas"
			
		return render_template('index.html', titre = titre, result = name, mode = fstName, verdict = bthDate)
		
	else :
		return render_template('index.html', titre = titre)


@app.route('/horoscope', methods = ['GET', 'POST'])
def horoscope():
	titre = "Écoutez le chant des étoiles"
	
	# Data processing
	if request.method == 'POST':
		name = request.form['inputName']
		fstName = request.form['inputFstName']
		bthDate = request.form['inputDOB']
        #Regex server-side validation for alphanumeric-only user input
		# namePattern = "[a-zA-Z0-9- ]+$"
		# bthdatePattern = "^((0|1)\\d{1})/((0|1|2|3)\\d{1})/((19|20)\\d{2})"
		# if not re.match(pattern, answer):
		# 	return render_template('noWay.tpl', titre = "Nooooooo!", message = "Tu m'auras pas comme ça!!  ;)")
		# hashed = hashThisShit(answer, mode)
		# if hashed == secretHash:
		# 	verdict = "correspond"
		# else:
		# 	verdict = "ne correspond pas"
		#return jsonify(tite = titre, result = request.form['inputName'], mode = request.form['inputFstName'], verdict = request.form['inputDOB'] )
		#test = jsonify(titre = titre, fstName = fstName)
		
		return json.dumps({'titre':titre, 'name':name, 'fstName': fstName, 'bthDate': bthDate})
		
	else :
		return render_template('index.html', titre = "Fuck you all")


# Error 404 management for any invalid GET request
@app.errorhandler(404)
def myErrorHandle(e):
	titre = "Erreur 404!  Page non trouvée!"
	message = "La page " + request.base_url + " n'existe pas!"
	return render_template('page404.tpl', titre = titre, message = message)
	
# Function returning the hashed value of user's input depending on the selected algorithm
def hashThisShit(ans, mode):
	switcher={
		"md5": hashlib.md5(),
		"sha1": hashlib.sha1(),
		"sha224": hashlib.sha224(),
		"sha256": hashlib.sha256(),
		"sha384": hashlib.sha384(),
		"sha512": hashlib.sha512()
	}
	
	hashMode = switcher.get(mode, "Error!!!")
	hashMode.update(ans.encode('utf-8'))
	return hashMode.hexdigest()
	
# App launcher in https mode with SSL keys ID
if __name__ == '__main__':
	app.run(debug=True, ssl_context=('travail3_cert.crt', 'travail3_pv.key'))