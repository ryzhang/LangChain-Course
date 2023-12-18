from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pprint import pprint


model = ChatOpenAI()
prompt=ChatPromptTemplate.from_template("tell me a short joke about {topic}")
chain=prompt|model
print(chain.input_schema.schema())
print(prompt.input_schema.schema())
print(model.input_schema.schema())
pprint(chain.output_schema.schema())

for s in chain.stream({"topic": "bears"}):
    print(s.content,end="", flush=True)

#print(chain.invoke({"topic": "bears"}))

#print(chain.batch([{"topic": "bears"}, {"topic": "cats"}]))


 