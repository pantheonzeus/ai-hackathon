BASIC_CUSTOMER_PROMPT = """I received a damaged package and the shop is not responding. 
I need the article and I bought it now somewhere else. Can you help me? I am a {} at the age of 
{}. My financial situation is {}. I shop {} per month. Adress me with the tone of voice 
{}. Emphasize according to the credit score of {} the impact to the financial situation, but be 
mindful and take person in considderation. Take the usual shopping items of {} into consideration of how 
stressed the person might be and what information Klarna can give. Write a personal message. Be subtle with any 
financial situation mention. It should make the person feel good and not judged or put into a segment. 
"""

BASIC_CUSTOMER_PROMPT_PLANNER = """You get customer questions. 
1. You decode their customer segmen based on the personal data they shared. 
2. Then you take the provided probelem with the Klarna services and give and solution. 
3. Then you answer per Email in the preferend tone of voice of this specific cutomer segment.

Customer Question:
I received a damaged package and the shop is not responding. 
I need the article and I bought it now somewhere else. Can you help me?
I am the age of 
{}. My financial situation is {}. I shop {} per month.

"""
