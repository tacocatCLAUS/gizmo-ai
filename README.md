![Hi, i'm Gizmo.](/images/gizmorbg.png)
---
Gizmo was a hobby project learning aboout ollama and local ai and became an assistant that I use on a day to day basis. Taking advantage of both fully custom coded internet search and a functioning RAG allowing for upload of your pdfs and other text documents Gizmo works easily with your workflow and allows for smooth converstaion even on low power machines.
<img src="/images/example.png" height="100">

## Features
Implemented:
 - Web search (via api)
 - PDF upload
 - Markdown upload
 - Looped, fluid conversation
 - <u>Optional</u> openai integration

Planned:
 - Local web search (via scraping)
 - Most code filetype uploads
 - Image Upload
 - AWS Rag profiling
 - Implementing hack clubs ai for easy free use
 - Code agent cabable of running commands (via reverse engineered [Warp AI](https://www.warp.dev/ai)) [COMING SOON!]

## Installation
Running the code is pretty simple once you have all the necessary libraries installed.

**Necessary Programs:**
- [Ollama](https://ollama.com/download)
- [Python](https://www.python.org/downloads/) + pip

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


