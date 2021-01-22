from . import mnistDataset

def test_mnistDataset():
    assert mnistDataset.apply("Jane") == "hello Jane"
