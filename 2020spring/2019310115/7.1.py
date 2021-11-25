{
  "cells": [
   {
    "cell_type": "code",
    "execution_count": 1,
    "metadata": {},
    "outputs": [],
    "source": [
     "import pandas as pd"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 2,
    "metadata": {},
    "outputs": [],
    "source": [
     "cor  = pd.read_csv('Coronavirus_data', header=None)"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 3,
    "metadata": {},
    "outputs": [],
    "source": [
     "wor = cor[0][1]"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 4,
    "metadata": {},
    "outputs": [
     {
      "data": {
       "text/plain": [
        "['全球累计278万例新冠肺炎确诊病例\\x012020-04-24\\x01疫情新闻网
       ]
      },
      "execution_count": 4,
      "metadata": {},
      "output_type": "execute_result"
     }
    ],
    "source": [
     "from nltk.tokenize import sent_tokenize\n",
     "sent_tokenize(wor)"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 5,
    "metadata": {},
    "outputs": [],
    "source": [
     "import jieba"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 6,
    "metadata": {},
    "outputs": [
     {
      "name": "stderr",
      "output_type": "stream",
      "text": [
       "Building prefix dict from the default dictionary ...\n",
       "Dumping model to file cache /var/folders/rw/nr6x4m013zb9hmrmkhk_3t3m0000gn/T/jieba.cache\n",
       "Loading model cost 1.086 seconds.\n",
       "Prefix dict has been built successfully.\n"
      ]
     },
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "Default Mode: 全球/ 累计/ 278/ 万/ 例新冠/ 肺炎/ 确诊/ 病例/ \u0001/ 2020/ -/ 04/ -/ 24/ \u0001/ 疫情/ 新闻/ 网/ "
      ]
     }
    ],
    "source": [
     "seg_list = jieba.cut(wor, cut_all=False)\n",
     "print(\"Default Mode: \" + \"/ \".join(seg_list))  "
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 7,
    "metadata": {},
    "outputs": [],
    "source": [
     "import jieba.analyse"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 8,
    "metadata": {},
    "outputs": [],
    "source": [
     "ser = jieba.analyse.textrank(wor, topK=15, withWeight=False, \n",
     "                       allowPOS=('ns', 'n', 'vn', 'v'))"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 20,
    "metadata": {},
    "outputs": [],
    "source": [
     "sen = list()",
     "num = len(cor)\n",
     "for i in range(1, num):\n",
     "    wor = cor[0][i-1]\n",
     "    ser = jieba.analyse.textrank(wor, topK=15, withWeight=False, \n",
     "                       allowPOS=('ns', 'n', 'vn', 'v'))\n",
     "    sen = sen+ser"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 23,
    "metadata": {},
    "outputs": [],
    "source": [
     "from os import path\n",
     "from imageio import imread\n",
     "import matplotlib.pyplot as plt\n",
     "from wordcloud import WordCloud"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 31,
    "metadata": {},
    "outputs": [],
    "source": [
     "d = path.abspath('.')\n",
     "back_coloring_path = \"ccc.jpg\"\n",
     "back_coloring = imread(path.join(d, back_coloring_path))"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 40,
    "metadata": {},
    "outputs": [],
    "source": [
     "met_txt = \" \".join(str(i) for i in sen)"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 63,
    "metadata": {},
    "outputs": [],
    "source": [
     "wc = WordCloud(\n",
     "    background_color='white',",
     "    mask=back_coloring_path,",
     "    max_words=2000,",
     "    max_font_size=150,",
     "    random_state=1,",
     "    scale=1",
     ")"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 54,
    "metadata": {},
    "outputs": [],
    "source": [
     "wcdict={}\n",
     "for word in sen:\n",
     "    if len(word)==1:\n",
     "        continue\n",
     "    else:\n",
     "        wcdict[word]=wcdict.get(word,0)+1"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 56,
    "metadata": {},
    "outputs": [
     {
      "ename": "TypeError",
      "evalue": "expected string or bytes-like object",
      "output_type": "error",
      "traceback": [
       "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
       "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
       "\u001b[0;32m<ipython-input-56-2c7608cb4ac0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mwc\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgenerate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mwcdict\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
       "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/wordcloud/wordcloud.py\u001b[0m in \u001b[0;36mgenerate\u001b[0;34m(self, text)\u001b[0m\n\u001b[1;32m    617\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    618\u001b[0m         \"\"\"\n\u001b[0;32m--> 619\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgenerate_from_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    620\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    621\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_check_generated\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/wordcloud/wordcloud.py\u001b[0m in \u001b[0;36mgenerate_from_text\u001b[0;34m(self, text)\u001b[0m\n\u001b[1;32m    598\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    599\u001b[0m         \"\"\"\n\u001b[0;32m--> 600\u001b[0;31m         \u001b[0mwords\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprocess_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    601\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgenerate_from_frequencies\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mwords\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    602\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/wordcloud/wordcloud.py\u001b[0m in \u001b[0;36mprocess_text\u001b[0;34m(self, text)\u001b[0m\n\u001b[1;32m    561\u001b[0m         \u001b[0mregexp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mregexp\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mregexp\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0;34mr\"\\w[\\w']+\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    562\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 563\u001b[0;31m         \u001b[0mwords\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mre\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfindall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mregexp\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtext\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mflags\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    564\u001b[0m         \u001b[0;31m# remove stopwords\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    565\u001b[0m         \u001b[0mwords\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mword\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mword\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mwords\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mword\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mstopwords\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;32m~/opt/anaconda3/lib/python3.7/re.py\u001b[0m in \u001b[0;36mfindall\u001b[0;34m(pattern, string, flags)\u001b[0m\n\u001b[1;32m    221\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    222\u001b[0m     Empty matches are included in the result.\"\"\"\n\u001b[0;32m--> 223\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0m_compile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpattern\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mflags\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfindall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstring\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    224\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    225\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mfinditer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpattern\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstring\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mflags\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;31mTypeError\u001b[0m: expected string or bytes-like object"
      ]
     }
    ],
    "source": [
     "wc.generate(wcdict)"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 57,
    "metadata": {},
    "outputs": [],
    "source": [
     "wl_split=' '.join(sen)"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 66,
    "metadata": {},
    "outputs": [
     {
      "ename": "NameError",
      "evalue": "name 'Wordcloud' is not defined",
      "output_type": "error",
      "traceback": [
       "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
       "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
       "\u001b[0;32m<ipython-input-66-f1bc297ab0f2>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mmywc\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mWordcloud\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgenerate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mwl_split\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
       "\u001b[0;31mNameError\u001b[0m: name 'Wordcloud' is not defined"
      ]
     }
    ],
    "source": [
     "mywc = Wordcloud().generate(wl_split)"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 60,
    "metadata": {},
    "outputs": [],
    "source": [
     "plt.rcParams['font.sans-serif'] = ['SimHei']"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 61,
    "metadata": {},
    "outputs": [
     {
      "data": {
       "text/plain": [
        "<matplotlib.image.AxesImage at 0x1a22004210>"
       ]
      },
      "execution_count": 61,
      "metadata": {},
      "output_type": "execute_result"
     },
     {
      "name": "stderr",
      "output_type": "stream",
      "text": [
       "findfont: Font family ['sans-serif'] not found. Falling back to DejaVu Sans.\n"
      ]
     },
     {
      "data": {
       "image/png": "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\n",
       "text/plain": [
        "<Figure size 432x288 with 1 Axes>"
       ]
      },
      "metadata": {
       "needs_background": "light"
      },
      "output_type": "display_data"
     }
    ],
    "source": [
     "plt.imshow(mywc)"
    ]
   }
  ],
  "metadata": {
   "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
   },
   "language_info": {
    "codemirror_mode": {
     "name": "ipython",
     "version": 3
    },
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": "3.7.4"
   }
  },
  "nbformat": 4,
  "nbformat_minor": 2
 }