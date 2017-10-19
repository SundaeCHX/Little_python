#-*- coding: utf-8 -*-

from wordcloud import WordCloud,STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random
import os

d = os.path.dirname(__file__)

def grey_color_func(word,font_size,position,orientation,random_state=None,**kwargs):
	return 'hsl(0,0%%,%d%%)' % random.randint(60,100)

# Make the whole mask.
mask = np.array(Image.open(os.path.join(d,'picture.png')))

# Read the whole text.
text = open(os.path.join(d, 'word.txt')).read().decode('gbk')

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
font=os.path.join(os.path.dirname(__file__),'DroidSansFallbackFull.ttf')

wordcloud = WordCloud(font_path=font).generate(text)
wordcloud = WordCloud(font_path=font,max_font_size=40,mask=mask,margin=10,random_state=1).generate(text)

default_colors = wordcloud.to_array()
plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3))
plt.axis("off")
plt.figure()
plt.imshow(default_colors)
plt.axis("off")
plt.show()
