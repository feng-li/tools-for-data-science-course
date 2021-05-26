{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "College graduates may want to study out of China. They need to think about what they want to do for themselves. If they stay out of Chinese for four years, their Chinese is week, the Chinese of four years ago. The other language, maybe English, is stronger, as good as a native speaker's. Where will they live? If they live in China, their English is more than enough, but their Chinese is less than enough. If theyu live out of China, their Chinese is useless, but their English is usually less than enough.What can they do?\n",
      "['College', 'graduates', 'may', 'want', 'to', 'study', 'out', 'of', 'China.', 'They', 'need', 'to', 'think', 'about', 'what', 'they', 'want', 'to', 'do', 'for', 'themselves.', 'If', 'they', 'stay', 'out', 'of', 'Chinese', 'for', 'four', 'years,', 'their', 'Chinese', 'is', 'week,', 'the', 'Chinese', 'of', 'four', 'years', 'ago.', 'The', 'other', 'language,', 'maybe', 'English,', 'is', 'stronger,', 'as', 'good', 'as', 'a', 'native', \"speaker's.\", 'Where', 'will', 'they', 'live?', 'If', 'they', 'live', 'in', 'China,', 'their', 'English', 'is', 'more', 'than', 'enough,', 'but', 'their', 'Chinese', 'is', 'less', 'than', 'enough.', 'If', 'theyu', 'live', 'out', 'of', 'China,', 'their', 'Chinese', 'is', 'useless,', 'but', 'their', 'English', 'is', 'usually', 'less', 'than', 'enough.What', 'can', 'they', 'do?']\n",
      "[['College' 'graduates' 'may' 'want' 'to' 'study' 'out' 'of' 'China.'\n",
      "  'They' 'need' 'to' 'think' 'about' 'what' 'they' 'want' 'to' 'do' 'for'\n",
      "  'themselves.' 'If' 'they' 'stay' 'out' 'of' 'Chinese' 'for' 'four'\n",
      "  'years,' 'their' 'Chinese']\n",
      " ['is' 'week,' 'the' 'Chinese' 'of' 'four' 'years' 'ago.' 'The' 'other'\n",
      "  'language,' 'maybe' 'English,' 'is' 'stronger,' 'as' 'good' 'as' 'a'\n",
      "  'native' \"speaker's.\" 'Where' 'will' 'they' 'live?' 'If' 'they' 'live'\n",
      "  'in' 'China,' 'their' 'English']\n",
      " ['is' 'more' 'than' 'enough,' 'but' 'their' 'Chinese' 'is' 'less' 'than'\n",
      "  'enough.' 'If' 'theyu' 'live' 'out' 'of' 'China,' 'their' 'Chinese'\n",
      "  'is' 'useless,' 'but' 'their' 'English' 'is' 'usually' 'less' 'than'\n",
      "  'enough.What' 'can' 'they' 'do?']]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=\"College graduates may want to study out of China. They need to think about what they want to do for themselves. If they stay out of Chinese for four years, their Chinese is week, the Chinese of four years ago. The other language, maybe English, is stronger, as good as a native speaker's. Where will they live? If they live in China, their English is more than enough, but their Chinese is less than enough. If theyu live out of China, their Chinese is useless, but their English is usually less than enough.What can they do?\"\n",
    "print(a)\n",
    "b=a.split(\" \")\n",
    "print(b)\n",
    "c=np.array(b).reshape(3,32)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
