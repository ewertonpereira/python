text: str = '''
enter your text here
'''
print(f'I used {(result := len(text.split()))} words')
