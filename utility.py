import datetime
import unittest
def days_until_centurion():
  cur_date = datetime.date.today()
  centurion = datetime.date(2089, 12, 23) # my birthday
  days_left = str((centurion - cur_date).days)
  formatted_days_left = days_left[:2] + ',' + days_left[2:]
  print '\nin {} days i turn 100.'.format(formatted_days_left)

def days_old():
  cur_date = datetime.date.today()
  birthday = datetime.date(1989, 12, 23)
  days_old = str((cur_date - birthday).days)
  formatted_days_old = days_old[:1] + ',' + days_old[1:]
  print '\ni am {} days old.'.format(formatted_days_old)
  return days_old

def days_until_10000():
  print '\n{} days until i am 10,000 days old.'.format(10000-int(days_old()))

"""add entry, get current weight, get history, chart weight, all time values"""
class Weight(object):
  """ class to keep track of weight """
  weight = []
  
  def __init__(self, weight):
    self.weight.append((weight, datetime.date.today()))

  @classmethod
  def get_current_weight(cls):
    """ return the most recent weight entry """
    return cls.weight[-1][0]

  @classmethod
  def add_entry(cls, entry, day=None, month=None, year=None):
    """ add a weight entry """
    entry_date = datetime.date(year,month,day)
    cls.weight.append((entry, entry_date))

  @classmethod
  def get_weight_history(cls):
    for entry in cls.weight:
      print "weight:{} date:{}".format(entry[0], entry[1])

  @classmethod
  def all_time_Values(cls):
    max_weight = max(cls.weight)[0]
    min_weight = min(cls.weight)[0]
    print 'max weight:{}, min weight:{}'.format(max_weight, min_weight)


class TestWeight(unittest.TestCase):
  def setup(self):
    john = Weight(201)
    john.add_entry(215, 23, 12, 1989)
    self.assertEqual()

  def test_add_entry(self):
    john = Weight(201)
    john.add_entry(215, 23, 12, 1989)
    john.get_weight_history()

  def test_all_time_values(self):
    pass

# if __name__ == "__main__":
#     unittest.main()


# john = Weight(200)
# john.add_entry(215)
# john.add_entry(215)
# john.add_entry(215)
# john.add_entry(215)
# john.add_entry(215)
# print john.get_current_weight()

  # john.get_weight_history()

# print datetime.date.today()
# print datetime.date(1883,12,20)

days_until_centurion()
days_until_10000()
