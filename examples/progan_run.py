# -*- coding: UTF-8 -*-

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# NOTE: Make sure to configure for ProGAN with
#       '$ python config.py progan [--optional_kwargs]'
#       before running this script.

from gan_lab import get_current_configuration
from gan_lab.utils.data_utils import prepare_dataset, prepare_dataloader
from gan_lab.progan.learner import ProGANLearner

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

SAVE_MODEL_PATH = './models/progan_model.tar'

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# get most recent configurations:
config = get_current_configuration( 'config' )
data_config = get_current_configuration( 'data_config' )

# get DataLoader(s)
train_ds, valid_ds = prepare_dataset( data_config )
train_dl, valid_dl, z_valid_dl = prepare_dataloader( config, data_config, train_ds, valid_ds )

# instantiate ProGANLearner and train:
learner = ProGANLearner( config )
print( learner.gen_model.__class__.__name__, learner.disc_model.__class__.__name__ )
learner.train( train_dl, valid_dl, z_valid_dl )   # train for config.num_main_iters iterations
learner.config.num_main_iters = 300000
learner.train( train_dl, valid_dl, z_valid_dl )   # train for another 300000 iterations

# save model:
learner.save_model( SAVE_MODEL_PATH )