from mikrotikrscparser.rscparser import RscParser

with open('01_parse_example.rsc', 'r') as file:
    rsc_file_content = file.read()

rscParser = RscParser()
statements = rscParser.parse(rsc_file_content)

