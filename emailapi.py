import requests

class Email:

	def __init__(self):
		"""
        Constructer that initializes the mailgun email api url"
        """
		self.api_url = "https://api.mailgun.net/v3/sandbox85c8787e2a1c4cd28488c233abd7f613.mailgun.org/messages"
		
	def send_simple_message(self, atclink, name):
		"""
        Creates and sends an email to notify the user with a name and link attached.
        atclink (string) String link to add the item to your cart
        name (string) name of the item
        """
		self.name = name
		self.atclink = atclink
		print(self.name)
		print(self.atclink)
		print(self.api_url)
		return requests.post(
			self.api_url,
			auth=("api", "2059660d66fece76720ff76a4d61b2f5-7005f37e-933641fe"),
			data={"from": "Bestbuy Alert <sandbox85c8787e2a1c4cd28488c233abd7f613.mailgun.org>",
				"to": "User <cs110nicktavor7@gmail.com>",
				"subject": "In Stock Alert!",
				"text": self.name + "is in stock!" + self.atclink})