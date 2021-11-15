import sys, os

here = os.path.dirname(os.path.abspath(__file__))
app = os.path.abspath(os.path.join(here, "../../webhook"))
sys.path.insert(0, app)
