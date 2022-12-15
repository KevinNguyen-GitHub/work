#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <algorithm>
#include <regex>
using namespace std;

vector<string> duplicateWord(string str);

void removePunctuations(string& s)
{
    string punctuations = ".!?";

    auto pos = s.find_first_of(punctuations);

    while (pos != string::npos)
    {
        s.erase(pos, 1);

        pos = s.find_first_of(punctuations);
    }
}


void removeQuotes(string& s)
{
	s.erase(remove(s.begin(), s.end(), '\"'), s.end());
}

char toLower(char c)
{
	return tolower(c);
}

string convertLower(string s)
{
	transform(s.begin(), s.end(), s.begin(), toLower) ;
	return s;
}

bool checkAlpha(unsigned char ch)
{
    return !std::isalnum(ch) && ch != '-' && ch != '\'';
}


bool validWord(string& s)
{
    s.erase(std::remove_if(s.begin(), s.end(), checkAlpha), s.end());
    return !s.empty() && std::isalpha(s[0]);
}


void populate(string filepath, vector<string>& out)
{
    // Use std::ifstream to read the input file
    std::ifstream file(filepath);

    // Check if the file was successfully opened
    if (file.is_open())
    {
        // Read each line from the file
        std::string line;
        while (std::getline(file, line))
        {
            // Use duplicateWord to find all duplicate words in the line
            vector<string> w = duplicateWord(line);

            // Add the duplicate words to the output vector
            out.insert(out.end(), w.begin(), w.end());
        }

        // Close the file
        file.close();
    }
    else
    {
        // Print an error message if the file could not be opened
        std::cout << "Error: Could not open file " << filepath << std::endl;
    }
}


vector<string> duplicateWord(string str)
{
    // Create a vector to hold the duplicate words
    vector<string> out;

    // Use std::stringstream to extract words from the input string
    std::stringstream ss(str);

    // Read each word from the stringstream
    std::string word;
    while (ss >> word)
    {
        // Check if the word is valid and add it to the output vector
        if (validWord(word))
        {
            out.push_back(word);
        }
    }

    return out;
}

int main(int argc, char** argv)
{
    // Check if the correct number of arguments were provided
    if (argc < 3)
    {
        std::cout << "Please include input filename and output filename in param list.\n";
        std::cout << "Example:\n";
        std::cout << "     % spellchecker american-english.txt flatland.txt\n";
        return 0;
    }

    // Get the file paths from the command line arguments
    string dictionary = argv[1];
    string txt = argv[2];

    // Create vectors to hold the words from the dictionary and input file
    vector<string> dict;
    vector<string> file;

    // Populate the vectors with words from the dictionary and input file
    populate(dictionary, dict);
    populate(txt, file);

    // Create a map to hold the misspelled words and their frequencies
    std::map<string, int> misspelledWords;

    // Loop through the words from the input file
    for (const string& word : file)
    {
        // Convert the word to lowercase and check if it is not in the dictionary
        string lowercaseWord = convertLower(word);
        if (std::find(dict.begin(), dict.end(), lowercaseWord) == dict.end())
        {
            // Check if the word is already in the map
            auto it = misspelledWords.find(lowercaseWord);
            if (it == misspelledWords.end())
            {
                // Add the word to the map with a frequency of 1
                misspelledWords.insert({lowercaseWord, 1});
            }
            else
            {
                // Increment the frequency of the word in the map
                misspelledWords[lowercaseWord] = it->second + 1;
            }
        }
    }

    // Print the number of misspelled words
    std::cout << "Misspelled words: " << misspelledWords.size() << std::endl;

    // Print the misspelled words and their frequencies
    for (const auto& [word, frequency] : misspelledWords)
    {
        std::cout << word << " - " << frequency << std::endl;
    }

    return 0;
}
