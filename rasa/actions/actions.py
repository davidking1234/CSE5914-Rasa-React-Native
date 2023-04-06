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
# !!!!!!!! ELASTIC SEARCH
from datetime import datetime
from elasticsearch import Elasticsearch
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
es = Elasticsearch(hosts="https://localhost:9200", basic_auth=(USER, PASS), verify_certs=False)

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

class ActionElasticSearch(Action):
    def name(self) -> Text:
        return 'action_elastic_search'
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        index_documents()
        link = search_documents('sleep')
        dispatcher.utter_message(text=link)
        return
