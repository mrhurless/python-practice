import emoji

emo = input('Input: ').strip()

print(emoji.emojize(emo, language='alias'))