import fontforge
import psMat

print 'Starting..'

print 'Opening source font..'
a = fontforge.open('NanumGothicCoding.sfd')
#a.selection.select(("ranges", None), "A", "Z")
#a.selection.select(("ranges", None), "U+AC00", "U+D7A3")
a.selection.select(("ranges", None), "U+AC00", "U+AC10")
print 'Copying..'
a.copy()

print 'Opening target font.. Input.sfd'
i = fontforge.open('Input-Regular-Light.sfd')

print 'Select Rngs'
i.selection.select(("ranges", None), "U+AC00", "U+AC10")

print 'Pasting'
i.paste()

#i['A'].condenseExtend(1,0,1,-30)
#i['A'].transform(psMat.translate(50,))
##i['A'].transform(psMat.scale(1.35,1.00))

print 'Transforming:'
#l = i.selection.select(("ranges", None), "U+AC00", "U+D7A3"):
l = i.selection.select(("ranges", None), "U+AC00", "U+AC10")
for it in l:
    print it, '/', len(l)
    i[it].transform(psMat.scale(1.35,1.30))
    i[it].condenseExtend(1,0,1,-13)
    i[it].transform(psMat.translate(50,))

print 'Saving'
i.save("Imma.sfd")

'''
n = fontforge.font()
print '1'
n.fontname = "Imma"
print '1'
n.selection.select(("ranges", None), "U+0041", "U+005A")
n.paste()
print '1'
#print n['A'].foreground()
n.save("Imma.sfd")
'''

