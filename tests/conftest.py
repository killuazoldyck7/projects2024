import pytest
from faker import Faker
import random

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=0, type=int, help="Number of records to generate")

@pytest.fixture(scope="session")
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture
def generate_records(num_records):
    records = []
    for _ in range(num_records):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operation = random.choice(['add', 'subtract', 'multiply', 'divide', 'unknown'])
        records.append((a, b, operation))
    return records
