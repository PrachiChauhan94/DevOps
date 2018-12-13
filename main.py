import random

buzz = ['continuous testing', 'continuous integration', 'continuous deployment', 'continuous improvement', 'devops']
adjectives = ['complete', 'modern', 'self-service', 'integrated', 'end-to-end']
adverbs = ['remarkably', 'enormously', 'substantially', 'significantly','seriously']
verbs = ['accelerates', 'improves', 'enhances', 'revamps', 'boosts']


def get_phrase():
    words = set(random.sample(buzz, 2))
    words.add(random.sample(adjectives, 1)[0])
    words.add(random.sample(adverbs, 1)[0])
    words.add(random.sample(verbs, 1)[0])
    return ','.join(words)

'''
if __name__ == '__main__':
    generated_phrase = get_phrase()
'''