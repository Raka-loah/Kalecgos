from Kalecgos.core import Kalec, Kalec_Event
from importlib import import_module
from quart import Quart, request, jsonify
import os
import logging

app = Quart(__name__)

def load():
    plugins = [ f.name for f in os.scandir(os.path.join(os.path.dirname(os.path.abspath(__file__)) ,'plugins')) if f.is_dir() ]

    for plugin in plugins:
        try:
            print(f'[INFO] Loading plugin "Kalecgos.plugins.{plugin}"...')
            module = import_module(f'Kalecgos.plugins.{plugin}')
            Kalec.register_plugin(f'Kalecgos.plugins.{plugin}', module.TOC)
        except Exception as e:
            print(f'[ERROR] Module {plugin}: {e}.')

@app.route('/', methods=['POST'])
async def post():
    try:
        # POSTed data as json
        j = await request.get_json(force=True)

        nickname = j['sender'].get('card', j['sender'].get('nickname', '')) if 'sender' in j else '#NAME?'
        
        app.logger.setLevel(logging.INFO)
        app.logger.info(f"[{j.get('message_type', 'UNKNOWN').upper()}][{j.get('group_id','--')}][{nickname}({j['sender'].get('user_id', '')})]:{j['message']}")

        event = Kalec_Event()
        event.generate(j)

        Kalec.fire_event(event.event, event)

        return '', 204

    except Exception as e:
        app.logger.error(f"[ERROR] {e}")
        return '', 204

def run():
    load()
    app.run(port=8888, debug=False)