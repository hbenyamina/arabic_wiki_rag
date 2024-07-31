import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
