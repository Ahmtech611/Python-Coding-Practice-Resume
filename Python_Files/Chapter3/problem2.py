#String Templete(Like a part or collection of some kind of data as a templete) like Letter Templete:

# Letter = '''Dear Ahmad Ali Butt,
#             You are selected.
#             31/07/2025
# '''
#OR
Letter = '''Dear <|Name|>
       You are selected.
        <|Data|>
'''

print(Letter.replace("<|Name|>","Ahmad Ali Butt").replace("<|Data|>","21,January,2025"))
