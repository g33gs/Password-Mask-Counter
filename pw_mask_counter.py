from collections import Counter

def main():
    passwords_file = open('/path/to/password/list.txt') #For Windows paths, make sure to escape the first slash (i.e., C:\\Users\\H@cker\\Desktop\\Password.txt)
    passwords = [x.strip() for x in passwords_file.readlines()]
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = [x.upper() for x in lower]
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def split(word):
            return [char for char in word]

    def converter(password):
            broken_password = split(password)
            converted_splitword = []

            for p in range(0, len(password)):
                if broken_password[p] in lower:
                    converted_splitword.append("?l")

                elif broken_password[p] in upper:
                    converted_splitword.append("?u")

                elif broken_password[p] in digits:
                    converted_splitword.append("?d")
                
                else:
                    converted_splitword.append("?s")

            return converted_splitword

    def wordlistappender(wordfile):
            converted_wordlist = []
            for word in wordfile:
                new_word = converter(word)
                converted_wordlist.append(''.join(new_word))

            return converted_wordlist

    def topmasks(sample_file):
            master = wordlistappender(sample_file)
            count = Counter(master)
            answer1 = count.most_common()[0]
            answer2 = count.most_common()[1]
            answer3 = count.most_common()[2]
            print("Top 3 Password Masks")
            print("--------------------")
            print("1. %s : %s" % (answer1))
            print("2. %s : %s" % (answer2))
            print("3. %s : %s" % (answer3))
            
            

    topmasks(passwords)

main()