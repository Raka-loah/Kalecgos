from quart import Quart, request

app = Quart(__name__)

@app.route("/<path:text>", methods=['POST'])
async def main(text):
    content = await request.get_json(force=True)
    print(content)
    return '', 200

if __name__ == '__main__':
    app.run(port=5700, debug=False)