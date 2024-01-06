import json, os

def load_config():
    global config
    with open("config.json") as f:
        config = json.loads(f.read())

load_config()

def load_key(key_name: str):
    os.environ[key_name] = config[key_name]

# NEED a json file named config.json in the root of this directory that contains the following API keys:
#   OPEN_API_KEY
#   HUGGINGFACEHUB_API_TOKEN 
#   SERPAPI_API_KEY
# (These are the expected key names. The values are the keys.)
