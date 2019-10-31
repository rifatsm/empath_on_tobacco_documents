# Tobacco sample deposition abstract
# article = "The witness, senior vice-president and controller at R. J. Reynolds Tobacco Holding Inc., was deposed by the plaintiffs. He described the financial status of the holding company and its economic activities. He indicated that industry changes, corporate changes, market changes, structural changes, and some legal developments have all had an adverse effect on the profitability of the company. The witness also noted that advertising and promotion restrictions placed on them in 1998 by the Master Settlement Agreement had caused a drop in sales volume. He said that punitive damage awards would have a devastating effect on the company, although he declined to say whether bankruptcy was being considered."

# ETD sample abstract
# article = "It is often assumed that more realism is always desirable. In particular, many techniques for locomotion in Virtual Reality (VR) attempt to approximate real-world walking. However, it is not yet fully understood how the design of more realistic locomotion techniques influences effectiveness and user experience. In the previous VR studies, the effects of interaction fidelity have been coarse-grained, considering interaction fidelity as a single construct. We argue that interaction fidelity consists of various independent components, and each component can have a different effect on the effectiveness of the interface. Moreover, the designer's intent can influence the effectiveness of an interface and needs to be considered in the design. Semi-natural locomotion interfaces can be difficult to use at first, due to a lack of interaction fidelity, and effective training would help users understand the forces they were feeling and better control their movements. Another method to improve locomotion interaction is to develop a more effective interface or improve the existing techniques. A detailed taxonomy of walking-based locomotion techniques would be beneficial to better understand, analyze, and design walking techniques for VR. We conducted four user studies and performed a meta-analysis on the literature to have a more in-depth understanding of the effects of interaction fidelity on effectiveness. We found that for the measures dependent on proprioceptive sensory information, such as orientation estimation, cognitive load, and sense of presence, the level of effectiveness increases with increasing levels of interaction fidelity. Other measures which depend more on the ease of learning and ease of use, such as completion time, movement accuracy, and subjective evaluation, form a u-shape uncanny valley. For such measures, moderate-fidelity interfaces are often outperformed by low- and high-fidelity interfaces. In our third user study, we further investigated the effects of components of interaction fidelity, biomechanics and transfer function, as well as designers' intent. We learned that the biomechanics of walking are more sensitive to changes and that the effects of these changes were mostly negative for hyper-natural techniques. Changes in the transfer function component were easier for the user to learn and to adapt to. Suitable transfer functions were able to improve some locomotion features but at the cost of accuracy. To improve the level of effectiveness in moderate-fidelity locomotion interfaces we employed an effective training method. We learned that providing a visual cue during the acclimation phase can help users better understand their walking in moderate-fidelity interfaces and improve their effectiveness. To develop a design space and classification of locomotion techniques, we designed a taxonomy for walking- based locomotion techniques. With this taxonomy, we extract and discuss various characteristics of locomotion interaction. Researchers can create novel locomotion techniques by making choices from the components of this taxonomy, they can analyze and improve existing techniques, or perform experiments to evaluate locomotion techniques in detail using the presented organization. As an example of using this taxonomy, we developed a novel locomotion interface by choosing a new combination of characteristics from the taxonomy."

# My own random sample 
article = "Why do you hate it"

# lexical categories total: 194
# categories total: 

import operator
import os
from sys import argv
from empath import Empath

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-' and argv[0][1] != 'h':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def process_data(data, categories = None, normalize=True):
    # Store all the emotions
    if categories is None:
        result = lexicon.analyze(data, normalize=normalize)
    else:
        result = lexicon.analyze(data, categories=categories, normalize=normalize)
    # Keeping only the non.zero valued items
    result = {x:y for x,y in result.items() if y!=0.0}
    # Sort the emotions based on their probability
    return sorted(result.items(), key=operator.itemgetter(1), reverse=True)

lexicon = Empath()

myargs = getopts(argv)
if '-h' in myargs or len(myargs) == 0:  # Example usage.

    print('\nProcessing on example sentence : "Why do you hate it" ')
    result = process_data(article)
    print("result", result)

    print('\n\nUsage: python test_empath.py -d data_directory_path -t[optional] number_of_files -s[optional][used alone] "test sentence here" ')
    print('\t-d: Specify data directory path')
    print('\t-t: Number of documents to be processed from the directory')
    print('\t-h: To see this help page again.')
    print('\t-s: Process on given string.\n')

    exit()

DATA_DIR = myargs['-d']

if '-t' in myargs:
    DOCS_TO_PROCESS = int(myargs['-t'])
else:
    DOCS_TO_PROCESS = len([name for name in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, name))])

if '-s' in myargs:
    
    sentence = myargs['-s']
    result = process_data(sentence)

    print("result", result)

    exit()

categories = ['hate','fear','joy','envy','love', 'surprise']
for i, file_name in enumerate(os.listdir(DATA_DIR)):

    file_path = os.path.join(DATA_DIR, file_name)
    file = open(file_path, 'r')
    data = file.read().replace('\n', ' ')
    result = process_data(data, categories,True)
    print(file_name, "\n", result)
    if i == DOCS_TO_PROCESS-1:
        break