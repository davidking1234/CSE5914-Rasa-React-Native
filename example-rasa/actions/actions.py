# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import FormValidation, SlotSet, Restarted
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import datetime
#from elasticsearch import Elasticsearch



MOCK_CHECKBOX = json.load(
    open("actions/schemas/checkbox.json", "r")
)
dict_list = [{'tag': ['sids', 'sleep', 'crib', 'babys', 'baby'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/alone-back-crib/'}, 
             {'tag': ['stepone', 'pregnancy', 'parenting', 'bump', 'resources'], 'link': 'https://www.columbus.gov/celebrate-one/'}, 
             {'tag': ['ohiohealth', 'columbus', 'mortality', 'infant', 'optum'], 'link': 'https://www.columbus.gov/celebrate-one/About-CelebrateOne/'}, 
             {'tag': ['prenatal', 'postpartum', 'pregnancy', 'progesterone', 'medicaid'], 'link': 'https://www.columbus.gov/celebrate-one/Pregnant-Women/'}, 
             {'tag': ['breastfeeding', 'moms', 'baby', 'cribs', 'breastfeed'], 'link': 'https://www.columbus.gov/celebrate-one/New-Mothers/'}, 
             {'tag': ['sleep', 'safe', 'abcs', 'tips', 'babies'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/safe-sleep-home/'}, 
             {'tag': ['cribs', 'sleep', 'safe', 'baby', 'kids'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/comforting-your-baby/'}, 
             {'tag': ['sids', 'grandbaby', 'baby', 'sleep', 'rebreathing'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/tips-for-your-baby/'}, 
             {'tag': ['abcs', 'sleep', 'preventable', 'baby', 'safe'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/sweet-dreams-team/'}, 
             {'tag': ['columbus', '3111', 'workloads', 'assistance', 'service'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/columbus-service-center/'}, 
             {'tag': ['sleep', 'caregivers', 'abuelos', 'bebé', 'grandparents'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/education-links/'}, 
             {'tag': ['sleep', 'safe', 'columbus', 'infant', 'moms'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/safe-sleep-ambassador-training-events/'}, 
             {'tag': ['dorans', 'eventbrite', 'shayla', 'bankston', 'ginther'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/become-a-safe-sleep-ambassador-contact-form/'}, 
             {'tag': ['cribs', 'sleep', 'kids', 'safe', 'crib'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/become-a-safe-sleep-partner/'}, 
             {'tag': ['sleep', 'babies', 'safe', 'infant', 'crib'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/history-of-safe-sleep/'}, 
             {'tag': ['crib', 'dorans', 'grandmas', 'shayla', 'bankston'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/campaign-materials/'}, 
             {'tag': ['iud', 'reversible', 'teen', 'implant', 'pregnancy'], 'link': 'https://www.columbus.gov/celebrate-one/Women-and-Teens/'}, 
             {'tag': ['toolkit', 'fathers', 'infant', 'vitality', 'modules'], 'link': 'https://www.columbus.gov/celebrate-one/Infant-Vitality-Toolkit/Home/'}, 
             {'tag': ['moms', 'franklinton', 'profile', 'map', 'neighborhoods'], 'link': 'https://www.columbus.gov/celebrate-one/Neighborhoods/'}, 
             {'tag': ['5x11', 'sleep', 'moms', 'chw', 'columbus'], 'link': 'https://www.columbus.gov/celebrate-one/Help-Us-Take-Action/'}, 
             {'tag': ['caresource', 'fiorile', 'borror', 'ohiohealth', 'foundation'], 'link': 'https://www.columbus.gov/celebrate-one/Give-to-CelebrateOne/'}, 
             {'tag': ['email', 'protected', 'kurtek', 'desamours', '43205'], 'link': 'https://www.columbus.gov/celebrate-one/Contact-Us/'}, 
             {'tag': ['sleep', 'infant', 'crib', 'safe', 'eventbrite'], 'link': 'https://www.columbus.gov/celebrate-one/safe-sleep/request-a-crib/'}, 
             {'tag': ['bump', 'baby', 'mom', '3322', 'pregnancy'], 'link': 'https://www.columbus.gov/celebrate-one/baby-bump-beyond/'}, 
             {'tag': ['2022', '2023', 'newsletter', 'infant', 'babies'], 'link': 'https://columbus.gov/celebrate-one/newsletters/ '}, 
             {'tag': ['32768', 'trimbox', '065', 'xobject', 'obj'], 'link': 'https://www.columbus.gov/celebrate-one/2021-C1-annual-report/'}, 
             {'tag': ['trimbox', 'xobject', 'obj', '1008', 'pdf'], 'link': 'https://www.columbus.gov/celebrate-one/Healthy-Beginnings-At-Home-Policy-Brief/'}, 
             {'tag': ['stepone', 'prenatal', '0009', 'healthy', 'pregnancy'], 'link': 'https://www.columbus.gov/celebrate-one/StepOne-for-a-Healthy-Pregnancy/'},
             {'tag': ['stepone', 'pregnancy', 'parenting', 'bump', 'resources'], 'link': 'https://columbus.gov/celebrate-one/'}, 
             {'tag': ['ohiohealth', 'columbus', 'mortality', 'infant', 'optum'], 'link': 'https://columbus.gov/celebrate-one/About-CelebrateOne/'}, 
             {'tag': ['prenatal', 'postpartum', 'pregnancy', 'progesterone', 'medicaid'], 'link': 'https://columbus.gov/celebrate-one/Pregnant-Women/'}, 
             {'tag': ['breastfeeding', 'moms', 'baby', 'cribs', 'breastfeed'], 'link': 'https://columbus.gov/celebrate-one/New-Mothers/'}, 
             {'tag': ['sleep', 'safe', 'abcs', 'tips', 'babies'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/safe-sleep-home/'}, 
             {'tag': ['sids', 'sleep', 'crib', 'babys', 'baby'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/alone-back-crib/'}, 
             {'tag': ['cribs', 'sleep', 'safe', 'baby', 'kids'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/comforting-your-baby/'}, 
             {'tag': ['sids', 'grandbaby', 'baby', 'sleep', 'rebreathing'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/tips-for-your-baby/'}, 
             {'tag': ['abcs', 'sleep', 'preventable', 'baby', 'safe'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/sweet-dreams-team/'}, 
             {'tag': ['columbus', '3111', 'workloads', 'assistance', 'service'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/columbus-service-center/'}, 
             {'tag': ['sleep', 'caregivers', 'abuelos', 'bebé', 'grandparents'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/education-links/'}, 
             {'tag': ['sleep', 'safe', 'columbus', 'infant', 'moms'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/safe-sleep-ambassador-training-events/'}, 
             {'tag': ['dorans', 'eventbrite', 'shayla', 'bankston', 'ginther'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/become-a-safe-sleep-ambassador-contact-form/'}, 
             {'tag': ['cribs', 'sleep', 'kids', 'safe', 'crib'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/become-a-safe-sleep-partner/'}, 
             {'tag': ['sleep', 'babies', 'safe', 'infant', 'crib'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/history-of-safe-sleep/'}, 
             {'tag': ['crib', 'dorans', 'grandmas', 'shayla', 'bankston'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/campaign-materials/'}, 
             {'tag': ['iud', 'reversible', 'teen', 'implant', 'pregnancy'], 'link': 'https://columbus.gov/celebrate-one/Women-and-Teens/'}, 
             {'tag': ['toolkit', 'fathers', 'infant', 'vitality', 'modules'], 'link': 'https://columbus.gov/celebrate-one/Infant-Vitality-Toolkit/Home/'}, 
             {'tag': ['moms', 'franklinton', 'profile', 'map', 'neighborhoods'], 'link': 'https://columbus.gov/celebrate-one/Neighborhoods/'}, 
             {'tag': ['5x11', 'sleep', 'moms', 'chw', 'columbus'], 'link': 'https://columbus.gov/celebrate-one/Help-Us-Take-Action/'}, 
             {'tag': ['caresource', 'fiorile', 'borror', 'ohiohealth', 'foundation'], 'link': 'https://columbus.gov/celebrate-one/Give-to-CelebrateOne/'}, 
             {'tag': ['email', 'protected', 'kurtek', 'desamours', '43205'], 'link': 'https://columbus.gov/celebrate-one/Contact-Us/'}, 
             {'tag': ['bump', 'baby', 'mom', '3322', 'pregnancy'], 'link': 'https://columbus.gov/celebrate-one/baby-bump-beyond/'}, 
             {'tag': ['32768', 'trimbox', '065', 'xobject', 'obj'], 'link': 'https://columbus.gov/celebrate-one/2021-C1-annual-report/'}, 
             {'tag': ['trimbox', 'xobject', 'obj', '1008', 'pdf'], 'link': 'https://columbus.gov/celebrate-one/Healthy-Beginnings-At-Home-Policy-Brief/'}, 
             {'tag': ['file', 'servers', 'columbus', 'twitter', 'facebook'], 'link': 'https://www.columbus.gov/celebrate-one/Rides4Baby/'}, 
             {'tag': ['stepone', 'prenatal', '0009', 'healthy', 'pregnancy'], 'link': 'https://columbus.gov/celebrate-one/StepOne-for-a-Healthy-Pregnancy/'}, 
             {'tag': ['sleep', 'infant', 'crib', 'safe', 'eventbrite'], 'link': 'https://columbus.gov/celebrate-one/safe-sleep/request-a-crib/'}, 
             {'tag': ['file', 'servers', 'columbus', 'twitter', 'facebook'], 'link': 'https://columbus.gov/celebrate-one/Rides4Baby/'}]

# es = Elasticsearch('https://localhost:9200')
USER = 'elastic'
PASS = 'PASSWORD'
#es = Elasticsearch(hosts="https://localhost:9200", basic_auth=(USER, PASS), verify_certs=False)

# Updating Index
def index_documents():
    id = 1
    for doc in dict_list:
        resp = es.index(index="test-index", id=id, document=doc)
        # print(resp['result'])
        id += 1

# Getting Results
def search_documents(term):
    resp = es.search(index="test-index", query={"match": {"tag":term}})
    # print("Got %d Hits:" % resp['hits']['total']['value'])
    num_results = resp['hits']['total']['value']
    if num_results > 10:
        num_results = 10
    
    if num_results == 0:
        print("No results for this keyword.")
    else:
        print("Here are %d relevant links:" % num_results)
        for hit in resp['hits']['hits']:
            x = hit["_source"]
            print(x['link'])
            return x['link']

# !!!!! END ELASTIC SEARCH
class ActionElasticSearch(Action):
    def name(self) -> Text:
        return 'action_elastic_search'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        #index_documents()
        print("ES CALLED")
        msg = tracker.latest_message['text']

        search_term = msg.remove("es")
        print("message: ", msg, "dict: ", tracker.latest_message)
        #link = search_documents('sleep')
        #dispatcher.utter_message(text=link)
        return



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
    
class ClearBackPainSlot(Action):
    def name(self) -> Text:
        return 'action_clear_back_pain_slot'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        return[SlotSet('back_pain', None)]  
    
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
    

class UtterTypes(Action):
    def name(self) -> Text:
        return 'action_types'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        influence = tracker.get_slot('influence_topic')

        print("UTTER TYPES types: ",types, "influence: ", influence)
        #if(types is not None and influence is None):
        dispatcher.utter_message(response = "utter_body_aches_types")


        return None  
    
class UtterInfluences(Action):
    def name(self) -> Text:
        return 'action_influence'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')

        influence = tracker.get_slot('influence_topic')
        print("UTTER INFLUENCE influence: ",influence, "types: ", types)
        #if(influence is not None and types is None):
        dispatcher.utter_message(response = "utter_body_aches_influence_types")

        return None  
    
class SciaticaDefinition(Action):
    def name(self) -> Text:
        return 'action_sciatica_types'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        influence = tracker.get_slot('influence_topic')
        sciatica = tracker.get_slot('sciatica')
        carpal_tunnel = tracker.get_slot('carpal_tunnel')
        round_ligament = tracker.get_slot('round_ligament')
        back_pain = tracker.get_slot('back_pain')

        print("SCIATICA_DEF: types: ",types,"influence: ", influence, "sciatica: ", sciatica, "carpal_tunnel: ", carpal_tunnel, "round_ligament: ", round_ligament, "back_pain: ", back_pain)
        #if (types is not None and sciatica is not None and carpal_tunnel is None and influence is None):
        dispatcher.utter_message(response = "utter_body_aches_sciatica_definition")
        
       
        return None
    
class CarpalTunnelDefinition(Action):
    def name(self) -> Text:
        return 'action_carpal_tunnel_types'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        influence = tracker.get_slot('influence_topic')
        sciatica = tracker.get_slot('sciatica')
        carpal_tunnel = tracker.get_slot('carpal_tunnel')
        round_ligament = tracker.get_slot('round_ligament')
        back_pain = tracker.get_slot('back_pain')

        print("CARPAL_TUNNEL_DEF: types: ",types,"influence: ", influence, "sciatica: ", sciatica, "carpal_tunnel: ", carpal_tunnel, "round_ligament: ", round_ligament, "back_pain: ", back_pain)

        #if (types is not None and carpal_tunnel is not None and influence is None and sciatica is None):
        dispatcher.utter_message(response = "utter_body_aches_carpal_tunnel_definition")
       

        return None
    
class RoundLigamentDefinition(Action):
    def name(self) -> Text:
        return 'action_round_ligament_types'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        influence = tracker.get_slot('influence_topic')
        sciatica = tracker.get_slot('sciatica')
        carpal_tunnel = tracker.get_slot('carpal_tunnel')
        round_ligament = tracker.get_slot('round_ligament')
        back_pain = tracker.get_slot('back_pain')

        print("ROUND_LIGAMENT_DEF: types: ",types,"influence: ", influence, "sciatica: ", sciatica, "carpal_tunnel: ", carpal_tunnel, "round_ligament: ", round_ligament, "back_pain: ", back_pain)
        #if (types is not None and carpal_tunnel is not None and influence is None and sciatica is None):
        dispatcher.utter_message(response = "utter_body_aches_round_ligament_definition")
        

        return None
    
class BackPainDefinition(Action):
    def name(self) -> Text:
        return 'action_back_pain_types'
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        sciatica = tracker.get_slot('sciatica')
        influence = tracker.get_slot('influence_topic')
        carpal_tunnel = tracker.get_slot('carpal_tunnel')
        round_ligament = tracker.get_slot('round_ligament')
        back_pain = tracker.get_slot('back_pain')


        print("BACK_PAIN_DEF: types: ",types,"influence: ", influence, "sciatica: ", sciatica, "carpal_tunnel: ", carpal_tunnel, "round ligament: ", round_ligament, "back pain: ", back_pain)

        #if (types is not None and carpal_tunnel is not None and influence is None and sciatica is None):
        dispatcher.utter_message(response = "utter_body_aches_back_pain_definition")
        
        return None
    
class SciaticaInfluence(Action):
    def name(self) -> Text:
        return 'action_sciatica_influence'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        influence = tracker.get_slot('influence_topic')
        sciatica = tracker.get_slot('sciatica')
        carpal_tunnel = tracker.get_slot('carpal_tunnel')
        round_ligament = tracker.get_slot('round_ligament')
        back_pain = tracker.get_slot('back_pain')

        print("SCIATICA_INFLUENCE: types: ",types,"influence: ", influence, "sciatica: ", sciatica, "carpal_tunnel: ", carpal_tunnel, "round_ligament: ", round_ligament, "back_pain: ", back_pain)
        #if (types is not None and sciatica is not None and carpal_tunnel is None and influence is None):
        dispatcher.utter_message(response = "utter_body_aches_influencing_factors_sciatica")
        
       
        return None
    
class CarpalTunnelInfluence(Action):
    def name(self) -> Text:
        return 'action_carpal_tunnel_influence'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        influence = tracker.get_slot('influence_topic')
        sciatica = tracker.get_slot('sciatica')
        carpal_tunnel = tracker.get_slot('carpal_tunnel')
        round_ligament = tracker.get_slot('round_ligament')
        back_pain = tracker.get_slot('back_pain')

        print("CARPAL_TUNNEL_INFLUENCE: types: ",types,"influence: ", influence, "sciatica: ", sciatica, "carpal_tunnel: ", carpal_tunnel, "round_ligament: ", round_ligament, "back_pain: ", back_pain)

        #if (types is None and carpal_tunnel is not None and influence is not None and sciatica is None):
        dispatcher.utter_message(response = "utter_body_aches_influencing_factors_carpal_tunnel")
           
        return None
    
class RoundLigamentInfluence(Action):
    def name(self) -> Text:
        return 'action_round_ligament_influence'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        influence = tracker.get_slot('influence_topic')
        sciatica = tracker.get_slot('sciatica')
        carpal_tunnel = tracker.get_slot('carpal_tunnel')
        round_ligament = tracker.get_slot('round_ligament')
        back_pain = tracker.get_slot('back_pain')

        print("ROUND_LIGAMENT_ INFLUENCE: types: ",types,"influence: ", influence, "sciatica: ", sciatica, "carpal_tunnel: ", carpal_tunnel, "round_ligament: ", round_ligament, "back_pain: ", back_pain)
        
        #if (types is None and carpal_tunnel is None and influence is not None and sciatica is None and round_ligament is not None):
        dispatcher.utter_message(response = "utter_body_aches_influencing_factors_round_ligament")
           
        return None
    

class BackPainInfluence(Action):
    def name(self) -> Text:
        return 'action_back_pain_influence'
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        types = tracker.get_slot('types_topic')
        sciatica = tracker.get_slot('sciatica')
        influence = tracker.get_slot('influence_topic')
        carpal_tunnel = tracker.get_slot('carpal_tunnel')
        round_ligament = tracker.get_slot('round_ligament')
        back_pain = tracker.get_slot('back_pain')


        print("BACK_PAIN_INFLUENCE: types: ",types,"influence: ", influence, "sciatica: ", sciatica, "carpal_tunnel: ", carpal_tunnel, "round_ligament: ", round_ligament, "back pain: ", back_pain)

        #if (types is not None and carpal_tunnel is not None and influence is None and sciatica is None):
        dispatcher.utter_message(response = "utter_body_aches_influencing_factors_back_pain")
        
        return None
    
class ActionElasticSearch(Action):
    def name(self) -> Text:
        return 'action_elastic_search'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        
        return


class ActionRestart(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_restart"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response='utter_restart')

        return [Restarted()]

class ActionAskShowCheckboxFormFoodList(Action):
    """Action Ask Show Checkbox Form Food List."""

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "action_ask_show_checkbox_form_food_list"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(
            text='Which food do you eat more?',
            json_message=MOCK_CHECKBOX,
        )
        return []

class ActionShowButtons(Action):
    """Show Buttons."""

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "action_show_buttons"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        buttons = []
        buttons.extend([
            {"title": 'Yes', "payload": "/affirm{}".format(json.dumps({"response_validation": True}))},
            {"title": 'No', "payload": "/deny{}".format(json.dumps({"response_validation": False}))},
        ])
        dispatcher.utter_message(
            text='Is it correct?',
            buttons=buttons,
        )

        return []

class ActionShowVideo(Action):
    """Show Video."""

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "action_show_video"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        video = {
            "type": "video",
            "url": "http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4"
        }

        dispatcher.utter_message(
            text='Here is something to cheer you up',
            json_message=video            
        )

        return []


class ActionShowSummary(Action):
    """Show Summary."""

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "action_show_summary"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        slots = ["food_list"]
        food_list = tracker.get_slot(slots[0])

        variables = {
            "OPTIONS": food_list,
        }
        dispatcher.utter_message(response='utter_summary', **variables)
        
        return [SlotSet(slot, None) for slot in slots]