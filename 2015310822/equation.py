{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solut():\n",
    "    import random\n",
    "    import math\n",
    "    i=random.sample(range(1,100),10)\n",
    "    j=random.sample(range(1,100),10)\n",
    "    k=random.sample(range(1,100),10)\n",
    "    for a in i:\n",
    "        for b in j:\n",
    "            for c in k:\n",
    "                    derta = b**2-4*a*c\n",
    "                    if derta == 0:\n",
    "                        x1=-c/b\n",
    "                        x2=x1\n",
    "                        print (x1,x2)\n",
    "                    elif derta >0:\n",
    "                        x1=(-b + math.sqrt(derta))\n",
    "                        x2=(-b - math.sqrt(derta))\n",
    "                        print (x1,x2)\n",
    "                    elif derta<0:\n",
    "                        print(\"方程无实根\")"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
