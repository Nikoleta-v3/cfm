import doctest
import os
import unittest
import matplotlib

matplotlib.use('Agg')

directories = ["./_labsheets", "./_handouts"]

def load_tests(loader, tests, ignore):
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for f in files:
                if f.endswith(".md"):
                     tests.addTests(doctest.DocFileSuite(os.path.join(root, f),
                                                      optionflags=doctest.ELLIPSIS))

    return tests


def clean_up():
    try:
        os.remove("my_plot.pdf")
    except FileNotFoundError:
        pass


def main():
    unittest.main()
    clean_up()


if __name__ == '__main__':
    main()
