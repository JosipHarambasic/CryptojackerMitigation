from Parser import Parser

parser = Parser("whitelist.txt", "nethogs.txt")
print(parser.parse())
