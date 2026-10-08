from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

def generate(question, chunks):

    input_for_claude = ''
    system_prompt = ('Using exclusively the chunks of text I send you, answer the question at the end of each message and cite the '
    'file paths where you found the answer. If the chunks of text are ' 
    'irrelevant to the question, say you cannot find that information in the chunks.')


    for index, items in enumerate(chunks):
        input_for_claude+= f'[{index+1}] {items[1]}\n{items[0]}\n\n'

    content_message = f'<chunks>\n{input_for_claude}\n</chunks>\n\n<question>\n{question}\n</question>'

    message = [{'role':'user', 'content':content_message}]


    response = client.messages.create(model='claude-sonnet-5-5', max_tokens=16000, system=system_prompt, messages=message)

    for content_block in response.content:

        if content_block.type == 'text':
            return content_block.text