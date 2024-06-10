import os
from list import extract_first_list_from_string

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    
)




Prompt = """Create a list that takes a user utterance as input and extracts the following information in the specified order:

Price range (minimum and maximum)
Product type (Necklace, Ring, Bracelet, Earrings)
Materials (Gold, Silver, Platinum, Diamond)
Occasions (Daily, Office, Party)
Weight(minimum and maximum)
The function should return a list containing these extracted values. The user utterance may contain any combination of the mentioned elements, but they should be extracted in the order mentioned above. If a particular element is not mentioned in the utterance, it should be represented as None in the output list. The price range should be extracted as numerical values, and product types, materials, and occasions should be extracted as strings. The user utterance should be assumed to be in English.
Rules to be follow:
only extract as list dont add any other texts or any other
format in the order of [int(Pricerangemin), int(pricerangemax), producttype, materials,occasions,int(minWeight),int(maxweight)]
only map to the list acording to input dont map anything else
Avoid Plurals like rings, necklaces and map according type
Example:

Example User Utterance: "I'm looking for 10g gold and silver earrings under 10000 for a party."

Output: [0, 10000, "Earrings", "Gold,Silver", "Party",5,10]

Explanation:

Price range: 0 to 10000 (under 10000)
Product type: Earrings
Materials: Gold
Occasion: Party
weightMin:10 (because there is no range)
WeightMax:10 (because there is no range)

Example User Utterance: "list 10g gold"

Output: [None, None, None, "Gold", None ,10,10]

Explanation:

Price range: None
Product type: Earrings
Materials: Gold
Occasion: None
weightMin:10 (because there is no range)
WeightMax:10 (because there is no range)


Example User Utterance: "show earing in gold and silver"

Output: [None, None, None, "Gold,Silver", None ,None,None]

Explanation:

Price range: None
Product type: Earrings
Materials: Gold,silver
Occasion: None
weightMin:None
WeightMax:None
"""

def input_utterance(input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": Prompt,
            },
            {
                "role": "user",
                "content": input}],
        model="llama3-70b-8192",
    )

    response = chat_completion.choices[0].message.content
    response = extract_first_list_from_string(response)
    print(response)
    print(type(response))

    return response

if __name__ == "__main__":
    input_utterance(input="list me a 10g gold")
