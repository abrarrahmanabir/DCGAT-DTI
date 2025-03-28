from utils import process_DB
from utils import process_bindingDB ,process_yamanishi, process_luo # , process_hetionet, process_BioKG, 
import sys 


class PREPROCESS:
    def __init__(self, config):
        self.config = config
        
    def process_data(self):
        if self.config['name'] == 'drugbank':
            X_drug, X_target, DTI = process_DB.process_data(self.config)
        elif self.config['name'] == 'yamanishi':
            print(self.config)
            X_drug, X_target, DTI = process_yamanishi.process_data(self.config)
        elif self.config['name'] == 'luo':
            X_drug, X_target, DTI = process_luo.process_data(self.config)
        # elif self.config['name'] == 'hetionet':
        #     X_drug, X_target, DTI = process_hetionet.process_data(self.config)
        # elif self.config['name'] == 'BioKG':
        #     X_drug, X_target, DTI = process_BioKG.process_data(self.config)
        elif self.config['name'] == 'bindingDB':
            #print("I am in binding DB")
            X_drug, X_target, DTI = process_bindingDB.process_data(self.config)
            #print("I am in binding DB ///",X_drug.values)
        else:
            print('Dataset name not recognized')
            sys.exit()
        return X_drug, X_target, DTI



