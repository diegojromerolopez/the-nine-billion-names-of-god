# the-nine-billion-names-of-god
Experiment inspired by the short story
"[The Nine Billion Names of God](https://urbigenous.net/library/nine_billion_names_of_god.html)"
by Arthur C. Clarke.

# Rationale
In the short story "The Nine Billion Names of God" by
[Arthur C. Clarke](https://en.wikipedia.org/wiki/Arthur_C._Clarke), the idea of a project
is presented to us, the readers: some Tibetan monks want to use a computer to write all
the names of God. Their aim is to write all the names of God. Once they achieve their objective,
the Universe will come to an end.

This repository makes the project easier, by providing a script that creates strings of size 9
of all possible combinations of legal IPA symbols and writes them to a file. In the story the
monks had their own alphabet, but I chose IPA as it represents all sounds of human languages.

# Usage
Run with no arguments and a file **god_names.txt** will appear with a God name per line.
```
python3 main.py 
```

# Why I did this?
No reason, must a poet have a reason to write a poem?

Run this script and maybe the Universe will end when the last name of God is written.

# Dependencies
* [panphon](https://github.com/dmort27/panphon)

# License and copyright notice
This project is a work of art. The Arthur C. Clarke estate does not
endorse, promote, help or has any relationship with this project.

This project is a homage to Arthur C. Clarke.

**validate_ipa.py** and **ipa_all.csv** files have been
copied from [panphon](https://github.com/dmort27/panphon)
project. Both projects have the same license.

This code has [MIT](LICENSE) license.
