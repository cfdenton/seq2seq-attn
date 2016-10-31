import sys
import random
import string
import math

def generate_dict(dict_len, min_word_len, max_word_len):
    dictionary = []
    for i in range(dict_len):
        dictionary.append(''.join(random.choice(string.ascii_lowercase) for _ in \
            range(math.floor(random.random()*(max_word_len - min_word_len + 1) + min_word_len))))
    return dictionary

def build_set(dictionary, num_seq, min_sent_len, max_sent_len):
    sequences = []
    for i in range(num_seq):
        int_seq = [random.randint(0, len(dictionary) - 1) for _ in \
            range(random.randrange(min_sent_len, max_sent_len))]
        seq = [dictionary[k] for k in int_seq]
        sequences.append(seq)
    return sequences    

def write(filename, sequences, targ):
    with open(filename, 'w') as f:
        for seq in sequences:
            for word in seq:
                if targ:
                    f.write(word + ' ')
                else:    
                    f.write(word)
            f.write('\n')

def main(arguments):
    dictionary = generate_dict(100, 3, 8)
    sequences = build_set(dictionary, 100, 4, 20)
    write('test_src.out', sequences, False)
    write('test_targ.out', sequences, True)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
