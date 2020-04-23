from gingerit.gingerit import GingerIt
import requests
def auto_correct(text):
    # text = 'The smelt of fliwers bring back memories.'
    parser = GingerIt()
    result=parser.parse(text)
    return result['result'] 

def auto_check(input_text):
    # input_text='She’s married with an dentist.'  
    url='https://languagetool.org/api/v2/check'
    dataPost={'text':input_text,'language':'en-US'}
    response=requests.post(url, data=dataPost)
    result=response.json()

    if not len(result['matches']):
        input_text_err=''
        message='Perfect'
    else:
        offset=result['matches'][0]['offset']
        length=result['matches'][0]['length']
        input_text_err=input_text[offset:(offset+length)]
        message=result['matches'][0]['message']
    return input_text_err,message
# print()

input_text='She’s married to a dentist.'  
url='https://languagetool.org/api/v2/check'
dataPost={'text':input_text,'language':'en-US'}
response=requests.post(url, data=dataPost)
result=response.json()
