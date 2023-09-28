import string
import enchant


# Define the substitution cipher
cipher_text = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
cipher_text = cipher_text.replace(" ","")
alphabet = string.ascii_lowercase


# Define a function to decrypt the cipher text using a given key
def decrypt(cipher_text, key):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            index = key.index(letter)
            plain_text += alphabet[index]
        else:
            plain_text += letter
    return plain_text

# Define a function to analyze the frequency of letters in the ciphertext
def analyze_frequency(cipher_text):
    frequencies = {}
    for letter in cipher_text:
        if letter in alphabet:
            if letter not in frequencies:
                frequencies[letter] = 0
            frequencies[letter] += 1
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequencies

# Analyze the frequency of letters in the ciphertext
sorted_frequencies = analyze_frequency(cipher_text)
most_frequent_letters = [x[0] for x in sorted_frequencies]

# Try all possible keys using the most frequent letters as a starting point
for first_letter in most_frequent_letters:
    index = alphabet.index(first_letter)
    key = alphabet[index:] + alphabet[:index]
    plain_text = decrypt(cipher_text, key)
    print(f"Key = {key}: {plain_text}")
