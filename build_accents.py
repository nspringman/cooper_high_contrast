from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# define glyph constructions
txt = '''\
Agrave = A + grave@center,top
Aacute = A + acute@center,top
Acircumflex = A + circumflex@center,top
Adieresis = A + dieresis@center,top
Atilde = A + tilde@center,top
Egrave = E  + grave@center,top
Eacute = E + acute@center,top
Ecircumflex = E + circumflex@center,top
Edieresis = E + dieresis@center,top
Uacute = U + acute@center,top
Igrave = I  + grave@center,top
Iacute = I + acute@center,top
Icircumflex = I + circumflex@center,top
Idieresis = I + dieresis@center,top
Oacute = O + acute@center,top
Ocircumflex = O + circumflex@center,top
Otilde = O + tilde@center,top
agrave = a + grave@center,top
aacute = a + acute@center,top
acircumflex = a + circumflex@center,top
atilde = a + tilde@center,top
egrave = e + grave@center,top
eacute = e + acute@center,top
ecircumflex = e + circumflex@center,top
edieresis = e + dieresis@center,top
igrave = i + grave@center,top
iacute = i + acute@center,top
icircumflex = i + circumflex@center,top
idieresis = i + dieresis@center,top
ntilde = n + tilde@center,top
ograve = o + grave@center,top
oacute = o + acute@center,top
ocircumflex = o + circumflex@center,top
otilde = o + tilde@center,top
odieresis = o + dieresis@center,top
ugrave = u + grave@center,top
uacute = u + acute@center,top
ucircumflex = u + circumflex@center,top
udieresis = u + dieresis@center,top
yacute = y + acute@center,top
ydieresis = y + dieresis@center,top
'''

# get the actual glyph constructions from text
constructions = ParseGlyphConstructionListFromString(txt)

# get the current font
font = CurrentFont()

# collect glyphs to ignore if they already exist in the font
ignoreExisting = [L.split('=')[0].strip()[1:] for L in txt.split('\n') if L.startswith('?')]

# iterate over all glyph constructions
for construction in constructions:

    # build a construction glyph
    constructionGlyph = GlyphConstructionBuilder(construction, font)

    # if the construction for this glyph was preceded by `?`
    # and the glyph already exists in the font, skip it
    if constructionGlyph.name in font and constructionGlyph.name in ignoreExisting:
        continue

    # get the destination glyph in the font
    glyph = font.newGlyph(constructionGlyph.name, clear=True)

    # draw the construction glyph into the destination glyph
    constructionGlyph.draw(glyph.getPen())

    # copy construction glyph attributes to the destination glyph
    glyph.name = constructionGlyph.name
    glyph.unicode = constructionGlyph.unicode
    glyph.width = constructionGlyph.width
    glyph.markColor = 1, 1, 0, 0.5

    # if no unicode was given, try to set it automatically
    if glyph.unicode is None:
        glyph.autoUnicodes()