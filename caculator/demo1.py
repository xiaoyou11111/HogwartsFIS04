import pytest
import yaml

print(yaml.safe_load(open("./data.yaml"))["add_int"])