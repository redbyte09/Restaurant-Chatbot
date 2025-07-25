from langchain_community.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os

# Set your Cohere API key
os.environ['COHERE_API_KEY'] = "EEHgpuTUanIxAvCpbvMN7nlmVZBuOBiK7RZ8T8hg"

# Use Cohere instead of OpenAI
llm = Cohere(temperature=0.7, model="command")

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name', 'cuisine'],
        template="""
        Suggest 5 simple and popular {cuisine} food items for a restaurant named {restaurant_name}.
        Keep the names easy to understand. Return them as a comma-separated string.
        """
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    response = chain({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
