email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")

# check for "." in email as well
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
  
  # modified 
  email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")

# check for ".edu"
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
  # using "re.search"
import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

# using special symbols
import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
  
  # modified 
import re

email = input("What's your email? ").strip()

if re.search(".+@.+.edu", email):
    print("Valid")
else:
    print("Invalid")

# modified further 
import re

email = input("What's your email? ").strip()

if re.search(".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

# "r" for raw string 
import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

# adding ^ and $
import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# adding [] and [^]
import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
  # adding "[a-zA-Z0-9_]"
import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_].+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

#replace "[a-zA-Z0-9_]" with "\w"
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
  
# add alternate email endings
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
  
# added re.IGNORECASE
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
  # modified 
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")





  
  
