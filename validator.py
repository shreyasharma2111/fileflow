import re

allowedextensions = ['.jpg', '.txt', '.pdf', '.png', '.docx', '.xlsx', '.pptx', '.csv', '.json', ]

def validatefilename(filename):
    #define validating factors (date format, underscore, lowercase and .)
    pattern = r'^\d{4}-\d{2}-\d{2}_[a-z0-9_]+\.[a-z0-9]+$' 
    if not re.match (pattern, filename):
        return False
    
    #extract the file extention from filename
    extension = '.' + filename.split('.')[-1].lower()
    #check if it's an allowed extension
    if extension not in allowedextensions:
        return False
    
    return True
