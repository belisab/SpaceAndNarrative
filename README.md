# Space and Narrative in Huxley's and Atwood's Dystopian Fiction


## Project description
This GitHub repository is part of the MA thesis "Space and Narrative in Huxley's and Atwood's Dystopian Fiction" from the University of Helsinki. 
The aim was to combine digital tools and close readings to gain insight into the
role of space and place in structuring narrative. 

In my thesis, the objective was not to investigate broad trends in literature, but rather, to leverage the digital
for assisting in narrative sense-making and in pointing to relevant themes and passages for close
reading in two novels: Aldous Huxley's _Brave New World_ and Margaret Atwood's _The Handmaid's Tale_. 
For this purpose, the digital finds two applications: firstly,
Python aided in the segmentation of the narratives and was used to visualise the spatial narrative
progressions. Secondly, Python was used to retrieve word frequencies. The word frequencies were
further used to detect thematic correlation between selected words with the help of Voyant Tools, a
commonly used corpus program for literary analysis. Microsoft Copilot was utilised
to assist in the writing of code that generates narrative progression diagrams.


## Code
The project features two Python programs: NarrativeProgression.py and 
LinguisticSpace.py. The former code maps the texts' narrative progression in 
the form of horizontally stacked progression bar diagrams shown in Figure 1 and Figure 2. 

LinguisticSpace.py finds the most common words from the two POS groups
nouns and verbs and creates Excel sheets with the fifty most common words
of each category in both texts. LinguisticSpaceData.xlsx is a compiled file with those lists.
The code also conducts an NER analysis by
retrieving LOCs, GPEs, and FACs (locations, geopolitical entities, facilities).



## Run the code
0. (Set up venv by running `python3 -m venv .venv`, then on Windows run `.venv\Scripts\activate` or on macOS/Linux `source .venv/bin/activate`)
1. Run `python3 -m pip install -r requirements.txt`
2. Run `cd SpatialNarrativeProgression`
3. Get the .txt files of the novels and add them to the same folder
4. Separately install the spacy large language model using
`python3 -m spacy download en_core_web_lg`

## Results
The diagrams in Figure 1 and Figure 2 serve to illustrate spatial narrative progression as transitions between the dystopian and
non-dystopian. Comparing the two diagrams, one can see that they highlight the distinct spatial
organisations of the two narratives.

The linguistic analysis provides insight into the texts' linguistic spaces. 
The top fifty lemmatised nouns and verbs were compiled and saved in LinguisticSpaceData.xlsx (lemmatised and unlemmatised results were copied into the file from the code-generated files *_LinguisticSpace.xlsx).
The results suggest that both texts feature a large number of space-related
nouns (e.g. room, door, floor, house, window), nouns that have to do with people (e.g. woman, man,
girl, boy, child, people) and body parts (e.g. hand, eye, head, face).

A subsequent analysis with VoyantTools helped to identify thematic 
co-occurrence of space-related nouns shown in Figures 3, 4, and 5.
The results of the NER analysis can be found in NER_results_LinguisticSpace.xlsx.

## Findings
Find the thesis via Helda, an open repository of the University of Helsinki: https://helda.helsinki.fi/ 



