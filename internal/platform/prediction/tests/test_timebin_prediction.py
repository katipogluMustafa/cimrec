import unittest

from internal.platform.datasets.movielens_dataset import MovielensDataset
from internal.platform.optimizer.dataset_optimizer import DatasetOptimizer
from internal.platform.prediction.timebin_prediction import StaticTimebinPrediction


class TestTimebinPrediction(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(TestTimebinPrediction, self).__init__(*args, **kwargs)
    self.dataset = MovielensDataset(
            ratings_file_path=r'C:\Users\Yukawa\PycharmProjects\ProjectAlpha\data\movie_datasets\ml-latest-small'
                              r'\ratings.csv',
            movies_file_path=r'C:\Users\Yukawa\PycharmProjects\ProjectAlpha\data\movie_datasets\ml-latest-small'
                             r'\movies.csv')
    self.optimized_dataset = DatasetOptimizer(self.dataset)

  def test_prediction(self):
    self.assertEqual(False, False)
    static_timebin_prediction = StaticTimebinPrediction(self.optimized_dataset)
    static_timebin_prediction.predict(448, 3)


if __name__ == '__main__':
  unittest.main()
