from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Добавление тестовых продуктов"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name="кондиционеры")

        products = [
            {
                "name": "Настенный кондиционер Daichi AIR35AVQ1R / AIR35FV1R серии Air",
                "price": 37790.00,
                "category": category,
            },
            {"name": "aeronik", "price": 31300.00, "category": category},
        ]

        for prod in products:
            product, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added book: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Book already exists: {product.name}")
                )
