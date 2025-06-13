from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI()
st.title("5 Facts Generator")
schema=[
    ResponseSchema(name='Fact_1',description='first fact about the topic'),
    ResponseSchema(name='Fact_2',description='second fact about the topic'),
    ResponseSchema(name='Fact_3',description='third fact about the topic'),
    ResponseSchema(name='Fact_4',description='fourth fact about the topic'),
    ResponseSchema(name='Fact_5',description='fifth fact about the topic'),
]
topic = st.text_input("Enter your topic")
parser=StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instructions}',
    input_variables=[topic],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
 


if st.button('5 Facts'):
    # Step 1: Generate detailed report
    chain= template | model | parser
    result= chain.invoke({topic})
    # Display both
    
    st.write(result)


