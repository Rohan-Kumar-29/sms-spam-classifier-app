import nltk

nltk_packages = ['punkt', 'stopwords', 'wordnet']

for pkg in nltk_packages:
    try:
        nltk.data.find(f'tokenizers/{pkg}') if pkg == 'punkt' else nltk.data.find(f'corpora/{pkg}')
    except LookupError:
        nltk.download(pkg)
