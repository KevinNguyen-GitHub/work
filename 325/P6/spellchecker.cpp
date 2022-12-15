#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <algorithm>
#include <regex>

using namespace std;
vector<string> removeDupWord(string str);
void remove_punctuation(string& s)
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
void remove_captization()
{

}
void remove_double_quotes(string& s)
{
	s.erase(remove(s.begin(), s.end(), '\"'), s.end());
}
char to_lower(char c)
{
	return std::tolower(c);
}
string convert_to_lower(string s)
{
	std::transform(s.begin(), s.end(), s.begin(), to_lower) ;
	return s;
}
bool check_alpha(unsigned char ch)
{	 
	bool bRes = isalpha(ch) || ch == '-' || ch == '\'';
	return !bRes;
}
bool is_word_valid(string& s)
{
	/*
	 1. A proper word must have at least one letter (use the 26 letters in the English alphabet) and may contain 
	 a hyphen or an apostrophe. No other characters are allowed.

	 2. A word must start with a letter, and it can contain one or more hyphens (multi-thread), and it can have 
	zero or one apostrophe (don’t)
	3. Capitalization is ignored (fred is the same as Fred)
	4. Punctuation is ignored (! ? )
	5. Double quotes are ignored (“hammer” is the same as hammer)
*/
	//Punctuation is ignored (! ? )
	remove_punctuation(s);

	//Double quotes are ignored(“hammer” is the same as hammer)
	remove_double_quotes(s);


	bool bValid = false;

	if(find_if(s.begin(), s.end(), check_alpha) == s.end())
		bValid = true;
		
	//A word must start with a letter
		if (isalpha(s[0]) == false)
			bValid = false;
	return bValid;
}
void populate_word_list(string filepath,vector<string>& out)
{
	fstream new_file;
	std::string line;
	int i = 0;

	//if (filepath == "")
	//{
	//	//dummy data insertion in case of online compiler.
	//	// todo it should be removed later.

	//	for (int i = 0; i < COUNT; i++)
	//	{
	//		arr[i] = (rand() % (MAX_VAL - MIN_VAL + 1) + MIN_VAL);
	//	}
	//	return;
	//}

	new_file.open(filepath, ios::in);
	if (!new_file)
		cout << "No such file";
	else {
		char ch;
		while (!new_file.eof())
		{
			getline(new_file, line);
			vector<string> w = removeDupWord(line);
			out.insert(out.end(), w.begin(), w.end());
			i++;
		}
	}
	new_file.close();
}

vector<string> removeDupWord(string str)
{
	vector<string> out;
	string word = "";
	for (auto x : str)
	{
		if (x == ' ')
		{
			//cout << word << endl;
			if (is_word_valid(word))
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
	//cout << word << endl;
	if (is_word_valid(word))
		out.push_back(word);

	return out;
}
int main(int argc, char** argv)
{
    if (argc < 3)
    {
        cout << "Error :invalid arguments are passed" << endl;
        return -1;
    }


    string dict_file_name = argv[1];
    string txt_file_name = argv[2];

    vector<string> word_dict;
    vector<string> word_file;


	convert_to_lower("Wood");
	populate_word_list(dict_file_name, word_dict);
	populate_word_list(txt_file_name, word_file);
	//cout << "**********************" << endl;
	map<string, int> mis_spelled_words;
	for (string word : word_file)
	{
		word = convert_to_lower(word);
		if (find(word_dict.begin(), word_dict.end(), word) == word_dict.end())
		{
			map<string, int>::iterator it = mis_spelled_words.find(word);
			if (it == mis_spelled_words.end())
			{
				mis_spelled_words.insert(std::pair<string,int>(word,1));
			}
			else
			{
				mis_spelled_words[word] = it->second + 1;
			}
		}
	}

	cout << "Misspelled words:" << mis_spelled_words.size() << endl;
	for (map<string, int>::iterator it = mis_spelled_words.begin(); it != mis_spelled_words.end(); it++)
	{
		cout << it->first << " - " << it->second << endl;
	}


}