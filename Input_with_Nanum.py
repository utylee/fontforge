import fontforge
import psMat
import unicodedata2

uni_from = "U+AC00"

#uni_to = "U+AC59" # normal Imma.ttf
uni_to = "U+AC5A" # normal ? little wider?
#uni_to = "U+AC5B" # normal ? little wider?
#uni_to = "U+AC5C" # little wider
#uni_to = "U+AC5F" # little wider
#uni_to = "U+AC60" # little wider

print 'Starting..'

print 'Opening source font..'
a = fontforge.open('NanumGothicCoding.sfd')
#a.selection.select(("ranges", None), "U+AC00", "U+D7A3")
#a.selection.select(("ranges", None), "U+AC00", "U+AC10")
#a.selection.select(("ranges", None), "U+AC00", "U+AC40") # GUM normal 
#a.selection.select(("ranges", None), "U+AC00", "U+AC59") # GUM normal 
a.selection.select(("ranges", None), uni_from, uni_to) # GUM little wider 
#a.selection.select(("ranges", None), "U+AC00", "U+AC80") # GUM normal ? little wider
#a.selection.select(("ranges", None), "U+AC00", "U+AC81") # GUM normal ?
#a.selection.select(("ranges", None), "U+AC00", "U+ACDF") # a little wider
#a.selection.select(("ranges", None), "U+AC00", "U+ACE0") # a little wider
#a.selection.select(("ranges", None), "U+AC00", "U+AD10") # twice wider
#a.selection.select(("ranges", None), "U+AC00", "U+AE10")
#a.selection.select(("ranges", None), "U+AC00", "U+B097")
print 'Copying..'
a.copy()

print 'Opening target font.. Input.sfd'
i = fontforge.open('Imma2-Base.sfd')
#i = fontforge.open('Imma-Base.sfd')

print 'Select Rngs'
#i.selection.select(("ranges", None), "U+AC00", "U+AC59")
i.selection.select(("ranges", None), uni_from, uni_to)
#i.selection.select(("ranges", None), "U+AC00", "U+D7A3")

print 'Pasting'
i.paste()

#i['A'].condenseExtend(1,0,1,-30)
#i['A'].transform(psMat.translate(50,))
##i['A'].transform(psMat.scale(1.35,1.00))

print 'Transforming:'
#l = i.selection.select(("ranges", None), "U+AC00", "U+D7A3")
l = i.selection.select(("ranges", None), uni_from, uni_to)

for it in l:
    ch = unichr(i[it].encoding)
    print it, '/', len(l), i[it].unicode, ch, unicodedata2.script_cat(ch)
    #i[it].transform(psMat.scale(1.35,1.30))
    i[it].transform(psMat.scale(1.35,1.00))
    i[it].condenseExtend(1,0,1,-13)
    #i[it].condenseExtend(1,0,1,-13,False)
    i[it].transform(psMat.translate(50,))
    
    while i[it].width < 1324:
        i[it].transform(psMat.translate(1,))
        #print 'cur width : ', i[it].width


print 'Saving'
#i.save("Imma.sfd")
i.save("Imma2.sfd")

print 'Generating ttf'
#i.generate("/Users/utylee/Downloads/Imma.ttf")
i.generate("/Users/utylee/Downloads/Imma2.ttf")

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

