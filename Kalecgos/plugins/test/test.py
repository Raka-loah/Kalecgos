from Kalecgos.api import *
from Kalecgos.api import _G

def message(Event: Event):
    if Event.event == 'CHAT_MSG_GROUP':
        SendChatMessage(Event.message + ' recv', 'group', Event.group_id)

RegisterEvent(message, 'CHAT_MSG_PRIVATE')
RegisterEvent(message, 'CHAT_MSG_GROUP')

UnregisterEvent(message, 'CHAT_MSG_PRIVATE')

print(_G())