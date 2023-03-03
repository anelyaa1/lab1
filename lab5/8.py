import re
text = "PythonLabs"
print(re.findall('[A-Z][^A-Z]*', text))

#['Python', 'Labs']