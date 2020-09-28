from Kalecgos.api import *

def message(Event):
    if Event.event == 'CHAT_MSG_GROUP':
        SendChatMessage(Event.message + ' recv', 'group', Event.group_id)

RegisterEvent(message, 'CHAT_MSG_PRIVATE')
RegisterEvent(message, 'CHAT_MSG_GROUP')