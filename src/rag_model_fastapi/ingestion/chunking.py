import re

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






        