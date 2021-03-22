from class_20_03_21.helpers import get_session
from class_20_03_21.models import Restaurant

session = get_session()

result = session.query(Restaurant).all()
print(result)
