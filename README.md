# palmetto-py
Python interface for [Palmetto](https://github.com/AKSW/Palmetto)

NOTE: If palmetto endpoint is down, [create issue in palmetto repository](https://github.com/dice-group/Palmetto).

## How to use
First install palmettopy from the pipy:
```
pip install palmettopy
```

Then you can include it into your application and get coherence for a list of words as follows:
```
from palmettopy.palmetto import Palmetto
palmetto = Palmetto()
words = ["cake", "apple", "banana", "cherry", "chocolate"]
palmetto.get_coherence(words)
```

By default, this interface uses "cv" coherence type (the best performing according to the publication [1]). 
The coherence type can be customized as follows:
```
from palmettopy.palmetto import Palmetto
palmetto = Palmetto()
words = ["cake", "apple", "banana", "cherry", "chocolate"]
palmetto.get_coherence(words, coherence_type="cv")
```
The available coherence types are "ca", "cp", "cv", "npmi", "uci", and "umass".

The default endpoint is run by AKSW research group [2]. If you want to run your own endpoint, you can customize the interface as follows:
```
from palmettopy.palmetto import Palmetto
palmetto = Palmetto("http://example.com/myownendpoint")
words = ["cake", "apple", "banana", "cherry", "chocolate"]
palmetto.get_coherence(words, coherence_type="cv")
```

You can also calculate fast coherence using document frequencies for terms using get_coherence_fast method as follows:
```
from palmettopy.palmetto import Palmetto
palmetto = Palmetto()
words = ["cake", "apple", "banana", "cherry", "chocolate"]
palmetto.get_coherence_fast(words)
```

To get document frequencies for the words you can use the following method:
```
from palmettopy.palmetto import Palmetto
palmetto = Palmetto()
words = ["cake", "apple", "banana", "cherry", "chocolate"]
palmetto.get_df_for_words(words)
```

### References
* [1] [Exploring the Space of Topic Coherence Measures by Michael Röder, Andreas Both, and Alexander Hinneburg in Proceedings of the eight International Conference on Web Search and Data Mining, Shanghai, February 2-6](http://svn.aksw.org/papers/2015/WSDM_Topic_Evaluation/public.pdf)
* [2] [Palmetto project page on AKSW research group web site](http://aksw.org/Projects/Palmetto.html)

## Development Setup & Testing
```
  pip install -r requirements.txt
  pip install -e ./
  make test
```

## TODOs
Implement coherence calculation for two words as follows:
```
Two words w_i, w_j with two sets s_i, s_j, their intersection set s_ij (|s| is the size of these sets) and the size of the corpus C:
P(w_i,w_j)/(P(w_i)*P(w_j))
= (|s_ij| / C)/((|s_i| / C)*(|s_j| / C))
= (s_ij * C)/(|s_i|*|s_j|)
```
No need to calculate the logarithm as this will not affect the ranking.

## Contributors

Ivan Ermilov: [my github account](https://github.com/earthquakesan)
Michael Roeder: [github account](https://github.com/MichaelRoeder)

## License

This interface is licensed with Apache 2.0 license. For Palmetto license, see the [Palmetto github repo](https://github.com/aksw/palmetto).
