import discord
from discord.ext import commands
import re
from datetime import datetime,timedelta
import mysql.connector
import api


# initialise the database

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='scalerdb'
)
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                  qualified VARCHAR(255) NOT NULL Default 'no'
                )''')



intents = discord.Intents.all()
intents.typing = False
intents.presences = False

# Initialize the bot with a command prefix (!)
bot = commands.Bot(command_prefix='!',intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


# @bot.command()

# async def Hello(ctx):
#     await ctx.send("Hello,Thanks for testing our bot! developer:PJ")

@bot.event
async def on_message(message):
    # Check if the message sender is the bot itself to prevent infinite loops
    if message.author == bot.user:
        return
    
    msg=message.content.lower()
    day=30
    m=msg.split("\n")
    # print(m[0].split())
    # pattern = r'^!bot completed day-([1-9]|[1-2][0-9]|30)$'

    pattern1 = r'^!bot completed day-$'
    # pattern = r'!bot completed day-(?:[1-9]|[12]\d|30)\b'
    first_line = m[0]
    nfirst_line=first_line[:19]

    nl=first_line.split()[2]
    day_num=nl[4:len(nl)]
    firstline_seg=first_line.split()
    match = re.match(pattern1, nfirst_line)
    print(match)

    post_pattern = r'^social media link: https://(www.linkedin.com|twitter.com)/+'

    start_date = datetime(2023, 10, 3)
    result_date = start_date + timedelta(days=30)
    day_diff = (result_date - start_date).days


    #day control.....
    current_date = datetime.now()
    print(current_date)
    day = (current_date - start_date).days+1
    print(day)

    #end....

    # Use regular expression to match the specified format
    try:
        print(day_diff)
        if match and int(day_num)<=(day_diff) and int(day_num)==day:
            second_line=str(m[1])
            print(second_line)
            if re.match(post_pattern,second_line):
                name=str(message.author)
                print(type(name))

                cursor.execute('UPDATE students SET qualified = %s WHERE name = %s', ('yes', name))
                db.commit()
        
                await message.channel.send(f"Congratulations! you have completed day-{day_num}")
        

        elif day!=int(day_num):
            await message.channel.send(" Please give the right day")

        else:
            await message.channel.send(" Warning! Please check your format.Write as per the instructions.")
    except Exception as e:
        print(e)  
        await message.channel.send(" Warning! Please check your format.Write as per the instructions.")

bot.run(api.api_key)
