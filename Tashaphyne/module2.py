#testnormlalize
from __future__ import unicode_literals
from stemming import *


word=u"الْعَراَبِيّةُ"
ArListem=ArabicLightStemmer();
stem=ArListem.lightStem(word);
print stem


print ArListem.get_unvocalized();
word=u'أفتكاتبانني'
stem=ArListem.lightStem(word);
print ArListem.get_stem();
print ArListem.get_right();


ArListem=ArabicLightStemmer();
word=u'فتصبرين'
stem=ArListem.segment(word);
print str(ArListem.get_affix_list()).decode("unicode-escape");
print ArListem.get_segment_list();
