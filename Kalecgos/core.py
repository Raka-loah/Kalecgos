from pubsub import pub
from importlib import import_module
import requests

class Kalecgos:
    __events = [
        'CHAT_MSG_PRIVATE',
        'CHAT_MSG_GROUP',
        'GROUP_INVITE',
        'GROUP_MEMBER_REQUEST',
        'GROUP_MEMBER_ADDED',
        'GROUP_MEMBER_LEAVE',
        'FRIEND_INVITE',
        'SYSTEM_MESSAGE',
    ]

    def __init__(self):
        self.__pub = pub
        self.__plugins = {}
        try:
            self.__cfg = import_module('Kalecgos.config')
        except Exception as e:
            print('[ERROR] Can not read config.py, using defaults...')

    def register_func(self, func, event):
        if event in self.__events:
            self.__pub.subscribe(func, event)
            return True
        return False

    def unregister_func(self, func, event):
        if event in self.__events:
            self.__pub.unsubscribe(func, event)
            return True
        return False

    def register_plugin(self, plugin_name, plugin_toc):
        self.__plugins[plugin_name] = plugin_toc

    def loaded_plugins(self):
        return self.__plugins

    def get_listeners(self):
        _G = {}
        for topic, v in self.__pub.topicsMap.items():
            for listener in v.listeners:
                if listener.getCallable() not in _G:
                    _G[listener.getCallable()] = []
                _G[listener.getCallable()].append(topic)
        return _G

    def fire_event(self, event, data):
        self.__pub.sendMessage(event, Event=data)
        print(f'[INFO] Event "{event}" fired.')

    def send_message(self, channel, reply_payload):
        base_url = getattr(self.__cfg, 'base_url', 'http://127.0.0.1:5700')
        if channel == 'private':
            r = requests.post(f'{base_url}/send_private_msg_rate_limited', json=reply_payload)
        elif channel == 'group':
            r = requests.post(f'{base_url}/send_group_msg_rate_limited', json=reply_payload)
        else:
            return 404
        return r.status_code

Kalec = Kalecgos()

class Kalec_Event:
    def __init__(self):
        self.event= ''
        self.time = 0
        self.sender = {}
        self.self_id = 0
        self.user_id = 0
        self.post_type = ''
        self.message = ''
        self.is_me = False
        self.group_id = 0

    def generate(self, OneBot_json):
        j = OneBot_json
        if j['post_type'] == 'message':
            if j['message_type'] == 'private':
                self.event= 'CHAT_MSG_PRIVATE'
            elif j['message_type'] == 'group':
                self.event = 'CHAT_MSG_GROUP'
                self.group_id = j['group_id']

        self.time = j['time']
        self.self_id = j['self_id']
        self.user_id = j['user_id']

        self.is_me = True if j['self_id'] == j['user_id'] else False

        self.post_type = j['post_type']
        self.message = j['message']
        self.sender = j['sender']

