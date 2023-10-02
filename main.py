with open("_chat.txt", 'r', encoding='utf-8') as fp:
    text = fp.readlines()
    excite =0
    for eachline in text:
        if ':)' in eachline:
            excite=excite+1
    print(' Admin Sir!! Sapiens ungala ethana times excite aagaa vachirukanga :' +str(excite))
    