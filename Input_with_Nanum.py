import fontforge
import psMat, math
import unicodedata2

b_shrink = False
uni_from = "U+AC00"
#target_width = 1324
#target_width = 1400
target_width = 2200

#uni_to = "U+AC59" # normal Imma.ttf
#uni_to = "U+AC5A" # normal ? little wider?
#uni_to = "U+AC5B" # normal ? little wider?
#uni_to = "U+AC5C" # little wider
#uni_to = "U+AC5F" # little wider
#uni_to = "U+AC60" # little wider
uni_to = "U+D7A3" # full last

print 'Starting..'

print 'Opening source font..'
#a = fontforge.open('NanumGothicCoding.sfd')
a = fontforge.open('D2Coding.sfd')
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
#i = fontforge.open('Imma2-Base.sfd')
#i = fontforge.open('Imma2-Regular-Base.sfd')
#i = fontforge.open('Menlo for powerline.ttf')
i = fontforge.open('EnvyCodeR-Base.sfd')
#i = fontforge.open('Imma-Base.sfd')

#ranges = [(uni_from, uni_to), ("U+1100", "U+11FF"), ("U+3130", "U+318F")]
ranges = [(uni_from, uni_to)]

for r in ranges:
    print '\n\n\n\nSelect source Rngs'
    #i.selection.select(("ranges", None), "U+AC00", "U+AC59")
    #i.selection.select(("ranges", None), uni_from, uni_to)
    #a.selection.select(("ranges", None), uni_from, uni_to) # GUM little wider 
    a.selection.select(("ranges", None), r[0], r[1])
    a.copy()

    print 'Select destination Rngs'
    i.selection.select(("ranges", None), r[0], r[1])

    print 'Pasting'
    i.paste()


#i['A'].condenseExtend(1,0,1,-30)
#i['A'].transform(psMat.translate(50,))
##i['A'].transform(psMat.scale(1.35,1.00))

print 'Transforming:'
#l = i.selection.select(("ranges", None), "U+AC00", "U+D7A3")
#l = i.selection.select(("ranges", None), uni_from, uni_to)
l = i.selection.changed()

for it in l:
    ch = unichr(i[it].encoding)
    print it, '/', len(l), i[it].unicode, ch, unicodedata2.script_cat(ch)

    # scaling
    #i[it].transform(psMat.scale(1.35,1.30))
    #i[it].transform(psMat.scale(1.28,1.22), ("round"))
    #i[it].transform(psMat.scale(1.45,1.33), ("round")) - 1
    #i[it].transform(psMat.scale(2.45,2.33), ("round"))# - 4
    i[it].transform(psMat.scale(3.0,2.5), ("round"))# - 5
    #i[it].transform(psMat.scale(3.5,3.0), ("round"))# - 6
    #i[it].transform(psMat.scale(4.30,4.00), ("round")) #- 10

    #skew(italic)
    #i[it].transform(psMat.skew(math.radians(9)))
    #i[it].transform(psMat.scale(1.35,1.00))
    #i[it].condenseExtend(1,0,1,-13)
    i[it].condenseExtend(1,0,1,-30)
    #i[it].condenseExtend(1,0,1,-13,False)
    #move to right a little 
    i[it].transform(psMat.translate(20,))
    
    # width to target
    while i[it].width < target_width:
        i[it].transform(psMat.translate(1,))
        #print 'cur width : ', i[it].width


print 'Saving..'
#i.save("Imma.sfd")
#i.save("Imma2.sfd")
i.save("/Users/utylee/Downloads/Imma2.sfd")

print 'Generating ttf...'
#i.generate("/Users/utylee/Downloads/Imma.ttf")
i.generate("/Users/utylee/Downloads/Imma2-5.ttf")


removed_num = 0
# shrink size process
if b_shrink:
    print 'Shrinken sizes...'

    for it in i:
        try:
            ch = unichr(a[it].unicode)
        except:
            continue
        print it, '/', len(l), i[it].unicode, ch, unicodedata2.script_cat(ch)
        if unicodedata2.script(ch) in ("Common", "Latin", "Hangul"):
            continue
        i.removeGlyph( i[it] )
        print 'removed!'
        removed_num = removed_num + 1

    print 'removed_num = ', removed_num
    i.generate("/Users/utylee/Downloads/Imma2-diet.ttf")


print 'Completed'
print '\a'

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

