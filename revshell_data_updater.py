import execjs
import httpx
import asyncio
import pprint

runtime = execjs.get()

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://raw.githubusercontent.com/0dayCTF/reverse-shell-generator/main/js/data.js")
        context = runtime.compile(response.text)
        commands = {
                    'reverseShellCommands': context.eval('reverseShellCommands'),
                    'bindShellCommands': context.eval('bindShellCommands'),
                    'msfvenomCommands': context.eval('msfvenomCommands'),
                    'hoaxShellCommands': context.eval('hoaxShellCommands'),
                    'rsgData': context.eval('rsgData')
                }
        # output to file
        with open('static/data.py', 'w') as f:
            f.write("data = ")
            pprint.pprint(commands, stream=f)

asyncio.run(fetch_data())

# from static.data import data
# print(data['reverseShellCommands'][0])