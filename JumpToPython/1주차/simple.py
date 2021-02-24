#simple.py
languages = ['python', 'perl', 'C', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['C','java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")