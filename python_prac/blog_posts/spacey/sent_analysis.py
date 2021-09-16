import spacy 
from spacy.util import minibatch, compounding 



# import my dataset 
# text = pd.read_csv('', sep = ',')

doc = nlp(text)
token_list = [token for token in doc]
token_list

# remove stop words 
filtered_tokens = [token for token in doc if not token.is_stop]
filtered_tokens 

# normalize words 


# model part - will have to play with different options because not everything is going to be computationally effecient
def train_mod(training_data, test_data, iterations):
    nlp = spacy.load('en_core_web_sm')
    # doc = nlp(training_data)
    if "textcat" not in nlp.pipe_names:
        textcat = nlp.create_pipe("textcat", config={"architecture": "simple_cnn"})
        nlp.add_pipe(textcat, last = True)
    else:
        textcat = nlp.get_pipe("textcat")

    textcat.add_label("pos")
    textcat.add_label("neg")

    training_excluded_pipes = [pipe for pipe in nlp.pipe_names if pipe != "textcat"]




