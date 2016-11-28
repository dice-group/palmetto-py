"""Fast coherence calculation from DF."""

def calculate_coherence_fast(words, doc_id_sets, corpus_size=4264684):
    word_pairs = _get_word_pairs(words)
    coherences = []
    for word_pair in word_pairs:
        coherence = _calculate_coherence_for(word_pair, words, doc_id_sets, corpus_size)
        coherences.append(coherence)
    # TODO: check if I need to take a product here
    return sum(coherences)


def _get_word_pairs(words):
    word_pairs = []
    for i in range(0, len(words)):
        for j in range(i, len(words)):
            word_pairs.append((words[i], words[j]))
    return word_pairs


def _calculate_coherence_for(word_pair, words, doc_id_sets, corpus_size):
    word_a = word_pair[0]
    word_b = word_pair[1]
    doc_id_set_a = doc_id_sets[words.index(word_a)][1]
    doc_id_set_b = doc_id_sets[words.index(word_b)][1]
    doc_id_set_ab = len(doc_id_set_a.intersection(doc_id_set_b))
    coherence = ( doc_id_set_ab * corpus_size ) / ( len(doc_id_set_a) * len(doc_id_set_b))
    return coherence
