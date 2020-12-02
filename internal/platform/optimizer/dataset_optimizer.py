from internal.platform.datasets.dataset import Dataset
import pandas as pd

class DatasetOptimizer:
  def __init__(self, dataset:Dataset, is_active=True):
    if dataset is None:
      raise InvalidDatasetOptimizerInput
    self.dataset = dataset
    self.is_active = is_active
    self.ratings = pd.DataFrame()
    self.movies  = pd.DataFrame()
    self.movie_ratings = pd.DataFrame()

  def get_ratings(self):
    if not self.is_optimizer_active():
      return self.dataset.load_ratings()
    if self.ratings.empty:
      self.ratings = self.dataset.load_ratings()
    return self.ratings

  def get_movies(self):
    if not self.is_optimizer_active():
      return self.dataset.load_movies()
    if self.movies.empty:
      self.movies = self.dataset.load_movies()
    return self.movies

  def get_movie_ratings(self):
    if not self.is_optimizer_active():
      return self.dataset.load_movie_ratings()
    if self.movie_ratings.empty:
      self.movie_ratings = pd.merge(self.get_ratings(), self.get_movies(), on='item_id')
    return self.movie_ratings

  def clean(self, clean_movies=True, clean_ratings=True, clean_movie_ratings=True):
    if clean_movies:
      self.movies = pd.DataFrame()
    if clean_ratings:
      self.ratings = pd.DataFrame()
    if clean_movie_ratings:
      self.movie_ratings = pd.DataFrame()

  def is_optimizer_active(self):
    return self.is_active

  def activate(self):
    self.is_active = True

  def deactivate(self):
    self.is_active = False

class InvalidDatasetOptimizerInput(Exception):
  pass

