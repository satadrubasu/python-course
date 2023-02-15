import iso6346
class ShippingContainer:

    class_attr_counter = 100000
    next_serial = 1337

    def __init__(self,owner_code,contents,**kwargs):
        self.owner_code = owner_code
        self.contents = contents
        # ShippingContainer._make_bic_code doesnt let the Refrigirated child class to override.
        # self.bic = ShippingContainer._make_bic_code(owner_code=owner_code,serial=ShippingContainer._generate_serial())
        self.bic = self._make_bic_code(owner_code=owner_code,serial=ShippingContainer._generate_serial())
        self.serial = self.class_attr_counter
        ShippingContainer.class_attr_counter += 1

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="U"
        )

    @classmethod
    def create_empty(cls,owner_code,**kwargs):
        return cls(owner_code,contents=[],**kwargs)

    @classmethod
    def create_with_items(cls, owner_code,items,**kwargs):
        return cls(owner_code, contents=list(items),**kwargs)


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    def __init__(self,owner_code,contents,*,celsius,**kwargs):
        super().__init__(owner_code,contents,**kwargs)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Heated Boy!!")
        ## Go via the property setter to get validation logic not self._celsius
        self.celsius = celsius


    ######################### Getters and Setters
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Too Hot a temperature to set on the value.")
        self._celsius = value


    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)
    @fahrenheit.setter
    def fahrenheit(self,value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)
    ####################### END Getters / SETTERS

    @staticmethod
    def _c_to_f(celsius):
        return celsius *9/5 + 32
    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit -32 ) * 5/9

    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )