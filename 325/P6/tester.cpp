#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <algorithm>
#include <regex>
using namespace std;

vector<string> duplicateWord(string str);

void removePunctiations(string& s)
{
	string out = "";
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

char toLower(char c)
{
	return std::tolower(c);
}

string convertLower(string s)
{
	std::transform(s.begin(), s.end(), s.begin(), toLower) ;
	return s;
}

bool check_alpha(unsigned char ch)
{	 
	bool bRes = isalpha(ch) || ch == '-' || ch == '\'';
	return !bRes;
}

bool validWord(string& s)
{
	removePunctiations(s);
	removeQuotes(s);

	bool bValid = false;

	if(find_if(s.begin(), s.end(), check_alpha) == s.end())
		bValid = true;
		
		if (isalpha(s[0]) == false)
			bValid = false;
	return bValid;
}

void populate(string filepath, vector<string>& out)
{
	fstream newFile;
	string line;
	int i = 0;

	newFile.open(filepath, ios::in);
	if (!newFile)
		cout << "No such file";
	else {
		char ch;
		while (!newFile.eof())
		{
			getline(newFile, line);
			vector<string> w = duplicateWord(line);
			out.insert(out.end(), w.begin(), w.end());
			i++;
		}
	}
	newFile.close();
}

vector<string> duplicateWord(string str)
{
	vector<string> out;
	string word = "";
	for (auto x : str)
	{
		if (x == ' ')
		{
			if (validWord(word))
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

	if (validWord(word))
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

    vector<string> dict;
    vector<string> file;

	populate(dictionary, dict);
	populate(txt, file);

	map<string, int> misspelledWords;
	for (string word : file)
	{
		word = convertLower(word);
		if (find(dict.begin(), dict.end(), word) == dict.end())
		{
			map<string, int>::iterator it = misspelledWords.find(word);
			if (it == misspelledWords.end())
			{
				misspelledWords.insert(std::pair<string,int>(word,1));
			}
			else
			{
				misspelledWords[word] = it->second + 1;
			}
		}
	}

	cout << "Misspelled words:" << misspelledWords.size() << endl;
	for (map<string, int>::iterator it = misspelledWords.begin(); it != misspelledWords.end(); it++)
	{
		cout << it->first << " - " << it->second << endl;
	}
}
