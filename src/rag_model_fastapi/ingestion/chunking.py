import re

from nltk.tokenize import sent_tokenize

from rag_model_fastapi.retrieval.model import model


class CodeBlockProtector:

    def __init__(self):
        self.codeblocks = {}
        self.counter = 0

    def protect(self, match):
        self.counter +=1
        placeholder = f"__CODEBLOCK{self.counter}__"

        self.codeblocks[placeholder] = match.group(0)

        return placeholder


def restore_placeholder_codeblocks(chunk: str, list_of_placeholders: dict):

    for key, value in list_of_placeholders.items():
        if key in chunk:
            chunk = chunk.replace(key, value)


    return chunk


def chunk_text(text):

    codeblock = CodeBlockProtector()
    pattern = r'```.*?```'

    text = re.sub(pattern, codeblock.protect, text, flags = re.DOTALL)
    list_of_sentences = sent_tokenize(text)
    current_chunk_length = 0
    chunk = ''
    list_of_chunks = []
    current_sentences = []
    overlap = ''

    for x in list_of_sentences:

        real_restored_sentence = restore_placeholder_codeblocks(x, codeblock.codeblocks)
        
        if len(model.tokenizer.encode(real_restored_sentence)) > 300:
                    if chunk:
                        list_of_chunks.append(chunk)
                        list_of_chunks.append(real_restored_sentence)
                        chunk = ''
                    else:
                        list_of_chunks.append(real_restored_sentence)
                    continue
        
        current_sentences.append(x)
        current_chunk_length += len(model.tokenizer.encode(real_restored_sentence))
                
        if current_chunk_length < 300:
            chunk += ' ' + x
        else:
            list_of_chunks.append(chunk)
            for y in range(len(current_sentences) - 2, -1, -1):
                if (len(model.tokenizer.encode(overlap)) + len(model.tokenizer.encode(current_sentences[y])))<60:
                    if overlap:
                        overlap+= ' ' + current_sentences[y]
                    else:
                        overlap += current_sentences[y]
                else:
                   break
            chunk = overlap + ' ' + x
            current_chunk_length = len(model.tokenizer.encode(restore_placeholder_codeblocks(chunk, codeblock.codeblocks)))
            current_sentences = [x]
            overlap = ''

    if chunk:
        list_of_chunks.append(chunk)

    final_chunks = [restore_placeholder_codeblocks(chunk, codeblock.codeblocks) for chunk in list_of_chunks]

    return final_chunks
            
            

         




        