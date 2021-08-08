from django.db.models import (
    Model, CharField, TextField, ForeignKey, DateTimeField, DecimalField,
    SmallIntegerField, PositiveSmallIntegerField, ImageField,
    PROTECT,
)


class ProductSubCategory(Model):
    """
    Pod-Kategorie produktů:
        Rostliny
            * pokojové, tilandsie, řasokoule, kapradiny, kaktusy a sukulenty, masožravé, orchideje a bromélie, ostatní
            * description: pro kanceláře, ložnice, obývací pokoj, začátečníky, pet friendly, baby friendly, hodně světla
        Květináče
            * magnetické, plastové, keramické, hliněné, kovové, betonové, závěsné, truhlíky, zavlažovací...
            * velikost: do 6cm, 7-9 cm, 10-14 cm, 15-19 cm, 20-24 cm, 25-29 cm, 30+ cm
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
        return f"{self.name} {self.description}"


class ProductCategory(Model):
    """ Kategorie produktů: Rostliny, Květináče, Příslušenství, Doplňky, Nástroje """
    name = CharField(max_length=64, null=False, blank=False)
    sub_category = ForeignKey(ProductSubCategory, null=False, on_delete=PROTECT)

    def __str__(self):
        return f"{self.name} - {self.sub_category.name}"


class Product(Model):
    """ Produkt k prodeji """
    name = CharField(max_length=64, null=False, blank=False)
    description = TextField(max_length=128, null=False, blank=False)
    category = ForeignKey(ProductCategory, null=False, on_delete=PROTECT, related_name="products")
    diameter = SmallIntegerField(null=False, blank=False)
    price = DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    quantity = PositiveSmallIntegerField(null=False, blank=False)  # pridat validator, nesmi byt mensi nez 0
    image = ImageField(null=True, blank=True, upload_to="images/")
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(null=True, blank=True)
    deleted_at = DateTimeField(null=False, blank=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name},  {self.price}, {self.quantity}%"

    @property
    def image_url(self):
        try:
            url = self.image.url
        except ValueError:
            url = ""
        return url
