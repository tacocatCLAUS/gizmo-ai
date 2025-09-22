![Hi, i'm Gizmo.](/images/gizmorbg.png)
---
Gizmo is your local ai assistant. Claude code is at over 33,000 ✩ but not a bit is local. Gizmo is a completely-local, mcp-enabled, personal assistant that can even talk! Just come with good hardware and some MCP servers. Youll be able to tell it to turn off your light in no time!

This has been coded around and works the best with the wizard llm ollama model. All api connections are an afterthought and do not work perfectly (no mcp). Changing the ollama model might have side effects as well. If you wnat to suggest changes and supports for different models look into the model folder.

## Installing / Getting started

Installing is easy. Just install [Ollama](https://ollama.com/),
and either download the release or clone the repo!
Keep in mind that this project takes up about 5 GB of space. If you are demoing just delete the repo and uninstall the pip packages.

```shell
git clone https://github.com/tacocatCLAUS/gizmo.git
cd gizmo
python setup.py
python gizmo.py
```

This will install everything necessary and have you set the configuration.
Keepbin mind that this scriptbis still in development so you should go over the config after it is run.

## Developing
All you need to do is install the project as shown above.
Running setup.py will install from model/requirements.txt but if you want to do this yourself just run: 
```shell
pip install -r model/requirements.txt
```

## Features

* Full MCP support using the same system as Claude
* Ollama and OpenAI support
* Smart RAG handling so you can upload most documents and it will use them accordingly.
* Even realistic voice generation using F5-TTS

## Configuration

Here you should write what are all of the configurations a user can enter when
using the project.

<<<<<<< HEAD
```json
{
  "openai": false,
  "openai_model": "gpt-3.5-turbo",
  "openai_api_key": "",
  "hc": false,
  "hc_model": "meta-llama/llama-4-maverick-17b-128e-instruct",
  "devmode": false,
  "db_clear": true,
  "use_mcp": true,
  "voice": false,
  "rag_model": "none"
}
```
=======
**Setup:**

First, [download the repo](https://github.com/tacocatCLAUS/gizmo-ai/archive/refs/heads/main.zip), extract the zip, and then enter your terminal.  Run ```cd main``` and then ```pip install -r requirements.txt``` then then ```pip install langchain-huggingface``` now edit gizmo.py
```
# Configuration
openai = False # Use OpenAI instead of Ollama model.
openai_model = "gpt-3.5-turbo"  # Set the OpenAI model to use.
devmode = False  # Set to True for development mode, False for production
db_clear = True  # Set to True to clear the database on startup, False to keep it persistent
tavily_api = True  # Set to True to use Tavily API

# API's etc.
userAgent = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15')
openai_api_key = ''
tavily_api_key = ''
```
All of the config variables are supported, except for tavily_api, which is still being implemented. 

You can get your tavily api from [their website](https://app.tavily.com/).
And the openai api (optional) from [their website](https://platform.openai.com/).

Now it is time to **set the model**.

Run ```cd setup```, ```ollama pull gemma3:1b``` then ```bash llm-maker.sh``` This will make the custom chatbot. If you want to edit the model's personality, edit the system.txt file in the setup directory.

Now that everything is set up, you can leave the setup directory with ```cd ..``` and then run ```python gizmo.py``` Now you can interact with gizmo!
>>>>>>> 296a0e592502c6850af21623f312b9ae61e427bf


#### openai, hc 
Default: `'false'`

Model selection is handled through these two booleans. If both are false, the program will default to using Ollama models. The model can be changed through the respective variable.

#### voice
Default: `'false'`

If true, the program will use F5-TTS to speak responses. If false, it will just print them.

#### use_mcp
Default: `'true'`

This will use mcp from the mcp.json file. If not it wont be used.

#### rag_model
Default: `'none'`
Options: `ollama, 'openai'`
RAG model selection is handled through this variable. If set to 'none', no RAG will be used. If set to another model, that model will be used for RAG.

#### db_clear
Default: `'true'`
The RAG will be cleared on startup if this is true. If false the ai will have a bit of a memory.

#### devmode
Default: `'false'`
This will show EVERYTHING in the console. Useful for debugging. But very annoying.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing
The code in this project is licensed under MIT license.
