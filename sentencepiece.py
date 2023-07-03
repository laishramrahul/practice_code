import sentencepiece as spm
spm.SentencePieceTrainer.train(input='/home/laishram/workspace/mt/data/train.as.txt', model_prefix='m', vocab_size=10000, user_defined_symbols=['foo', 'bar'])