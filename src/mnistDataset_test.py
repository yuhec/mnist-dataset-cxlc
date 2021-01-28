from . import mnistDataset

def test_mnistDataset():
    assert mnistDataset.apply("../data/six.png") == {'best_probabilities': 0.97026044, 'number_selected': 8}
