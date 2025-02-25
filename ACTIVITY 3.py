def frequency_counter(sentence):
    words = sentence.split(" ")

    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    print("Word frequency: ")
    
    for key, value in frequency_dict.items():
        print(f"{key}:{value}")

def main():
    sentence = frequency_counter(input("Enter a sentence: "). lower())

main()
   