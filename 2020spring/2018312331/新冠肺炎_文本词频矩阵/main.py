from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import jieba


def main():
    df = pd.read_csv('新冠文本.csv', encoding='utf-8')
    df = df.dropna(how='any')
    df = df.drop_duplicates(subset=['url'])
    words = [' '.join(jieba.lcut(sentence)) for sentence in df['content'].values]
    vectorizer = CountVectorizer()
    result = vectorizer.fit_transform(words)
    print(pd.DataFrame(result.toarray(), columns=vectorizer.get_feature_names()))


if __name__ == '__main__':
    main()
