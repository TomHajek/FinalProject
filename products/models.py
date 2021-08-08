from django.db.models import (
    Model, CharField, TextField, ForeignKey, FloatField,
    DateTimeField, IntegerField, BooleanField, ImageField,
    PROTECT,
)


class ProductSubCategory(Model):
    """
    Rostliny
        * pokojové, tilandsie, řasokoule, kapradiny, kaktusy a sukulenty, masožravé, orchideje a bromélie, ostatní...
        * vhodná pro: kanceláře, ložnice, obývací pokoj, začátečníky, pet friendly, baby friendly, hodně světla...
    Květináče
        * magnetické, plastové, keramické, hliněné, kovové, betonové, závěsné, truhlíky, zavlažovací...
        * velikost: -6cm, 7-9cm, 10-14cm, 15-19cm, 20-24cm, 25-29cm, 30+cm
    Příslušenství
        * stojánky, baňky,vzpěry, podložky
    Doplňky
        * Substráty, hnojiva, insekticidy
    Nástroje
        * konvičky, rozprašovače, nářadí
    """
    name = CharField(max_length=64, null=False, blank=False)
    description = TextField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.description}"


class ProductCategory(Model):
    """ Rostliny, Květináče, Doplňky """
    name = CharField(max_length=64, null=False, blank=False)
    sub_category = ForeignKey(ProductSubCategory, null=False, on_delete=PROTECT)

    def __str__(self):
        return f"{self.name} - {self.sub_category.name} - {self.sub_category.description}"


class Discount(Model):
    """ Sleva produktu """
    name = CharField(max_length=64, null=False, blank=False)
    description = TextField(max_length=128, null=False, blank=False)
    percent = FloatField(null=False, blank=False)
    active = BooleanField(default=False, null=True, blank=True)
    created_at = DateTimeField(null=False, blank=False)
    modified_at = DateTimeField(null=True, blank=True)
    deleted_at = DateTimeField(null=False, blank=False)

    def __str__(self):
        return f"Sleva {self.percent} %"


class Product(Model):
    """ Produkt """
    name = CharField(max_length=64, null=False, blank=False)
    description = TextField(max_length=128, null=False, blank=False)
    category = ForeignKey(ProductCategory, null=False, on_delete=PROTECT)
    # sub_category = ForeignKey(ProductSubCategory, null=False, on_delete=PROTECT)
    diameter = IntegerField(null=False, blank=False)
    price = FloatField(null=False, blank=False)
    discount = ForeignKey(Discount, null=True, blank=True, on_delete=PROTECT)
    quantity = IntegerField(null=False, blank=False)
    image = ImageField(null=True, blank=True)
    created_at = DateTimeField(null=False, blank=False)
    modified_at = DateTimeField(null=True, blank=True)
    deleted_at = DateTimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.name},  {self.price}, {self.quantity}%"
