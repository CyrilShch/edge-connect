from main import main
import os
import random
from datetime import datetime
from torch.utils.tensorboard import SummaryWriter

def setup_experiment(title, logdir="./tb"):
    experiment_name = "{}@{}".format(title, datetime.now().strftime("%d.%m.%Y-%H:%M:%S"))
    writer = SummaryWriter(log_dir=os.path.join(logdir, experiment_name))
    
    return writer, experiment_name
  
writer, experiment_name = setup_experiment("EdgeConnect", logdir="./tb")

main(mode=1, writer=writer)
