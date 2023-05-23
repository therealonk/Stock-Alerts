#### CS 110
# Final Exam - Advanced Programming with Python

### [Exam Description](https://docs.google.com/document/d/1FI-WV95nSTK1JMg5j5sKhxcbl46DPVPkBrxC3FMo45g/edit?usp=sharing)

***

_Replace anything surrounded by the `< >` symbols._

## SUMMARY:
Please make sure you have completed the soot survey at:
    [soot.binghamton.edu](https://soot.binghamton.edu)

Please list the urls for the APIs you used:
https://api.mailgun.net/v3/sandbox85c8787e2a1c4cd28488c233abd7f613.mailgun.org/messages
https://discord.com/api/webhooks/
https://api.bestbuy.com/v1/products(sku%20in%20(6360418))?format=json&apiKey=evtrx3mbnq2ewwx5swdt62du


Summary of Program:
    With an api link derived from a specfic BestBuy item sku, this program will end if the item is out of stock, but will send a detailed webhook to the entered webhook address, and to a specific email address.
Most Challenging topic in the course:
    Working with pygame

## KNOWN BUGS AND INCOMPLETE PARTS:
 < For some reason, as soon as I implemented classes and imported the data thrugh initializing these classes, both the email and discord webhook apis failed to run. Both notification systems are taking in the correct values (seen by the print statements showing the data from Bestbuy() is being peroperly transferred), but for some reason that I cannot find in any documentation, the webhook fails to be sent, as with the email. The email notification systmem does not even give me an error code to work with, just does not send. I am using the default python configuration for mailgun with proper values being used, but mailgun fails to send anything. The [1/1] Webhook status code 400: {"embeds": ["0"]} error code has little documentation online, and the only thing I can find is that discord themselves is rejecting the data from my webhook push. Both notifications appeared to work earlier today, with identical configurations. I cannot, for the life of me, find the reason behind these errors.  >

## REFERENCES:
 < https://pypi.org/project/discord-webhook/ >

## MISCELLANEOUS COMMENTS:
 < If you wish to test this program's handling of an out of stock item, in bestbuyapi, find self.api_url and change the 6360418 near the middle of the link to 6470646. 
 -To find/create your webhook, 
 1. Open your DiscordServer Settings and head into the Integrations tab. This can be in any server you own, and you can easily make a new, empty server for this purpose.
 2. Click the "Create Webhook" button to create a new webhook. Changing the name/avatar is not needed for this program, but set the channel to something you want the program to push webhooks to. 
-To access the email I forward the notification to
Log into gmail with this email: cs110nicktavor7@gmail.com Password: bestbuyapi
 >
