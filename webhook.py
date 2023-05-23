from discord_webhook import DiscordEmbed, DiscordWebhook

class Hook:

    def __init__(self):
       
        self.api_url = input("https://discord.com/api/webhooks/918984943001042944/cBQzcwIpNY1HI_FvebA8-eh5CGqx-RpUNxt_8bUFNP0ygzkpX2962kL1X9c574RmEORc") 
        self.webhook = DiscordWebhook(url= self.api_url, username="Store List")
    
    def sendAlert(self, atclink, name, price):
       
        webhook = self.webhook
        embed = DiscordEmbed(title= name, url= atclink, color='03b2f8')
        embed.add_embed_field(name='Price', value= price)
        embed.add_embed_field(name='Add to cart', value= atclink, inline=False)
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
