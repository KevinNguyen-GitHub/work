#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <algorithm>
#include <regex>

using namespace std;

vector<string> duplicateWord(string str);

char toLower(char c)
{
	return tolower(c);
}

string convertLower(string s)
{
	std::transform(s.begin(), s.end(), s.begin(), toLower) ;
	return s;
}

void removePunctiation(string& s)
{
	string out = " ";
	for (auto& c : s)
	{
		bool bPunc = (c == '.' || c == '!' || c == '?' || c == ',');
		if (!bPunc)
			out += c;
	}
	s = out;
}

void removeQuotes(string& s)
{
	s.erase(remove(s.begin(), s.end(), '\"'), s.end());
}

bool checkAlpha(unsigned char ch)
{	 
	bool alpha = isalpha(ch) || ch == '-' || ch == '\'';
	return !alpha;
}

bool checkValid(string& s)
{
	removePunctiation(s);
	removeQuote(s);

	bool valid = false;

	if(find_if(s.begin(), s.end(), checkAlpha) == s.end())
		valid = true;
		
		if (isalpha(s[0]) == false)
			valid = false;

	return valid;
}

void populate(string filepath, vector<string>& out)
{
	fstream file;
	std::string line;
	int i = 0;
	
	file.open(filepath, ios::in);
	if (!file)
		cout << "No such file";
	else {
		char ch;
		while (!file.eof())
		{
			getline(file, line);
			vector<string> w = duplicateWord(line);
			out.insert(out.end(), w.begin(), w.end());
			i++;
		}
	}
	file.close();
}

vector<string> duplicateWord(string str)
{
	vector<string> out;
	string word = "";
	for (auto x : str)
	{
		if (x == ' ')
		{
			//cout << word << endl;
			if (checkValid(word))
			{
				out.push_back(word);
				word = "";
			}
			else
			{
				int i = 10;
				word = "";
			}
		}
		else {
			word = word + x;
		}
	}

	if (checkValid(word))
		out.push_back(word);

	return out;
}
int main(int argc, char** argv)
{
    if (argc < 3)
    {
        cout << "Please include input filename and output filename in param list.\n";
		cout << "Example:\n";
		cout << "     % spellchecker american-english.txt flatland.txt\n";
		exit(EXIT_SUCCESS);
    }


    string dictionary = argv[1];
    string txt = argv[2];

    vector<string> word_dict;
    vector<string> word_file;


	convertLower("Wood");
	populate(dictionary, word_dict);
	populate(txt, word_file);

	map<string, int> misspelledWord;
	for (string word : word_file)
	{
		word = convertLower(word);
		if (find(word_dict.begin(), word_dict.end(), word) == word_dict.end())
		{
			map<string, int>::iterator it = misspelledWord.find(word);
			if (it == misspelledWord.end())
			{
				misspelledWord.insert(std::pair<string,int>(word,1));
			}
			else
			{
				misspelledWord[word] = it->second + 1;
			}
		}
	}

	cout << "Misspelled words:" << misspelledWord.size() << endl;
	for (map<string, int>::iterator it = misspelledWord.begin(); it != misspelledWord.end(); it++)
	{
		cout << it->first << " - " << it->second << endl;
	}
}