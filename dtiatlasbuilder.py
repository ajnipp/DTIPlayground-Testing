
import os
import time
import sys
import json 
import argparse
import csv
import shutil
import threading
import traceback
from copy import deepcopy
from pathlib import Path 
import yaml 

### for dev

import dmri.atlasbuilder.preprocess as preprocess
import dmri.atlasbuilder.atlas as atlas 
import dmri.atlasbuilder.utils as utils 
import dmri.atlasbuilder.builder as builder
import dmri.atlasbuilder as ab 
import dmri.common

logger=ab.logger.write

def build_atlas(args):
    Path(args.output_dir).mkdir(parents=True,exist_ok=True)
    logfilepath=Path(args.output_dir).joinpath('log.txt')
    initialize_logger(logfilepath, args.no_log_timestamp,args.no_verbosity)
    ## system log
    sys_log_dir=current_dir.joinpath('logs')
    sys_log_dir.mkdir(parents=True,exist_ok=True)
    env=os.environ
    uid, ts = dmri.common.get_uuid(), dmri.common.get_timestamp()
    sys_logfilename='dmriatlasbuilder_'+env['USER']+"_"+ts+"_"+uid+".txt"
    sys_logfile=sys_log_dir.joinpath(sys_logfilename)
    ab.logger.addLogfile(sys_logfile.__str__(),mode='w')
    logger("Execution ID : {}".format(uid))
    logger("Execution Command : "+" ".join(sys.argv))
    logger("--------------- Atlasbulder begins ----------------------",ab.Color.INFO)
    bldr=builder.Builder()
    bldr.configure(output_dir=args.output_dir,
                        config_path=args.config,
                        hbuild_path=args.hbuild,
                        greedy_params_path=args.greedy_params,
                        buildsequence_path=args.buildsequence,
                        node=args.node)
    bldr.build()

## utilities
def initialize_logger(logpath, no_log_timestamp, no_verbosity):
    ## default log setting
    ab.logger.setLogfile(logpath)
    ab.logger.setTimestamp(not no_log_timestamp)
    ab.logger.setVerbosity(not no_verbosity)

if __name__=="__main__":
    current_dir=Path(__file__).parent
    parser=argparse.ArgumentParser(description="Argument Parser")
    parser.add_argument('--output-dir', help='configuration file',default='output',type=str)
    parser.add_argument('--config',help='configuration file',default='config.yml',type=str)
    parser.add_argument('--hbuild',help='hierarchical build file', default='h-build.yml', type=str)
    parser.add_argument('--greedy-params',help='Greedy atlas parameter xml file', type=str)
    parser.add_argument('--node',help="node to build",type=str)
    parser.add_argument('--buildsequence',help='build sequence file, if this option is inputted then build sequence process will be skipped',type=str)

    ## log related
    parser.add_argument('--no-log-timestamp',help='Remove timestamp in the log', default=False, action="store_true")
    parser.add_argument('--no-verbosity',help='Do not show any logs in the terminal', default=False, action="store_true")

    args=parser.parse_args()

    try:
       logger("--------------- Atlasbulder begins ----------------------",ab.Color.INFO)
       build_atlas(args)
       sys.exit(0)
    except Exception as e:
       logger(str(e))
       msg=traceback.format_exc()
       logger(msg,ab.Color.ERROR)
       sys.exit(1)     



