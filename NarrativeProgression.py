"""
NARRATIVE PROGRESSION

This program creates two diagrams that afford a visual representation of the
conceptual spatial organisations of plot in two literary dystopian texts:
Huxley's Brave New World and Atwood's The Handmaid's Tale.

A list of quotations that indicate whenever the stories transition from
dystopian to non-dystopian space or vice versa was created manually. Using that
list, the program identifies starting indexes of these quotes and consecutively
calculates the length of each segment of text measured in tokens. The results
are visualised using matplotlib.

"""

import matplotlib.pyplot as plt
from matplotlib.patches import Patch


sections_BNW = ["Dystopian World State", "Non-dystopian reservation",
                "Dystopian World State", "Non-dystopian reservation",
                "Dystopian World State", "Lighthouse"]
# I asked Copilot to create this list with the following prompt:
# continue this following list of alternating entries
# "Dystopian Gilead", "Pre-dystopian state", "Dystopian Gilead",
# "Pre-dystopian state" until the list contains 21 entries in total.
sections_THT = [
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead",
              "Pre-dystopian state",
              "Dystopian Gilead"
            ]


def get_text(filename, beginning):
    """
    Function returns a cleaned version of a text ("filename") as a
    string. CLeaning includes stripping any pre- and post-text that is not part
    of the fictional text, removing trailing hyphens so that words are not
    split and deleting line breaks so the text is saved in one continuous
    string.
    :param filename: str, name of .txt file
    :param beginning: str, the first words of the story, e.g. "Chapter One"
    :return: str, cleaned text
    """
    with open(filename) as file:
        # read text into a string and replace line breaks with an empty string
        # text_as_string = file.read().replace('\n', ' ')
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
            x = line.rstrip("- ") # remove trailing hyphens at the end of lines
        else:
            x = line.replace('\n', ' ')  # replace line break with empty string
        text += x

    return text


def find_transits_in_BNW(text):
    """
    Finds spatial transitions in story. Function splits story into chunks
    according to locations. Transitions were manually identified and the
    function finds indexes using chapter numbers and quotes. TThe function
    returns the indexes starting a new chunk (a new location) and the length of
    each chunk as list with integers.

    --- TRANSITIONS TO NEW LOCATION ---

    "Chapter One" (The World State is the initial setting)

    "Chapter Seven" (first time in the Mesa 'The mesa was like a ship becalmed
    in a strait of lion-colored dust')

    "Chapter Nine" (Bernard travels back to the World State to make arrangements
    before returning to the Reservation. When he embarks on his journey back,
    the narrative focalizer turns to John at the Reservation)

    "The young man stood outside the rest-house"

    "Chapter 10" (return to World State)

    "The Savage had chosen as his hermitage" (John arrives at the Lighthouse)
    """

    # manually found indicators that mark the start of chunk
    indicators = ["Chapter One",
                  "Chapter Seven",
                  "Chapter Nine",
                  "The young man stood outside the rest-house",
                  "Chapter Ten",
                  "The Savage had chosen as his hermitage",]

    # find index for new location
    starts = []
    for indicator in indicators:
        index = text.find(indicator)
        # test by printing out the first 200 characters of every start
        # of a chunk
        # print(index)
        # print(text[index: index + 200])
        starts.append(index)

    #print("starts: ", starts)
    #print("len of starts: ", len(starts))

    # starts mark the start of a chunk/location, but for the  diagram, the
    # length of each chunk is also needed
    chunks = []
    for i in range(len(starts)):  # len(starts) = 6 --> range 0-5
        # if last chunk, calculate chunk length based on
        # chunk = length of text - start of last chunk --> i ==  5
        if (i == len(starts) - 1):
            #print(i)
            chunk = len(text) - starts[i]
            # print("length of last chunk: ", chunk)
            # print(text[starts[i] : starts[i+200]])
        else:
            #print(i)
            chunk = starts[i + 1] - starts[i]
            # print("length of mid chunk: ", chunk)
            # print(text[starts[i] : starts[i+200]])
        chunks.append(chunk)
    #print(chunks)

    return starts, chunks


def find_transits_in_THT(text):
    """
    NOTE:This function is applied to only the first third of The Handmaid's Tale

    Finds spatial transitions in story. Function splits story into chunks
    according to locations. Transitions were manually identified and the
    function finds indexes using Chapter numbers and quotes. The function
    returns the indexes starting a new chunk (a new location) and the length of
    each chunk as lists with integers.
    """

    indicators = [
        "CHAPTER ONE", # present
        "Luke and I used to walk together",  # memory
        "We turn the corner",  # present
        "I remember those endless white plastic shopping bags",  # memory
        "Not here and now",  # present
        "Moira, sitting on the edge of my bed",  # memory
        "I would like to believe",  # present
        "I read that in a profile on her, in a news magazine",  # memory
        "She doesn’t make speeches any more",  # present
        "In the afternoons",  # memory
        "So. I explored this room",  # present
        "Moira, breezing into my room",  # memory
        "Is that how we lived",  # present
        "Moira and I",  # memory
        "The Commander stoops",  # present
        "One day, when she was eleven months old",  # memory
        "She fades, I can’t keep her here with me",  # present
        "I’m in our first apartment",  # dream/memory
        "The bell wakes me",  # present
        "It’s a Saturday morning, it’s a September",  # memory
        "The Commander knocks at the door.",  # present
    ]

    # shorten the text to only the first 100 pages since my manual annotations
    # only cover the first 100 (equals to 1/3 of teh text)
    text = text[:text.find("CHAPTER SIXTEEN")]
    # test output
    # print(text[-100:])

    # find index for new location
    starts = []
    for indicator in indicators:
        index = text.find(indicator)
        #print(index)
        # test by printing out teh first 200 characters of every start
        # of a chunk
        # print("Beginning of Transition: ", text[index: index + 500])
        starts.append(index)

    # print("starts: ", starts)
    # print("len of starts: ", len(starts))

    # calculate length of each chunk and store in list chunks
    chunks = []

    for i in range(len(starts)):    # len(starts) = 21 --> range 0-20
        # if last chunk, calculate chunk length based
        # chunk = length of text - start of last chunk --> i ==  20
        if (i == len(starts) - 1):
            #print(i)
            chunk = len(text) - starts[i]
            #print("length of last chunk: ", chunk)
            #print(text[starts[i] : starts[i+200]])
        else:
            #print(i)
            chunk = starts[i + 1] - starts[i]
            #print("length of mid chunk: ", chunk)
            #print(text[starts[i] : starts[i+200]])
        chunks.append(chunk)

    #print(chunks)

    return starts, chunks


def create_multi_row_diagram(title, starts, chunks, sections):
    """
    Function created with the support of Microsoft Copilot.
    Thus function creates a two-row broken horizontal bar chart for The
    Handmaid's Tale:
      - Top row (y=1): 'Dystopian Gilead' intervals
      - Bottom row (y=0): 'Pre-dystopian state' intervals
    --- Parameters ---
    title : str, Figure title
    starts : list[int], Start indexes of chunks.
    chunks : list[int], Lengths of consecutive narrative segments (as returned
    by find_transits_in_THT).
    sections : list[str], Labels of segment
    """

    # --- Split intervals by row/category ---
    intervals = {
        "Dystopian Gilead": [],
        "Pre-dystopian state": []
    }
    for length, start, label in zip(chunks, starts, sections):
        # Only collect known labels; ignore anything else silently
        if label in intervals:
            intervals[label].append((start, length))

    # --- Colors ----
    color_gilead = "darkred"    # OR desaturated teal  "#7A9E9F"
    color_neweng = "lightcoral"      # OR "#7A9E9F"

    # --- Build the figure ---
    fig, ax = plt.subplots(figsize=(10, 3), dpi=150)

    # full frame
    for spine in ["right", "top", "left", "bottom"]:
        ax.spines[spine].set_visible(True)

    # remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.tick_params(axis="both", which="both",
                   bottom=True, top=False, left=False, right=False,
                   labelbottom=True, labelleft=False)

    # y-axis label
    ax.set_ylabel("Ontological layers of space")
    # x-axis label
    ax.set_xlabel("Narrative progression in words")

    bar_height = 0.6

    # Draw the broken bars
    # Top row: Gilead at y=1
    if intervals["Dystopian Gilead"]:
        ax.broken_barh(intervals["Dystopian Gilead"], (1 - bar_height/2, bar_height),
                       facecolors=color_gilead)
    # Bottom row: Pre-dystopian at y=0
    if intervals["Pre-dystopian state"]:
        ax.broken_barh(intervals["Pre-dystopian state"], (0 - bar_height/2, bar_height),
                       facecolors=color_neweng)

    # X-limits: pad slightly around the total length
    total_len = sum(chunks)
    pad = max(5, int(0.02 * total_len))  # small visual margin
    ax.set_xlim(0 - pad, total_len + pad)

    # Title
    # --- Move title higher with padding and extra top space ---
    ax.set_title(title, pad=26)
    # increase vertical offset in points
    fig.subplots_adjust(top=0.83)        # leave extra room at the top (0..1

    # Legend (no labels on bars)
    handles = [
        Patch(facecolor=color_gilead, label="Dystopian Gilead"),
        Patch(facecolor=color_neweng, label="Pre-dystopian state"),
    ]
    ax.legend(handles=handles,
              ncol=2, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, 1.18))

    plt.tight_layout()

    plt.show()


def create_one_row_diagram(title, starts, chunks, sections):
    """
    Function created with the support of Copilot.
    Draws a one-row horizontally stacked bar chart for BNW. Each chunk is
    colored based on its section label.
    --- Parameters ---
    title : str, Figure title
    starts : list[int], Start indexes of chunks.
    chunks : list[int], Lengths of consecutive narrative segments (as returned
                        by find_transits_in_THT).
    sections : list[str], Labels of segment
    """

    # color palette for bar segments
    palette = {
        "Dystopian World State": "lightgreen",
        "Non-dystopian reservation": "darkgreen",
        "Lighthouse": "lightskyblue"
    }
    colors = [palette.get(lbl, "#999999") for lbl in sections]

    # Plot
    fig, ax = plt.subplots(figsize=(10, 3), dpi=150)

    # Show axis lines, but hide ticks and numeric labels
    for spine in ["right", "top", "left", "bottom"]:
        ax.spines[spine].set_visible(True)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.tick_params(axis="both", which="both",
                   bottom=True, top=False, left=False, right=False,
                   labelbottom=True, labelleft=False)

    # Axis labels
    ax.set_xlabel("Narrative progression in words")
    ax.set_ylabel("Ontological layers of space")

    # Draw stacked segments in one row
    y0 = 0
    height = 0.6
    for start, width, color in zip(starts, chunks, colors):
        ax.barh(y=y0, width=width, left=start, height=height,
                color=color, edgecolor="none")

    # X-limits
    total_len = sum(chunks)
    pad = max(5, int(0.02 * total_len))
    ax.set_xlim(0 - pad, total_len + pad)
    ax.set_ylim(-0.8, 0.8)

    # Title and legend
    ax.set_title(title, pad=20)
    fig.subplots_adjust(top=0.85)
    handles = [Patch(facecolor=clr, label=lbl) for lbl, clr in palette.items()]
    ax.legend(handles=handles, ncol=3, frameon=False,
              loc="upper center", bbox_to_anchor=(0.5, 1.15))

    plt.tight_layout()
    plt.show()


def main():
    cleaned_text_BNW = get_text("Huxley_BNW.txt", "Chapter One")
    starts_BNW, chunks_BNW = find_transits_in_BNW(cleaned_text_BNW)
    create_one_row_diagram("BNW progression", starts_BNW, chunks_BNW, sections_BNW)

    cleaned_text_THT = get_text("Atwood_HandmaidsTale.txt", "CHAPTER ONE")
    starts_THT, chunks_THT = find_transits_in_THT(cleaned_text_THT)
    create_multi_row_diagram("Progression of the first third of THT", starts_THT, chunks_THT, sections_THT)


if __name__ == "__main__":
    main()