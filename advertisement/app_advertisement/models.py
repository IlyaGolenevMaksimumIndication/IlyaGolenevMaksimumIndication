from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()
DEFAULT = 'advertisement/to/static/img/adv.png'

class Advertisement(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
    )
    auction = models.BooleanField(
        verbose_name="Торг",
        default=False,
        help_text="Отметьте, если торг уместен!"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата добавления",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата редактирования",
        auto_now=True
    )
    image = models.ImageField(
        verbose_name="Изображение", 
        upload_to="advertisements/",
        default=DEFAULT
        
    )
    
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)


   
def set_image_to_default(self):
        set_image_to_default(save=True)
        self.image = DEFAULT
        self.save()
   
 
    
    
    
    

def __str__(self):
        return f"id = {self.id} title = {self.title} price = {self.price}"
    


@admin.display(description="Дата создания")
def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%C")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%C")
    
    
            

@admin.display(description="Дата редактирования")
def updated_at(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    

@admin.display(description="Мини фотка")
def image_thumbnail(self):
      return format_html('<img src="" />' % (self.image.url))
    
                             
    

class Meta:
        db_table = 'advertisements'

   

 
       
