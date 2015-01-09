import threading
import random
import time
from app import models


class GetSales(object):

    sale = random.randint(10, 30000)
    finished = False

    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        print "starting the timer {}".format(time.time())
        start_time = time.time()
        self.sale = self.biggest_sale(models.Produs)['id']
        print time.time() - start_time

    def get_biggest_sale(self):
        return self.sale

    @staticmethod
    def process_entry(prod):
        """ a) create a list of the dict's keys and values;
            b) return the key with the max value"""
        dict = prod.preturi_dict()
        max_value = max(dict, key=lambda x: x['value'])
        min_value = min(dict, key=lambda x: x['value'])
        diff = 100 - ((min_value['value'] * 100)/max_value['value'])
        return diff

    def biggest_sale(self, model):
        entries = model.query.all()
        sales_list = [
            {'id': e.idProdus,
             'value': self.process_entry(e)}
            for e in entries
            ]
        return max(sales_list, key=lambda x: x['value'])
