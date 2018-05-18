import sys
import palmettopy.exceptions
from palmettopy.palmetto import Palmetto
words = ["cherry", "pie", "cr_eam", "apple", "orange", "banana",
         "pineapple", "plum", "pig", "cra_cker", "so_und", "kit"]
palmetto = Palmetto()
try:
    result = palmetto.get_df_for_words(words)
    sys.exit(0)
except palmettopy.exceptions.EndpointDown:
    sys.exit(1)
