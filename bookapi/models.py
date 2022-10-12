from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.

class Books(models.Model):
    title=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    options=(
        ("fantasy","fantasy"),
        ("literary","literary"),
        ("mystery","mystery"),
        ("non-fiction","non-fiction"),
        ("science-fiction", "science-fiction"),
        ("thriller","thriller")
    )
    genre=models.CharField(max_length=120,choices=options,default="")
    favourite=models.BooleanField()
    def avg_rating(self):
        all_reviews=self.reviews_set.all()
        if all_reviews:
            total=sum([review.rating for review in all_reviews])
            return total/len(all_reviews)
        else:
            return 0
    def review_count(self):
        return self.reviews_set.all().count()


class Reviews(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])
