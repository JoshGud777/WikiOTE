import re


def md_all(doc):
    newdoc = doc[:]
    cmds = [
        ['\*\*.*?\*\*', '<b>','</b>'],  # Bold
        ['~~.*?~~', '<s>', '</s>'],  # Strick out
        ['__.*?__', '<i>', '</i>'],  # Italics
        ['{{.*?}}', '<
        ]
    for cmd in cmds:
        newdoc = md_fr(cmd[0], cmd[1], cmd[2], newdoc)

    return newdoc

def md_url(doc):
    cmd = ["[^href='.']htt[p,s]*://[\w,.]*[/{1}\w*/{1}]*\.?\w*[\:\%\/\.\#\+\@\,\!\w*=\w*\&?]*",
         '<a href=\'url\'>', '</a>']  # Links
    newdoc = doc[:]
    while True:
        rematch = re.search(cmd[0], newdoc)
        if rematch == None:
            break
        cmd[1] = cmd[1].replace('url', rematch.group(0))
        oldword = str(rematch.group(0))
        newword = cmd[1] + oldword + cmd[2]
        newdoc = newdoc.replace(oldword, newword)
    return newdoc

def md_fr(MDCODE, RP0, RP1, doc):
    newdoc = doc[:]
    while True:
        rematch = re.search(MDCODE, newdoc)
        if rematch == None:
            break
        oldword = str(rematch.group(0))
        newword = RP0 + oldword[2:-2] + RP1
        newdoc = newdoc.replace(oldword, newword)
    return newdoc


if __name__ == '__main__':
    doc = '''Edit the **Expression __&__ Text** to see matches. Roll over matches or
the expression for ~~details.~~ Undo ~~__mistakes__ with~~ **ctrl-z**. Save & Share expressions
with friends **or the Community**. **A full Reference &** Help is available in the
**Library, or watch the video Tutorial.**

http://hi.bye.fuckyou/godie?method=knife

s

http://dsaweq.wqe.das/ljkld?eeeddd=fff'''
    m = re.search('\$\$([0-9,a-f]{6})\$\$.*?\$\$', '$$65fd89$$jklsjfkls$$')
    print(m.group(1))
'''

'''
