# # import streamlit as st
# # import openai

# # st.title("Medi Bot")
# # openai.api_key=st.secrets["OPEN_AI_API_KEY"]
# # if "openai_model" not in st.session_state:
# #     st.session_state["open_model"]="gpt-3.5-turbo"
# # #intitializing chat history

# # if "messages" not in st.session_state:
# #     st.session_state.messages=[]
    
# #     #display chat messages from history on app rerun
# #     for message in st.session_state.messages:
# #          with st.chat_message(message["role"]):
# #              st.markdown(message["content"])
             
# #              #Reac tot user input
# #              prompt= st.chat_input("What is up?")
# #              if prompt:
# #                   #display user message in chat container
# #                   with st.chat_message("user"):
# #                       st.markdown(prompt)
                      
# #                       #ADd user message to chat history
# #                       st.session_state.messages.append({"role":"user","content":prompt})

# #     with st.chat_message("assistant"):
# #         message_placeholder= st.empty()
# #         full_response = ""
# #         for response in openai.ChatCompletion.create(
# #             model=st.session_state["openai_model"],
# #             messages=[
# #                 {"role": m["role"],"content": m["content"]}
# #                 for m in st.session_state.messages
# #             ],
# #             stream=True,
# #         ):
                  
# #             full_response+=response.choices[0].delta.get("content", "")
# #             message_placeholder.markdown(full_response +  "| ")
# #         message_placeholder.markdown(full_response)
# #     st.session_state.messages.append({"role":"assistant","contemt":full_response})        
#           #OPEN_AI_API_KEY            
                      
# from openai import OpenAI
# import streamlit as st

# st.write("# Med-Bot")
# st.write("## Ask your medical  questions here!")

# st.title("")
# client = OpenAI(api_key=st.secrets["OPEN_AI_API_KEY"])


# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("What is up?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#         for response in client.chat.completions.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         ):
#             full_response += (response.choices[0].delta.content or "")
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})






from openai import OpenAI
import streamlit as st

from openai import OpenAI
import streamlit as st

st.write("# Med-Bot")
st.write("## Ask your medical  questions here!")

st.title("")
client = OpenAI(api_key=st.secrets["OPEN_AI_API_KEY"])


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})