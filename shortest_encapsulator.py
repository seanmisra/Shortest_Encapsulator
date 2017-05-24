import sys


if __name__ == '__main__':
    all_strings = []

    if len(sys.argv) == 1:
        print("No strings entered. You can enter them, space-separated, via the command-line.")
        exit
    else:
        # skip for argument
        iter_args = iter(sys.argv)
        next(iter_args)

        # add all other arguments (strings) to a string list
        for word in iter_args:
            all_strings.append(word)

        # loop through each element in string list (except the last)
        for elem in range (0, len(all_strings) - 1):
            string_length = len(all_strings[elem])

            # check chars in current elem against chars in next elem
            # if duplicates are found, delete them
            for i in range(1, string_length):
                if all_strings[elem][-i:] == all_strings[elem + 1][:i]:
                    all_strings[elem] = all_strings[elem][:-i]

        # combine strings into a final string - output it
        final_string = ""
        for word in all_strings:
            final_string += word

        print(final_string)
