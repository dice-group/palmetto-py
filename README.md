# palmetto-py
Python interface for [Palmetto](https://github.com/AKSW/Palmetto)

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

### References
* [1] [Exploring the Space of Topic Coherence Measures by Michael Röder, Andreas Both, and Alexander Hinneburg in Proceedings of the eight International Conference on Web Search and Data Mining, Shanghai, February 2-6](http://svn.aksw.org/papers/2015/WSDM_Topic_Evaluation/public.pdf)
* [2] [Palmetto project page on AKSW research group web site](http://aksw.org/Projects/Palmetto.html)

## Development Setup & Testing
```
  pip install -r requirements.txt
  pip install -e ./
  make test
```

## Contributors

Ivan Ermilov: [my github account](https://github.com/earthquakesan)

## License

This interface is licensed with Apache 2.0 license. For Palmetto license, see the [Palmetto github repo](https://github.com/aksw/palmetto).
