import nltk

hypothesis = ["This", "is", "cat"]
reference = ["This", "is","a", "cat"]
BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis, weights = [0.25])
print(BLEUscore)