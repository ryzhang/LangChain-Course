from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
#prompt_value = prompt.invoke({"topic": "ice cream"})
#print(prompt_value)
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

reply = chain.invoke({"topic": "ice cream"})
print(reply)