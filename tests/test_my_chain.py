from langchain.chains import LLMChain
from langchain.llms import HumanInputLLM
from langchain.prompts.prompt import PromptTemplate

from langchain_sql_test import MyChain


def test_my_chain() -> None:
    """Edit this test to test your chain."""
    llm = HumanInputLLM(input_func=lambda: "baz")
    llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template("foo {bar}"))
    MyChain(llm_chain=llm_chain)
