from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

'''
Architecture:  how do we make hierarchical conversation? For example:
    I want to order a product?
	bot: Which product?
	A router
	bot: which router?
	829.
	bot: Sure. Consider it done. Here is your confirmation number
'''

class ActionOrderProduct(Action):
	def name(self):
		return 'action_order_product'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		router = tracker.get_slot('router')
		confirmationNumber = 123456 #later generate through some process

		response = f"""Your product {router} is ordered for you. It will be shipped to your address. Your confirmation number is {confirmationNumber}"""

		dispatcher.utter_message(response)
		return [SlotSet('router',router)]


class ActionInfoSearch(Action):
	def name(self):
		return 'action_info_search'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		info = tracker.get_slot('info')
		confirmationNumber = 123456 #later generate through some process

		response = """Your info is {}  """

		dispatcher.utter_message(response)
		return [SlotSet('info',info)]