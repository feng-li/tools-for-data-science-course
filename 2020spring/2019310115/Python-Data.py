{
  "cells": [
   {
    "cell_type": "code",
    "execution_count": 1,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "111\n",
       "222\n",
       "333\n"
      ]
     }
    ],
    "source": [
     "with open(\"data/a.txt\",encoding=\"utf-8\",mode=\"r\") as myfile:\n",
     "    print(myfile.read())"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 2,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "111\n",
       "\n"
      ]
     }
    ],
    "source": [
     "with open(\"data/a.txt\",encoding=\"utf-8\",mode=\"r\") as myfile:\n",
     "    print(myfile.readline())"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 3,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "['111\\n', '222\\n', '333']\n"
      ]
     }
    ],
    "source": [
     "with open(\"data/a.txt\",encoding=\"utf-8\",mode=\"r\") as myfile:\n",
     "    print(myfile.readlines())"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 6,
    "metadata": {},
    "outputs": [
     {
      "data": {
       "text/plain": [
        "True"
       ]
      },
      "execution_count": 6,
      "metadata": {},
      "output_type": "execute_result"
     }
    ],
    "source": [
     "myfile.closed"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 9,
    "metadata": {},
    "outputs": [],
    "source": [
     "file=open(\"data/testfile.txt\",\"w\")\n",
     "file.write(\"Hello world\\n\")\n",
     "file.write(\"another line.\")\n",
     "file.close()"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 10,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "Hello world\n",
       "another line.\n"
      ]
     }
    ],
    "source": [
     "file=open(\"data/testfile.txt\",\"r\")\n",
     "text=file.read()\n",
     "print(text)\n",
     "file.close()"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 15,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "pi's value is 3.141592\n"
      ]
     }
    ],
    "source": [
     "pi=3.141592\n",
     "file=open(\"data/math.txt\",\"w\")\n",
     "file.write(\"pi's value is \"+str(pi))\n",
     "file.close()\n",
     "file=open(\"data/math.txt\",\"r\")\n",
     "text=file.read()\n",
     "print(text)\n",
     "file.close()"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 16,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "[[  2.    2.  199.5]\n",
       " [  3.    3.  199.4]\n",
       " [  4.    4.  198.9]\n",
       " [  5.    5.  199. ]\n",
       " [  6.    6.  200.2]\n",
       " [  7.    7.  198.6]\n",
       " [  8.    8.  200. ]\n",
       " [  9.    9.  200.3]\n",
       " [ 10.   10.  201.2]\n",
       " [ 11.   11.  201.6]\n",
       " [ 12.   12.  201.5]\n",
       " [ 13.   13.  201.5]\n",
       " [ 14.   14.  203.5]\n",
       " [ 15.   15.  204.9]\n",
       " [ 16.   16.  207.1]\n",
       " [ 17.   17.  210.5]\n",
       " [ 18.   18.  210.5]\n",
       " [ 19.   19.  209.8]\n",
       " [ 20.   20.  208.8]\n",
       " [ 21.   21.  209.5]\n",
       " [ 22.   22.  213.2]\n",
       " [ 23.   23.  213.7]\n",
       " [ 24.   24.  215.1]\n",
       " [ 25.   25.  218.7]\n",
       " [ 26.   26.  219.8]\n",
       " [ 27.   27.  220.5]\n",
       " [ 28.   28.  223.8]\n",
       " [ 29.   29.  222.8]\n",
       " [ 30.   30.  223.8]\n",
       " [ 31.   31.  221.7]\n",
       " [ 32.   32.  222.3]\n",
       " [ 33.   33.  220.8]\n",
       " [ 34.   34.  219.4]\n",
       " [ 35.   35.  220.1]\n",
       " [ 36.   36.  220.6]\n",
       " [ 37.   37.  218.9]\n",
       " [ 38.   38.  217.8]\n",
       " [ 39.   39.  217.7]\n",
       " [ 40.   40.  215. ]]\n"
      ]
     }
    ],
    "source": [
     "import numpy as np\n",
     "data=np.loadtxt(\"data/BJsales.txt\",skiprows=2,delimiter=\"\\t\")\n",
     "print(data)"
    ]
   },
   {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
     "**pandas.read_csv()**\n",
     "\n",
     "functions also includes \n",
     "\n",
     "read_excel,read_stata,read_json,read_html,read_sas......"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 23,
    "metadata": {},
    "outputs": [
     {
      "data": {
       "text/html": [
        "<div>\n",
        "<style scoped>\n",
        "    .dataframe tbody tr th:only-of-type {\n",
        "        vertical-align: middle;\n",
        "    }\n",
        "\n",
        "    .dataframe tbody tr th {\n",
        "        vertical-align: top;\n",
        "    }\n",
        "\n",
        "    .dataframe thead th {\n",
        "        text-align: right;\n",
        "    }\n",
        "</style>\n",
        "<table border=\"1\" class=\"dataframe\">\n",
        "  <thead>\n",
        "    <tr style=\"text-align: right;\">\n",
        "      <th></th>\n",
        "      <th>0</th>\n",
        "      <th>1</th>\n",
        "      <th>2</th>\n",
        "    </tr>\n",
        "  </thead>\n",
        "  <tbody>\n",
        "    <tr>\n",
        "      <th>0</th>\n",
        "      <td>1</td>\n",
        "      <td>1</td>\n",
        "      <td>200.1</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>1</th>\n",
        "      <td>2</td>\n",
        "      <td>2</td>\n",
        "      <td>199.5</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>2</th>\n",
        "      <td>3</td>\n",
        "      <td>3</td>\n",
        "      <td>199.4</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>3</th>\n",
        "      <td>4</td>\n",
        "      <td>4</td>\n",
        "      <td>198.9</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>4</th>\n",
        "      <td>5</td>\n",
        "      <td>5</td>\n",
        "      <td>199.0</td>\n",
        "    </tr>\n",
        "  </tbody>\n",
        "</table>\n",
        "</div>"
       ],
       "text/plain": [
        "   0  1      2\n",
        "0  1  1  200.1\n",
        "1  2  2  199.5\n",
        "2  3  3  199.4\n",
        "3  4  4  198.9\n",
        "4  5  5  199.0"
       ]
      },
      "execution_count": 23,
      "metadata": {},
      "output_type": "execute_result"
     }
    ],
    "source": [
     "sales=pd.read_csv('data/BJsales.csv',header=None)\n",
     "sales.head()"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 24,
    "metadata": {},
    "outputs": [
     {
      "data": {
       "text/html": [
        "<div>\n",
        "<style scoped>\n",
        "    .dataframe tbody tr th:only-of-type {\n",
        "        vertical-align: middle;\n",
        "    }\n",
        "\n",
        "    .dataframe tbody tr th {\n",
        "        vertical-align: top;\n",
        "    }\n",
        "\n",
        "    .dataframe thead th {\n",
        "        text-align: right;\n",
        "    }\n",
        "</style>\n",
        "<table border=\"1\" class=\"dataframe\">\n",
        "  <thead>\n",
        "    <tr style=\"text-align: right;\">\n",
        "      <th></th>\n",
        "      <th>id</th>\n",
        "      <th>time</th>\n",
        "      <th>value</th>\n",
        "    </tr>\n",
        "  </thead>\n",
        "  <tbody>\n",
        "    <tr>\n",
        "      <th>0</th>\n",
        "      <td>1</td>\n",
        "      <td>1</td>\n",
        "      <td>200.1</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>1</th>\n",
        "      <td>2</td>\n",
        "      <td>2</td>\n",
        "      <td>199.5</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>2</th>\n",
        "      <td>3</td>\n",
        "      <td>3</td>\n",
        "      <td>199.4</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>3</th>\n",
        "      <td>4</td>\n",
        "      <td>4</td>\n",
        "      <td>198.9</td>\n",
        "    </tr>\n",
        "    <tr>\n",
        "      <th>4</th>\n",
        "      <td>5</td>\n",
        "      <td>5</td>\n",
        "      <td>199.0</td>\n",
        "    </tr>\n",
        "  </tbody>\n",
        "</table>\n",
        "</div>"
       ],
       "text/plain": [
        "   id  time  value\n",
        "0   1     1  200.1\n",
        "1   2     2  199.5\n",
        "2   3     3  199.4\n",
        "3   4     4  198.9\n",
        "4   5     5  199.0"
       ]
      },
      "execution_count": 24,
      "metadata": {},
      "output_type": "execute_result"
     }
    ],
    "source": [
     "sales=pd.read_csv('data/BJsales.csv',names=[\"id\",'time','value'])\n",
     "sales.head()"
    ]
   },
   {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
     "Reading **Excle** file using **pandas**"
    ]
   },
   {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
     "Reading **pdf** file using **PyPDF2**"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 33,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "Collecting PyPDF2\n",
       "  Using cached PyPDF2-1.26.0.tar.gz (77 kB)\n",
       "Building wheels for collected packages: PyPDF2\n",
       "  Building wheel for PyPDF2 (setup.py): started\n",
       "  Building wheel for PyPDF2 (setup.py): finished with status 'done'\n",
       "  Created wheel for PyPDF2: filename=PyPDF2-1.26.0-py3-none-any.whl size=61087 sha256=56af7a06394f0ed756f04b9089c63a7d4c030678395e109ae5afd9cd6f9d39c1\n",
       "  Stored in directory: c:\\users\\der\\appdata\\local\\pip\\cache\\wheels\\80\\1a\\24\\648467ade3a77ed20f35cfd2badd32134e96dd25ca811e64b3\n",
       "Successfully built PyPDF2\n",
       "Installing collected packages: PyPDF2\n",
       "Successfully installed PyPDF2-1.26.0\n",
       "Note: you may need to restart the kernel to use updated packages.\n"
      ]
     }
    ],
    "source": [
     "pip install PyPDF2"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 6,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "MixedFrequencyDataSamplingRegression\n",
       "Models:the\n",
       "RPackage\n",
       "midasr\n",
       "EricGhysels\n",
       "UniversityofNorthCarolina\n",
       "VirmantasKvedaras\n",
       "VilniusUniversity\n",
       "VaidotasZemlys\n",
       "VilniusUniversity\n",
       "Abstract\n",
       "Regressionmodelsinvolvingdatasampledatdi\n",
       "!\n",
       "erentfrequenciesareofgeneralin-\n",
       "terest.Inthisdocumentthe\n",
       "Rpackage\n",
       "midasr\n",
       "isdescribedwithinaMIDASregression\n",
       "frameworkwithfunctionalconstraintsonparametersputforwardinworkby\n",
       "Ghysels,\n",
       "Santa-Clara,andValkanov\n",
       "(2002),Ghysels,Santa-Clara,andValkanov\n",
       "(2006a)and\n",
       "An-\n",
       "dreou,Ghysels,andKourtellos\n",
       "(2010).Keywords\n",
       ":MIDAS,speciÞcationtest.\n",
       "1.Introduction\n",
       "Regressionmodelsinvolvingdatasampledatdi\n",
       "!\n",
       "erentfrequenciesareofgeneralinterest.In\n",
       "thisdocumentweintroducea\n",
       "Rpackage\n",
       "midasr\n",
       "fortheregressionmodelingwiththemixed\n",
       "frequencydatabasedonaframeworkputforwardinrecentworkby\n",
       "Ghysels\n",
       "etal.\n",
       "(2002),Ghysels\n",
       "etal.\n",
       "(2006a)and\n",
       "Andreou\n",
       "etal.\n",
       "(2010)usingsocalledMIDAS,meaningMi(xed)\n",
       "Da(ta)S(ampling),regressions.\n",
       "1Inageneralframeworkofregressionswithfunctionalconstraintsonparameters,the\n",
       "midasr\n",
       "packagenotonlyprovidessimilarfunctionalitywithinastandard\n",
       "Rframeworkofthemodel\n",
       "speciÞcationcomparabletothatavailableintheusualfunctions\n",
       "lmornls,butalsodeals\n",
       "withanextendedmodelspeciÞcationanalysisforMIDASregressions.\n",
       "SeveralrecentsurveysonthetopicofMIDASareworthmentioningattheoutset.They\n",
       "are:\n",
       "Andreou,Ghysels,andKourtellos\n",
       "(2011)whoreviewmoreextensivelysomeofthema-\n",
       "terialsummarizedinthisdocument,\n",
       "Armesto,Engemann,andOwyang\n",
       "(2010)whoprovidea\n",
       "verysimpleintroductiontoMIDASregressionsandÞnally\n",
       "GhyselsandValkanov\n",
       "(2012)who\n",
       "discussvolatilitymodelsandmixeddatasampling.\n",
       "EconometricanalysisofMIDASregressionsappearsin\n",
       "Ghysels,Sinko,andValkanov\n",
       "(2006b),Andreou\n",
       "etal.\n",
       "(2010),Bai,Ghysels,andWright\n",
       "(2012),KvedarasandRaÿckauskas\n",
       "(2010),RodriguezandPuggioni\n",
       "(2010),Wohlrabe\n",
       "(2009),amongothers.\n",
       "MIDASregressioncanalsobeviewedasareducedformrepresentationofthelinearprojection\n",
       "whichemergesfromastatespacemodelapproach-byreducedformwemeanthattheMIDAS\n",
       "regressiondoesnotrequirethespeciÞcationofafullstatespacesystemofequations.\n",
       "Bai\n",
       "etal.\n",
       "(2012)showthatinsomecasestheMIDASregressionisanexactrepresentationoftheKalman\n",
       "1Ghysels\n",
       "(2013)alsodevelopedapackagefor\n",
       "MATLAB\n",
       "whichdealswiththeestimationandinformation\n",
       "criteria-basedspeciÞcationofMIDASregressionsaswellasforecastingandnowcastingofslowfrequencyseries.\n",
       "\n"
      ]
     }
    ],
    "source": [
     "import PyPDF2\n",
     "file=open('data/midasr.pdf','rb')\n",
     "reader=PyPDF2.PdfFileReader(file)\n",
     "reader.numPages\n",
     "pageobj=reader.getPage(0)\n",
     "print(pageobj.extractText())\n",
     "file.close()"
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
    "version": "3.7.6"
   }
  },
  "nbformat": 4,
  "nbformat_minor": 4
 }