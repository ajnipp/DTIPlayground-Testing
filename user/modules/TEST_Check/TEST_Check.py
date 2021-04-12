
from dtiprep.modules import DTIPrepModule
import dtiprep
import TEST_Check.dummy as dummy #user defined module in the module
import TEST_Check.arisu as ari
#from TEST_Check.tmod import arisu  as tmodari
import TEST_Check.tmod.arisu as tmodari
import sys

logger=dtiprep.logger.write
#logger=print

# class DTIPrepModule:
#     def __init__(self,*args,**kwargs):
#         print('test')
#     def process(self):
#         print('process')

class TEST_Check(DTIPrepModule):
    def __init__(self,*args,**kwargs):
        super().__init__(TEST_Check)

    def process(self):
        super().process()
        logger("USER defined pipeline function : {}".format(self))
        logger(str(dummy.add(54,100)))
        logger(str(ari.div(54,100)))
        logger(str(tmodari.div(100,2)))