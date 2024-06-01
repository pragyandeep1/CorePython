import abc
import re
matcher=re.finditer("a","a7b@k9z")
for match in matcher:
 print(match.start(),"......",match.group())
 x = [abc]