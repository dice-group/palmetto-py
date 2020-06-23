from palmettopy.palmetto import Palmetto
words = ["cherry", "pie", "cr_eam", "apple", "orange", "banana", "pineapple", "plum", "pig"]
#words = ['label', 'type', 'character', 'subject', 'discipline', 'topic', 'national', 'home_page', 'foundation', 'basis', 'foundation_garment', 'initiation']
#words = ['label', 'type', 'character', 'subject', 'discipline', 'topic', 'national', 'home_page', 'foundation', 'basis', 'foundation_garment']
#words = ['label', 'type', 'character', 'subject', 'discipline', 'topic', 'national', 'home_page', 'foundation', 'basis']
palmetto = Palmetto()
#palmetto.get_df_for_words(words)
#print(palmetto.get_coherence_fast(words))
print(palmetto.get_coherence(words))
