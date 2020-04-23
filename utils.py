from gingerit.gingerit import GingerIt

def auto_correct(text):
    # text = 'The smelt of fliwers bring back memories.'
    parser = GingerIt()
    result=parser.parse(text)
    return result['result'] 

# text="I am feel verry happy"
# result=auto_correct(text)
# print(result)

# print(auto_correct())