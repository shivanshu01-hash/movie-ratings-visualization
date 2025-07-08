# letter = '''
# dear <|name|>
# You are selected!
# <|date|>'''

letter = '''
dear <|name|>
You are selected!
<|date|>'''


print(letter.replace("<|name|>", "Shivanshu").replace("<|date|>", '20 oct 2050'))
