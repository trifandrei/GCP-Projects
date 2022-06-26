def count_words():
        sentence = input("Enter your sentance: ")
        if not sentence:
          print("No input provided")
        else:
            word_list = sentence.split()
            c=0
            for i in word_list:
                if '\\n' not in i:
                    c=c+1
                else:
                    if i=='\\n':
                        break
                    else:
                        c=c+1
                        break

            print("Nr. of words is :",c)

count_words()