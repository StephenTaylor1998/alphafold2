import torch

# constants

MAX_NUM_MSA = 20
MAX_NUM_TEMPLATES = 10
NUM_AMINO_ACIDS = 21
NUM_EMBEDDS_TR = 1280 # best esm model 

DISTOGRAM_BUCKETS = 37
THETA_BUCKETS = 25
PHI_BUCKETS = 13
OMEGA_BUCKETS = 25

# embedding related constants

MSA_EMBED_DIM = 768
MSA_MODEL_PATH = ["facebookresearch/esm", "esm_msa1_t12_100M_UR50S"]

ESM_EMBED_DIM = 1280
ESM_MODEL_PATH = ["facebookresearch/esm", "esm1b_t33_650M_UR50S"]

PROTTRAN_EMBED_DIM = 1024

# default device

DEVICE_NAME = 'cuda' if torch.cuda.is_available() else 'cpu'
DEVICE = torch.device(DEVICE_NAME)

# aminoacid data

AA_DATA = { 
    'A': {
        'bonds': [[0,1], [1,2], [2,3], [1,4]] 
         },
    'R': {
        'bonds': [[0,1], [1,2], [2,3], [2,4], [4,5], [5,6],
                  [6,7], [7,8], [8,9], [8,10]] 
         },
    'N': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [5,7]] 
         },
    'D': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [5,7]] 
         },
    'C': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5]] 
        },
    'Q': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [6,7], [6,8]] 
        },
    'E': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [6,7], [7,8]]
        },
    'G': {
        'bonds': [[0,1], [1,2], [2,3]] 
        },
    'H': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [6,7], [7,8], [8,9], [5,9]] 
        },
    'I': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [4,7]] 
         },
    'L': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [5,7]] 
         },
    'K': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [6,7], [7,8]] 
         },
    'M': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [6,7]] 
         },
    'F': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [6,7], [7,8], [8,9], [9,10], [5,10]] 
         },
    'P': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [0,6]] 
         },
    'S': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5]] 
         },
    'T': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [4,6]] 
         },
    'W': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [6,7], [7,8], [8,9], [9,10], [10,11], [11,12],
                  [12, 13], [5,13], [8,13]] 
         },
    'Y': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [5,6],
                  [6,7], [7,8], [8,9], [8,10], [10,11], [5,11]] 
         },
    'V': {
        'bonds': [[0,1], [1,2], [2,3], [1,4], [4,5], [4,6]] 
         },
    '_': {
        'bonds': []
        }
    }
