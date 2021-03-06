# Contains all the path variables that need to be configured before running
# the program on a new computer

import sys

BASEDIR = '/home/nlp/wpred'
if sys.platform == 'darwin':
    USERDIR = '/Users/alexanderfedchin/wpred'

NEWSELA = BASEDIR + "/newsela"
NEWSELA_METAFILE = NEWSELA + '/articles_metadata.csv'
PARSERDIR = BASEDIR + '/stanford-parser-full-2015-12-09/'
OUTDIR_SENTENCES = NEWSELA + '/alignments/sentences/'
OUTDIR_PARAGRAPHS = NEWSELA + '/alignments/paragraphs/'
MANUAL_SENTENCES = NEWSELA + '/manual/sentences/'
MANUAL_PARAGRAPHS = NEWSELA + '/manual/paragraphs/'
PARSERPROG = 'custom/Parser'
TOKENIZERPROG = 'custom/Tokenizer'
MODELS = 'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz'
CLASSPATH = ':'.join(['.', PARSERDIR, PARSERDIR + 'stanford-parser.jar',
                      PARSERDIR + 'stanford-parser-3.6.0-models.jar',
                      PARSERDIR + 'slf4j-api.jar',
                      BASEDIR + '/stanford-postagger/stanford-postagger.jar'])

N_GRAM_DIRECTORY = "/home/nlp/wpred/googleNGrams/"
LEXICON = "/home/nlp/wpred/lexicons/ALL.tsv"
SYLLABIFIER = "/home/nlp/wpred/ghpaetzold-MorphAdornerToolkit-44bb87d/" \
              "SyllableSplitter/SyllableSplitter.jar"

PREDICTIONS = BASEDIR + "/predictions/"
NN_MODELS = BASEDIR + "/models/"
DEFAULT_MODEL_NAME = PREDICTIONS + "Best02-srn-63-3.01-probs.h5"
nnetFile = BASEDIR + "/data/test/NoOverlapRawTest.pbz2"
indexFile = BASEDIR + "/data/test/NoOverlapRawTest.idx"

KRIZ_IDX_FILE = BASEDIR + "/data/test/paper.idx"
KRIZ_BZ2_FILE = BASEDIR + "/data/test/paper.bz2"


MORPH_ADORNER_TOOLKIT = BASEDIR + "/ghpaetzold-MorphAdornerToolkit-44bb87d/"    # can be downloaded from
    # http://ghpaetzold.github.io/MorphAdornerToolkit/
