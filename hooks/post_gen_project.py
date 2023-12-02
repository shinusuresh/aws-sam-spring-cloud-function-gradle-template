import os
import shutil

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"


def main():
    directory = '{{ cookiecutter.__package.replace(".","/") }}'
    srcDir = 'src/main/java/' + directory + "/"
    testDir = 'src/test/java/' + directory + "/"

    os.makedirs(srcDir, exist_ok=True)
    os.makedirs(testDir, exist_ok=True)

    srcFiles = os.listdir("_src/main/java")
    for f in srcFiles:
        os.rename("_src/main/java/" + f, srcDir + f)

    testFiles = os.listdir("_src/test/java")
    for f in testFiles:
        os.rename("_src/test/java/" + f, testDir + f)

    # print(INFO + "Configured spring cloud function for project." + TERMINATOR)

    shutil.rmtree("_src", ignore_errors=False)


if __name__ == '__main__':
    main()
