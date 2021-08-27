
import discord

from gsheet import *

client = discord.Client()
sheet = gsheet()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Restrict the command to a role
    # Change REQUIREDROLE to a role id or None
    REQUIREDROLE = None
    if REQUIREDROLE is not None and discord.utils.get(message.author.roles, id=str(REQUIREDROLE)) is None:
        await message.channel.send('You don\'t have the required role!')
        return

    # Command to insert attack data to excel
    if message.content.startswith('!attack '):
        SPREADSHEET_ID = '1CDRbzv1gAgRGqxgGI3mg70m3FuJMMc5u4yAnAbnJjA4' # Add ID here
        RANGE_NAME = 'Log!A1'
        FIELDS = 1 # Amount of fields/cells

        # Code
        msg = message.content[8:]
        result = int(msg)

        print(message.created_at)
        DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + [result] + [str('Attacks')]
        sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
        await message.channel.send('Your data has been successfully submitted!')


    # Command to insert first break data to excel
    if message.content.startswith('!first'):
        SPREADSHEET_ID = '1CDRbzv1gAgRGqxgGI3mg70m3FuJMMc5u4yAnAbnJjA4' # Add ID here
        RANGE_NAME = 'Log!A1'
        FIELDS = 1 # Amount of fields/cells

        # Code
        msg = message.content[7:]
        result = int('1')

        print(message.created_at)
        DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + [result] + [str('First break')]
        sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
        await message.channel.send('Your data has been successfully submitted!')


    # Command to insert missile data to excel
    if message.content.startswith('!missile '):
        SPREADSHEET_ID = '1CDRbzv1gAgRGqxgGI3mg70m3FuJMMc5u4yAnAbnJjA4' # Add ID here
        RANGE_NAME = 'Log!A1'
        FIELDS = 1 # Amount of fields/cells

        # Code
        msg = message.content[9:]
        result = int(msg)

        print(message.created_at)
        DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + [result] + [str('Missiles')]
        sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
        await message.channel.send('Your data has been successfully submitted!')


    # Command to insert probe data to excel
    if message.content.startswith('!probe '):
        SPREADSHEET_ID = '1CDRbzv1gAgRGqxgGI3mg70m3FuJMMc5u4yAnAbnJjA4' # Add ID here
        RANGE_NAME = 'Log!A1'
        FIELDS = 1 # Amount of fields/cells

        # Code
        msg = message.content[7:]
        result = int(msg)

        print(message.created_at)
        DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + [result] + [str('Probes')]
        sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
        await message.channel.send('Your data has been successfully submitted!')



    # Command to send the spreadsheet link
    if message.content.startswith('!hof sheet'):
        await message.channel.send('https://docs.google.com/spreadsheets/d/1CDRbzv1gAgRGqxgGI3mg70m3FuJMMc5u4yAnAbnJjA4/edit?usp=sharing')

    if message.content.startswith('!hof help'):
        await message.channel.send('Use \"**!attack** \", \"**!missile** \", or \"**!probe** \" followed by the number of attacks/missiles/probes you\'d like to log. For example, \"**!attack 1**\" would add 1 attack to your total. \"**!hof sheet**\" will respond with the link to the HoF totals.')


client.run('ODc2NTg4MDQ5OTk4NDIyMDM2.YRmQPQ.AsXOyJylIjVY0bMOR10qe7Du7FM') # Add bot token here