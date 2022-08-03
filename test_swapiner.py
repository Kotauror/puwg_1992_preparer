import unittest
import pytest
from swapiner import swapiner
import csv

def test_swappiner(capsys):
    swapiner('sample_puwg_1992_data.csv')
    captured = capsys.readouterr()

    assert "567541.7 241860.8\n567543.3 241859.7\n567545.0 241858.5\n" in captured.out