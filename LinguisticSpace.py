"""
LINGUISTIC SPACE

Space can be approached linguistically by finding words related to space and
place. This code finds the most common words from two POS groups — nouns and verbs —
and creates Excel sheets with the fifty most common words in each category
from two literary dystopian texts: Huxley's Brave New World and Atwood's The Handmaid's Tale.

The list of frequent words can be further analysed by comparing occurrences and
 frequencies of words related to space, travel, movement, etc.
Based on the list, the frequency distribution of selected words across segments
of texts can be visually displayed via Voyant Tools to check where in the text
the words occur and if there exists thematic co-occurrence.

NER retrieves LOCs, GPEs, and FACs (locations, geopolitical entities, facilities)

"""

import spacy
import pandas as pd


def get_text(filename, beginning):
    """
    cuts pre- and post-text not belonging to story and gets rid of line breaks
    as well as trailing hyphens.
    :param filename: string
    :param beginning: string, string that marks the beginning of text
    :return: string, cleaned text
    """
    with open(filename) as file:
        # read text into a string
        text_as_string = file.read()

    # cut the pre-text and post-text
    index_of_beginning = text_as_string.find(beginning)
    index_of_end = text_as_string.find("</pre>")
    # print("ending: ", story_text[-20:])
    story_text = text_as_string[index_of_beginning:index_of_end]

    # create one string without line breaks or trailing hyphens
    text = ""
    lines = story_text.splitlines()
    for line in lines:
        if line.endswith("- "):
            x = line.rstrip(
                "- ")  # remove trailing hyphens at the end of lines
        else:
            x = line.replace('\n', ' ')  # replace line break with empty string
        text += x
    return text


def get_nouns(doc, lemma=True):
    """
    Extracts words with POS tag NOUN. Creates dictionary with
    unique lemmatised nouns and their frequencies if lemma is True. If lemma is False,
    the function returns tokens instead of lemmas.
    :param doc: doc nlp objetc with text
    :return: dict, dictionary with nouns and frequencies
    """
    nouns_list = []
    for token in doc:
        if token.pos_ == "NOUN":
            # lemmatise to group together the different forms of the same token
            # like singular and plural forms of one token. lemma_ automatically
            # converts token into string
            if lemma:
                nouns_list.append(token.lemma_.lower())
            else: # lemma=false
                nouns_list.append(token.text.lower()) #for unlemmatised tokens
    # print("nr of nouns: ", len(nouns_list))
    # print(nouns_list[0], type(nouns_list[0]))

    noun_dict = {}
    for noun in nouns_list:
        if noun in noun_dict:
            # if noun in dict, add +1 to value count
            word_count_new = noun_dict[noun] + 1
            # replace value with new
            noun_dict[noun] = word_count_new
        else:
            noun_dict[noun] = 1
    return noun_dict


def get_verbs(doc, lemma=True):
    """
    Extracts words with POS tag VERB. Creates dictionary with
    unique lemmatised verbs and their frequencies.
    :param doc: doc nlp objetc with text
    :return: dict, dictionary with verbs and frequencies
        """
    verb_list = []
    for token in doc:
        if token.pos_ == "VERB":
            if lemma:
                # lemmatise to group together the different forms of the same token
                verb_list.append(token.lemma_.lower())
            else:
                # unlemmatised tokens
                verb_list.append(token.text.lower())
    print("nr of verbs: ", len(verb_list))
    # print(nouns_list[0], type(nouns_list[0]))

    verb_dict = {}
    for verb in verb_list:
        if verb in verb_dict:
            # if noun in dict, add +1 to value count
            word_count_new = verb_dict[verb] + 1
            # replace value with new
            verb_dict[verb] = word_count_new
        else:
            verb_dict[verb] = 1
    return verb_dict


def dict_to_df(dict_data):
    """
    Creates a pandas dataframe from dictionary.
    :param dict_data: dict
    :return: df_data, Dataframe
    """
    data = {'WORD': dict_data.keys(), "FREQUENCY": dict_data.values()}
    # print(data)
    df_data = pd.DataFrame.from_dict(data)
    return df_data


def get_LOCs(doc):
    """
    Loops over the named entities in the Doc object
    Note: this is not very useful. Wrong hits like Lenina, Delta, Central
    London (though part of "Central London Hatchery and Conditioning Centre".
    :param doc: nlp doc object
    :return: list with entities labeled as LOC
    """
    LOC_list = []
    for ent in doc.ents:
        if (ent.label_ == "LOC"):
            LOC_list.append(ent.text)

    return LOC_list


def get_GPE(doc):
    GPE_list = []
    for ent in doc.ents:
        if (ent.label_ == "GPE"):
            GPE_list.append(ent.text)
    return GPE_list


def get_FAC(doc):
    FAC_list = []
    for ent in doc.ents:
        if (ent.label_ == "FAC"):
            FAC_list.append(ent.text)
    return FAC_list


def lemmatise_doc(doc, name):
    # lemmatise each token and join into string
    lemmatised_text = " ".join(token.lemma_ for token in doc)
    #create a new txt file and add lemmatised text
    with open(name, "a") as f:
        f.write(lemmatised_text)


def main():
    nlp = spacy.load('en_core_web_lg')
    # print(nlp)
    BNW_text = get_text("Huxley_BNW.txt", "Chapter One")
    THT_text = get_text("Atwood_HandmaidsTale.txt", "CHAPTER ONE")

    BNW_doc = nlp(BNW_text)
    THT_doc = nlp(THT_text)
    # print(BNW_doc[:2000])
    # print(THT_doc[:2000])


    # --- NOUNS ----
    BNW_noun_dict = get_nouns(BNW_doc, lemma=True) #change to False to get tokens instead of lemmas
    print("nr of unique nouns: ", len(BNW_noun_dict))
    BNW_df_nouns = dict_to_df(BNW_noun_dict)
    # df to excel but only the fifty most common tokens
    BNW_fifty_nouns = BNW_df_nouns.sort_values(['FREQUENCY'], ascending=False).head(50)
    print("Fifty most common nouns in BNW: \n", BNW_fifty_nouns)
    BNW_fifty_nouns.to_excel("BNW_nouns_LinguisticSpace.xlsx")


    THT_noun_dict = get_nouns(THT_doc, lemma=True)
    print("nr of unique nouns: ", len(THT_noun_dict))
    THT_df_nouns = dict_to_df(THT_noun_dict)
    # df to excel but only the fifty most common tokens
    THT_fifty_nouns = THT_df_nouns.sort_values(['FREQUENCY'], ascending=False).head(50)
    print("Fifty most common nouns in THT: \n", THT_fifty_nouns)
    THT_fifty_nouns.to_excel("THT_nouns_LinguisticSpace.xlsx")


    # --- VERBS ---
    BNW_verb_dict = get_verbs(BNW_doc, lemma=True)
    print("nr of unique verbs: ", len(BNW_verb_dict))
    BNW_df_verbs = dict_to_df(BNW_verb_dict)
    BNW_fifty_verbs = BNW_df_verbs.sort_values(['FREQUENCY'], ascending=False).head(50)
    # print 50 verbs with highest freq
    print("Fifty most common verbs in BNW: \n", BNW_fifty_verbs)
    # df to excel
    BNW_fifty_verbs.to_excel("BNW_verbs_LinguisticSpace.xlsx")

    THT_verb_dict = get_verbs(THT_doc, lemma=True)
    print("nr of unique verbs: ", len(THT_verb_dict))
    THT_df_verbs = dict_to_df(THT_verb_dict)
    # df to excel
    THT_fifty_verbs = THT_df_verbs.sort_values(['FREQUENCY'], ascending=False).head(50)
    print("Fifty most common verbs in THT: \n", THT_fifty_verbs)
    THT_fifty_verbs.to_excel("THT_verbs_LinguisticSpace.xlsx")


    # --- NER LOC ---
    BNW_LOC_entities = get_LOCs(BNW_doc)
    print("Locations in BNW:")
    print(*BNW_LOC_entities, sep='\n')
    print("\n")
    print("Locations in THT:")
    THT_LOC_entities = get_LOCs(THT_doc)
    print(*THT_LOC_entities, sep='\n')

    # --- NER GPE ---    (geopolitical entity: countries, cities, states)
    BNW_GPE_entities = get_GPE(BNW_doc)
    print("Geopolitical entities in BNW:")
    print(*BNW_GPE_entities, sep='\n')
    print("\n")
    print("Geopolitical entities in THT:")
    THT_GPE_entities = get_GPE(THT_doc)
    print(*THT_GPE_entities, sep='\n')

    # --- NER FAC ---       (facilities: builidngs, bridges, airports)
    BNW_FAC_entities = get_FAC(BNW_doc)
    print("Geopolitical entities in BNW:")
    print(*BNW_FAC_entities, sep='\n')
    print("\n")
    print("Facility entities in THT:")
    THT_FAC_entities = get_GPE(THT_doc)
    print(*THT_FAC_entities, sep='\n')

    # get lemmatised BNW and THT  for further analysis with VoyantTools
    lemmatise_doc(BNW_doc, "lemmatised_BNW.txt")
    lemmatise_doc(THT_doc, "lemmatised_THT.txt")


if __name__ == "__main__":
    main()
