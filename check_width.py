import fontforge
import unicodedata2

#a = fontforge.open('Imma2-Base.sfd')
a = fontforge.open('Imma2.sfd')

for i in a:
    try:
        if a[i].width != 662:
            print a[i].width #i, ':', a[i].encoding, chr(a[i].encoding)
        '''
        if a[i].unicode == -1:
            #print  a[i].width, chr(a[i].encoding) 

            print  ord('A'), a['A'].width
            #continue
            '''
        '''
        ch = unichr(a[i].encoding)
        #print ch, unicodedata2.script(ch)
        cat = unicodedata2.script(ch)
        if cat in ('Hangul', 'Common', 'Latin'):
            print cat,unichr(a[i].encoding), a[i].width
            '''
    except:
        pass

