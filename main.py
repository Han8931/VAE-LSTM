import logging
from setproctitle import setproctitle

import torch

from dataloading import Data
from model import build_VAELSTM
from trainer import Trainer


DATA_DIR = '/home/nlpgpu5/hwijeen/VAE-LSTM/data/'
FILE = 'mscoco'
DEVICE = torch.device('cuda:0')


setproctitle("(paraphrase) testing")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt = '%m/%d/%Y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)


if  __name__ == "__main__":

    #logger.info('loading data from... {}{}'.format(DATA_DIR, FILE))
    data = Data(DATA_DIR, FILE)
    vaeLSTM = build_VAELSTM(len(data.vocab), hidden_dim=600, latent_dim=1100,
                            device=DEVICE)
    trainer = Trainer(vaeLSTM, data)

    trainer.train(epoch=1)

