from sacremoses import MosesTokenizer, MosesDetokenizer
mt, md = MosesTokenizer(lang='en'), MosesDetokenizer(lang='en')
sent = "This ain't funny. It's actually hillarious, yet double Ls. | [] < > [ ] & You're gonna shake it off? Don't?"
expected_tokens = ['This', 'ain', '&apos;t', 'funny', '.', 'It', '&apos;s', 'actually', 'hillarious', ',', 'yet', 'double', 'Ls', '.', '&#124;', '&#91;', '&#93;', '&lt;', '&gt;', '&#91;', '&#93;', '&amp;', 'You', '&apos;re', 'gonna', 'shake', 'it', 'off', '?', 'Don', '&apos;t', '?']
expected_detokens = "This ain't funny. It's actually hillarious, yet double Ls. | [] < > [] & You're gonna shake it off? Don't?"
mt.tokenize(sent) == expected_tokens
tokens=mt.tokenize(sent)
print(tokens)
md.detokenize(tokens) == expected_detokens
detok=md.detokenize(tokens)
print(detok)