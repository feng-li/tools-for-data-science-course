#include <cstdlib>
#include "dictionary.h"
#include <vector>
#include <iomanip>
#include <map>

const int MaxWordLength = 10;	//最大词长为10个字节（即5个汉字）
const char Separator = '/';	//词界标记

Dictionary word_dict;		//初始化一个词典


/*
 * 函数功能：对字符串用最大匹配算法（正向）处理
 * 函数输入：汉字字符串
 * 函数输出：分好词的字符串
 */
string SegmentSentence_1(string s1) {
	string s2 = "";		//用s2存放分词结果

	while (!s1.empty()) {
		int len = s1.length();	//取输入串长度
		if (len > MaxWordLength) {
			len = MaxWordLength;	//只在最大词长范围内进行处理
		}

		string w = s1.substr(0, len);
		int n = word_dict.findWord(w);	//在词典中查找相应的词
		while (len > 2 && n == 0) {
			len -= 2;	//从候选词右边减掉一个汉字，将剩下的部分作为候选词
			w = s1.substr(0, len);
			n = word_dict.findWord(w);
		}

		s2 = s2 + w + Separator;
		s1 = s1.substr(w.length(), s1.length() - w.length());
	}

	return s2;
}


/*
 * 函数功能：对字符串用最大匹配算法（逆向）处理
 * 函数输入：汉字字符串
 * 函数输出：分好词的字符串
 */
string SegmentSentence_2(string s1) {
	string s2 = "";		//用s2存放分词结果

	while (!s1.empty()) {
		int len = s1.length();	//取输入串长度
		if (len > MaxWordLength) {
			len = MaxWordLength;	//只在最大词长范围内进行处理
		}

		string w = s1.substr(s1.length() - len, len);
		int n = word_dict.findWord(w);	//在词典中查找相应的词
		while (len > 2 && n == 0) {
			len -= 2;	//从候选词左边减掉一个汉字，将剩下的部分作为候选词
			w = s1.substr(s1.length() - len, len);
			n = word_dict.findWord(w);
		}

		w = w + Separator;
		s2 = w + s2;
		s1 = s1.substr(0, s1.length() - len);
	}

	return s2;
}


/*
 * 函数功能：对句子进行最大匹配法处理，包含对特殊字符的处理
 * 函数输入：1.含有汉字、英文符号的字符串
 *         2.flag=1调用正向最大匹配算法，flag=2调用逆向最大匹配算法
 * 函数输出：分好词的字符串
 */
string SegmentSentenceMM(string s1, int flag) {
	string s2 = "";	//用s2存放分词结果
	int i;
	int dd;
	while (!s1.empty()) {
		unsigned char ch = (unsigned char)s1[0];
		if (ch < 128) {
			//处理西文字符
			i = 1;
			dd = s1.length();

			while (i < dd && ((unsigned char)s1[i] < 128) && (s1[i] != 10) && (s1[i] != 13)) {
				//s1[i]不能是换行符或回车符
				i++;
			}//中止循环条件：出现中文字符、换行或者回车

			if (i == 1 && (ch == 10 || ch == 13)) {
				//如果是换行或回车符，将它拷贝给s2输出
				s2 += s1.substr(0, i);
			}
			else {
				s2 += s1.substr(0, i) + Separator;
			}

			s1 = s1.substr(i, dd);
			continue;
		}
		else {
			if (ch < 176) {
				//中文标点等非汉字字符
				i = 0;
				dd = s1.length();

				//获取中文双字节特殊字符（非汉字、非中文标点），中止循环条件：超过长度、出现中文标点符号、出现汉字
				while (i < dd && ((unsigned char)s1[i] < 176) && ((unsigned char)s1[i] >= 161)
					&& (!((unsigned char)s1[i] == 161 && ((unsigned char)s1[i + 1] >= 162 && (unsigned char)s1[i + 1] <= 168)))
					&& (!((unsigned char)s1[i] == 161 && ((unsigned char)s1[i + 1] >= 171 && (unsigned char)s1[i + 1] <= 191)))
					&& (!((unsigned char)s1[i] == 163 && ((unsigned char)s1[i + 1] == 161 || (unsigned char)s1[i + 1] == 168
						|| (unsigned char)s1[i + 1] == 169 || (unsigned char)s1[i + 1] == 172 || (unsigned char)s1[i + 1] == 186
						|| (unsigned char)s1[i + 1] == 187 || (unsigned char)s1[i + 1] == 191)))) {
					//假定没有半个汉字
					i = i + 2;
				}

				//出现中文标点
				if (i == 0) {
					i = i + 2;
				}

				//中文标点每个加一个分词标记；其他非汉字双字节字符连续输出，只加一个分词标记
				s2 += s1.substr(0, i) + Separator;


				s1 = s1.substr(i, dd);
				continue;
			}
		}

		//以下处理汉字串
		i = 2;
		dd = s1.length();
		while (i < dd && (unsigned char)s1[i] >= 176) {
			i += 2;
		}

		if (flag == 1) {
			//调用正向最大匹配
			s2 += SegmentSentence_1(s1.substr(0, i));
		}
		else {
			//调用逆向最大匹配
			s2 += SegmentSentence_2(s1.substr(0, i));
		}

		s1 = s1.substr(i, dd);
	}

	return s2;
}


/*
 * 函数功能：删除分词标记（即去掉字符串中的/）
 * 函数输入：含有分词标记的字符串
 * 函数输出：不含分词标记的字符串
 */
string removeSeparator(string str_in) {
	char s[10000];
	int j = 0;
	for (int i = 0; i < str_in.length(); i++) {
		if (!(str_in[i] == '/')) {
			s[j] = str_in[i];
			j++;
		}
	}
	s[j] = '\0';
	string str_out = s;
	return str_out;
}


/*
 * 函数功能：计算切分标记的位置
 * 函数输入：1.strline_in未进行切分的汉字字符串
		   2.strline_right进行切分后的汉字字符串
 * 函数输出：vecetor，其中存放了strline_in中哪些位置放置了分词标记
 *         注意：vector中不包含最后标记的位置，但是包含位置0。
 */
vector<int> getPos(string strline_right, string strline_in) {
	int pos_1 = 0;
	int pos_2 = -1;
	int pos_3 = 0;
	string word = "";
	vector<int> vec;

	int length = strline_right.length();
	while (pos_2 < length) {
		//前面的分词标记
		pos_1 = pos_2;

		//后面的分词标记
		pos_2 = strline_right.find('/', pos_1 + 1);

		if (pos_2 > pos_1) {
			//将两个分词标记之间的单词取出
			word = strline_right.substr(pos_1 + 1, pos_2 - pos_1 - 1);
			//根据单词去输入序列中查出出现的位置
			pos_3 = strline_in.find(word, pos_3);
			//将位置存入数组
			vec.push_back(pos_3);
			pos_3 = pos_3 + word.size();
		}
		else {
			break;
		}
	}

	return vec;
}



int main(int argc, char* argv[]) {

	string strline_right;	//输入语料：用作标准分词结果
	string strline_in;	//去掉分词标记的语料（用作分词的输入）
	string strline_out_1;	//正向最大匹配分词完毕的语料
	string strline_out_2;	//逆向最大匹配分词完毕的语料

	ifstream fin("test.txt");	//打开输入文件
	//if (!fin) {
	//	cout << "Unable to open input file !" << argv[1] << endl;
	//	exit(-1);
	//}

	ofstream fout("result.txt");	//确定输出文件
	if (!fout) {
		cout << "Unable to open output file !" << endl;
		exit(-1);
	}

	long count = 0;	//句子编号
	long count_right_all = 0;	//准确的切分总数
	long count_out_1_all = 0;	//正向匹配切分总数
	long count_out_2_all = 0;	//逆向匹配切分总数
	long count_out_1_right_all = 0;	//正向匹配切分正确总数
	long count_out_2_right_all = 0;	//逆向匹配切分正确总数

	while (getline(fin, strline_right, '\n')) {
		if (strline_right.length() > 1) {

			//去掉分词标记
			strline_in = removeSeparator(strline_right);

			//正向最大匹配分词
			strline_out_1 = strline_right;
			strline_out_1 = SegmentSentenceMM(strline_in, 1);

			//逆向最大匹配分词
			strline_out_2 = strline_right;
			strline_out_2 = SegmentSentenceMM(strline_in, 2);

			//输出结果
			count++;
			cout << "----------------------------------------------" << endl;
			cout << "句子编号：" << count << endl;
			cout << endl;
			cout << "待分词的句子长度: " << strline_in.length() << "  句子：" << endl;
			cout << strline_in << endl;
			cout << endl;
			cout << "标准比对结果长度: " << strline_right.length() << "  句子：" << endl;
			cout << strline_right << endl;
			cout << endl;
			cout << "正向匹配分词长度: " << strline_out_1.length() << "  句子：" << endl;
			cout << strline_out_1 << endl;
			cout << endl;
			cout << "逆向匹配分词长度: " << strline_out_2.length() << "  句子：" << endl;
			cout << strline_out_2 << endl;
			cout << endl;

		}
	}
	cout << "----------------------------------" << endl;
	cout << endl;
	return 0;
}






























