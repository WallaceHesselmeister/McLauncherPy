#!/usr/bin/env python3
# This example shows how to simple install and launch the latest version of Minecraft.
import minecraft_launcher_lib
import subprocess
import sys


import tkinter as tk # Python 3 import
# import Tkinter as tk # Python 2 import


root = tk.Tk()

def my_function():
	minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
	# Get Minecraft directory
	latest = minecraft_launcher_lib.utils.get_latest_version()["release"]
	#get token on minecraft.net: console.log(`; ${document.cookie}`.split('; bearer_token=').pop().split(';').shift())
	# Set the data for your Azure Application here. For more information look at the documentation.
	CLIENT_ID = "YOUR CLIENT ID"
	REDIRECT_URL = "YOUR REDIRECT URL"
		
	
	current_id = my_entry.get()
	if current_id == "":
		version = latest
	else:
		version = current_id
	print(version)
	#do stuff with url_member
	print(version)

	
	# Make sure, the version of Minecraft is installed
	minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)
	
	# Login
	#login_url, state, code_verifier = minecraft_launcher_lib.microsoft_account.get_secure_login_data(CLIENT_ID, REDIRECT_URL)
	#print(f"Please open {login_url} in your browser and copy the url you are redirected into the prompt below.")
	#code_url = input()
	
	# Get the code from the url
	#try:
	#    auth_code = minecraft_launcher_lib.microsoft_account.parse_auth_code_url(code_url, state)
	#except AssertionError:
	#    print("States do not match!")
	#    sys.exit(1)
	#except KeyError:
	#    print("Url not valid")
	#    sys.exit(1)
	
	# Get the login data	
	#login_data = minecraft_launcher_lib.microsoft_account.complete_login(CLIENT_ID, None, REDIRECT_URL, auth_code, code_verifier)
	
	# Get Minecraft command
	options = {
	    "username": "Player",
	    "uuid": "",
	    "token": ""
	}
	minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
	# Start Minecraft
	subprocess.run(minecraft_command)












minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
print(minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory))
my_label = tk.Label(root, text = "Version: (Leave blank for latest) ")
my_label.grid(row = 0, column = 0)
my_entry = tk.Entry(root)
my_entry.grid(row = 0, column = 1)

my_button = tk.Button(root, text = "Submit", command = my_function)
my_button.grid(row = 1, column = 1)

root.mainloop()




