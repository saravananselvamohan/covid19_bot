# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import requests, json 



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCoronaCases(Action):

     def name(self) -> Text:
         return "action_corona_cases"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
         a = get_corona_cases() 

         dispatcher.utter_message(text=a)

         return []
         

def get_corona_cases():

	complete_url = 'https://covid-19india-api.herokuapp.com/v2.0/country_data'
	response = requests.get(complete_url) 
	x = response.json()
	y = x[1]
	output = "Active Cases =" + str(y["active_cases"])+"\nConfirmed Cases = " + str(y["confirmed_cases"]) + "\nDeath Cases = " +str(y["death_cases"])+"\nLast Updated = "+str(y["last_updated"])

      

	return output
