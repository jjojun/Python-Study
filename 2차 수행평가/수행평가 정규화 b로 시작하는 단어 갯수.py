import re

sentence = "butterflies are beautiful creatures, but bees are important too."
count = len(re.findall(r'\bb\w+', sentence, re.IGNORECASE))

print(count)
