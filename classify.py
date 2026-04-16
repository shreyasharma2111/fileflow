import os

#classify files based on name and type

def classify_file(filename, categories):
    #get file extension
    ext = os.path.splitext(filename)[1].lower()
    filename_lower = filename.lower()

    #check categories for matching extension
    for category, rules in categories.items():
        if category == 'general':
            continue

        #get keywords and extensions for the category
        keywords = rules.get("keywords", [])
        extensions = rules.get("extensions", [])

        #check if extension matches
        extension_match = ext in extensions
        #check if any keyword is in the filename
        keyword_match = any(keyword in filename_lower for keyword in keywords)
        #if either matches then return the category
        if extension_match or keyword_match:
            return category
        
    #if no category matches then return general
    return 'general'
