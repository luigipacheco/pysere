import os
import sys
import fileinput

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.config import Config

Config.set('graphics','width','500')
Config.set('graphics','height','200')



	
class AccountDetailsForm(BoxLayout):
	
	def searchreplace(self):
		search_box = ObjectProperty()
		replace_box= ObjectProperty()
		dir_box = ObjectProperty()
		
		print ("Text to search for:" + self.search_box.text)
		textToSearch = self.search_box.text

		print ("Text to replace it with:" + self.replace_box.text)
		textToReplace = self.replace_box.text

		print ("File to perform Search-Replace on:" + self.dir_box.text)
		fileToSearch  = self.dir_box.text
		#fileToSearch = 'D:\dummy1.txt'
		
		tempFile = open( fileToSearch, 'r+' )
		for line in fileinput.input( fileToSearch ):
			if textToSearch in line :
				print('Match Found')
			else:
				print('Match Not Found!!')
			tempFile.write( line.replace( textToSearch, textToReplace ) )
		tempFile.close()
		
		

		print("You just clicked the button!!")
		print("Text Changed!!")
	
	
class pysere(App):
	pass
	
	
pysere().run()
