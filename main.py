from decouple import config
# PORT = int(os.environ.get('PORT', 5000))
import telebot
from rak import getMenuforDay
API_KEY =config("botKey")
print(API_KEY)
bot = telebot.TeleBot(API_KEY)
import datetime



WeekDaysFrench=['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

 

def specificDay(message):
  if message.text in WeekDaysFrench:
    return True
  return False

@bot.message_handler(commands=['tout'])
def tout(message):
  dayIndex=datetime.datetime.today().weekday()
  dayName=WeekDaysFrench[dayIndex]
  nextDayName=WeekDaysFrench[(dayIndex+1)%7]
  response=getMenuforDay(dayName, nextDayName)
  bot.send_message(message.chat.id, response)

@bot.message_handler(func=specificDay)
def sendSpecificDay(message):
  dayName=message.text
  nextDayName=WeekDaysFrench[WeekDaysFrench.index(message.text)+1]
  response=getMenuforDay(dayName, nextDayName)
  bot.send_message(message.chat.id, response)


# bot.start_webhook(listen="0.0.0.0",
#                           port=int(PORT),
#                           url_path=TOKEN)

bot.polling()
# bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)