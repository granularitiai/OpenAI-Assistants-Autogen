#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
import os
from autogen import UserProxyAgent, config_list_from_json
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent


# In[3]:


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

assistant_id = "asst_FXwDLknCKNAhLznBtJ73caEp"
config_list = config_list_from_json("OAI_CONFIG_LIST")
llm_config = {
    "config_list": config_list,
}


# In[ ]:


assistant_config = {
    "assistant_id": assistant_id,
    "tools": [{"type": "retrieval"}],
}

gpt_assistant = GPTAssistantAgent(
    name = "assistant",
    instructions = "You are adapt at question answering",
    llm_config = llm_config,
    assistant_config = assistant_config,
)

user_proxy = UserProxyAgent(
    name = "user_proxy",
    code_execution_config = False,
    is_termination_msg = lambda msg: "TERMINATE" in msg["content"],
    human_input_mode = "ALWAYS",
)

user_proxy.initiate_chat(gpt_assistant, message = "Please list the topics that this file discusses.")


# In[ ]:




