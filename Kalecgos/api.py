from Kalecgos.core import Kalec

def RegisterEvent(func, event):
    return Kalec.register_func(func, event)

def SendChatMessage(message, chat_type, target_id):
    """
    Send chat message.

    Parameters:
    message: The message you want to send.
    chat_type: 'private' or 'group'.
    target_id: Id of the receiving group/friend.
    """
    reply_payload = {
        'at_sender': False,
        'reply': '',
    }
    if message != '':
        reply_payload['reply'] = message
        if chat_type == 'private':
            reply_payload['user_id'] = target_id
            return Kalec.send_message(chat_type, reply_payload)
        elif chat_type == 'group':
            reply_payload['group_id'] = target_id
            return Kalec.send_message(chat_type, reply_payload)
    return 404