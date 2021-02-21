class User:
    def __int__(self, email, password, full_name, gender='other', birth_date= None):
        self.email = email
        self.password = password
        self.full_name = full_name
        self.gender = gender
        self.birth_date = birth_date


class Card:
    def __init__(self):
        pass

class Address:
    def __init__(self, country, state, city, address_1, address_2, zipcode):

        self.country = country
        self.state = state
        self.city = city
        self.addres_1 = address_1
        self.addres_2 = address_2
        self.zipcode = zipcode


class Customer(User):

    def __init__(self, email, password, full_name,
                 card: Card,
                 shipping_address: Address,
                 billing_address: Address,
                 currency: str,
                 gender='other',
                 birth_date=None):
        super().__int__(email, password, full_name, gender, birth_date)
        self.gender= gender
        self.card = card
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.currency = currency

card = Card()
address = Address('USA', 'New York', 'New York', 'street_1', 'street-2', 1234)
customer = Customer('jack@jack.com', 'pass', 'Jack Johnson',card, address, address, currency='usd')
print(customer.full_name)
class VipCustomer(Customer):
    def __init__(self, discount=0, free_shipping=False, cupon=None):
        self.discount = discount
        self.free_shipping = free_shipping
        self.cupon = cupon



class Admin(User):
    def __init__(self):
        pass


