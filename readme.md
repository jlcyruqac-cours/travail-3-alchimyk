README.MD

By Jean-Sébastien St-Pierre
2019/10/11

PREREQUISITES:

- Python 3.x must be installed on the machine
- Tested with Windows 10 build 1803

RUNNING INSTRUCTIONS:

- Open a Powershell/Bash command shell
- At root level, clone the Git repo with "git clone [theRepoURL]"
- Navigate to folder "travail-3-alchimyk"
- Install the Python virtual environment:
	- Type "python -m venv ."
	- Activate the virtual environment:
		- UNIX-BASED OS: Type \bin\activate and press Enter
		- WINDOWS USERS: Type .\Scripts\activate and press Enter
- Install all the dependancies by typing the following command: "pip install -r requirements.txt"
- Download the appropriate Nginx version for your OS and extract TO THE ROOT! (very important if you want to live your life as God 	intended it)
- From root/travail-3-alchimyk/nginx, copy the 2 folders (conf + static) to the new root/nginx folder, replacing actual files
- Type "python app.py" and press Enter to start the Flask server
- From a new shell, go to root/nginx and type "start nginx", then hit Enter

The app will be available at https://localhost:8080 via your favorite internet browser

Don't screw your future by sticking to whatever-the-fuck your horoscope says, we all know it's bullshit.

** Please donate to our charity!  We accept all Interac, Visa, Mastercard and Paypal electronic money transfer! **
** NEW!!! ** We now accept Bitcoins (100 is the minimum).  Please EMT to 581-882-5150.  Simple, easy and secure! **


	
