# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ClearSciaticaSlot(Action):
    def name(self) -> Text:
        return 'action_clear_sciatica_slot'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        return[SlotSet('sciatica', None)]
    
class ClearCarpalTunnelSlot(Action):
    def name(self) -> Text:
        return 'action_clear_carpal_tunnel_slot'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        return[SlotSet('carpal_tunnel', None)]
    
class ClearRoundLigamentSlot(Action):
    def name(self) -> Text:
        return 'action_clear_round_ligament_slot'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        return[SlotSet('round_ligament', None)]  
    
class ClearTypesTopicSlot(Action):
    def name(self) -> Text:
        return 'action_clear_types_topic_slot'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        return[SlotSet('types_topic', None)]


class ClearInfluenceTopicSlot(Action):
    def name(self) -> Text:
        return 'action_clear_influence_topic_slot'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        return[SlotSet('influence_topic', None)]  
    
class ActionElasticSearch(Action):
    def name(self) -> Text:
        return 'action_elastic_search'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        
        return