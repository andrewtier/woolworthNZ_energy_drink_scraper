import re

def normalize_name(full_title):
    patterns = [
        r'Single can \d+ml',
        r'Can \d+ml',
        r'\d+ml cans \d+pack',
        r'Single bottle \d+ml',
        r'\d+ml',
        r'\d+pack',
        r'\s+pack',
        r'sugar free',
    ]
    cleaned = full_title.lower()
    for p in patterns:
        cleaned = re.sub(p, '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def filter_and_sort_drinks(drinks):
    unique_drinks = {}
    for title, price in drinks:
        norm_name = normalize_name(title)
        if norm_name not in unique_drinks or price < unique_drinks[norm_name][1]:
            unique_drinks[norm_name] = (title, price)
    return sorted(unique_drinks.values(), key=lambda x: x[1])

import re

def extract_key(title): # this doesnt really work well, need to improve
    """
    Extract a simplified key from product title for duplicate filtering.
    Keep single-letter brands like 'v' intact.
    """
    title = title.lower()

    # Extract size info
    size_match = re.search(r'(\d+\s?ml|\d+pack|\d+x\d+ml|4x\d+ml)', title)
    size = size_match.group(1) if size_match else ''

    # Remove flavor, sugar-free, packaging words, and sizes
    clean_title = re.sub(r'(zero sugar|sugar free|single can|can|single bottle|pack|flavor|flavours|flavour|single|cans|bottle|single can)', '', title)
    clean_title = re.sub(r'\d+\s?ml|\d+pack|\d+x\d+ml|4x\d+ml', '', clean_title)
    clean_title = re.sub(r'[^a-z\s]', '', clean_title)  # keep letters and spaces only

    words = clean_title.split()

    # If first word is single letter (like 'v'), keep it and next words till energy drink or max 3 words
    if len(words) >= 1 and len(words[0]) == 1:
        brand_part = words[:3]  # keep first 3 words to be safe
    else:
        brand_part = []
        for w in words:
            brand_part.append(w)
            if 'energy' in brand_part and 'drink' in brand_part:
                break
            if len(brand_part) >= 3:
                break

    product_key = ' '.join(brand_part).strip()

    return (product_key, size)
