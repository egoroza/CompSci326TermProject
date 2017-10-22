from django.db import models

# Create your models here.
class User(models.Model):
    """
    Model representing a User Account.
    """
    #Fields
    nug_id = models.IntegerField(help_text="Nugget ID unique to User")
    usr = models.CharField(max_length=25, help_text="Username")
    email = models.EmailField(max_length=50, help_text="User Email")
    pswd = models.CharField(max_length=50, help_text="User Password")
    bday = models.DateField(auto_now=True)
    coins = models.IntegerField(help_text="User Currency")
    #Messages & Settings should be their own models ?

    #Metadeta
    class Meta:
        ordering = ["nug_id", "usr", "email", "pswd", "bday", "coins"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of User
        """
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the User object (in Admin site)
        """
        return '%s (%s)' % (self.usr, self.nug_id)


class Nugget(models.Model):
    """
    Model representing a Nugget.
    """
    #Fields
    nug_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=25, help_text="Nugget name")
    #inv=models.ForeignKey('Inventory', on_delete=models.SET_NULL, null=True)
    #atr=models.ForeignKey('Attributes', on_delete=models.SET_NULL, null=True)

    #Metadeta
    class Meta:
        ordering = ["nug_id", "name"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Nugget
        """
        return reverse('nugget-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Nugget
        """
        return self.name


class NuggetAttribute(models.Model):
    """
    Model representing a Nugget's Attributes.
    """
    #Fields
    nug_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    nug_color = models.CharField(max_length =50, help_text="Nugget color")
    nug_size = models.DecimalField(max_digits=25, decimal_places=2)
    mouth_size = models.DecimalField(max_digits=25, decimal_places=2)
    eye_size = models.DecimalField(max_digits=25, decimal_places=2)
    experience = models.IntegerField(help_text="Experience Points")

    mouth_type = (
        ('h', 'Happy'),
        ('n', 'Nervous'),
        ('d', 'displeased'),
        ('hu', 'Hungry'),
    )

    eye_shape = (
        ('w', 'Wide'),
        ('s', 'Small'),
        ('sl', 'Sleepy'),
        ('m', 'Mad'),
    )

    nugget_shape = (
        ('e', 'Egg-like'),
        ('r', 'Round'),
        ('t', 'Triangle'),
        ('s', 'Square'),
    )

    mouth_status = models.CharField(max_length=1, choices=mouth_type, blank=True, default='h', help_text='Type of Nugget Mouth')
    eye_status = models.CharField(max_length=1, choices=eye_shape, blank=True, default='w', help_text='Type of Nugget Eye')
    nugget_status = models.CharField(max_length=1, choices=nugget_shape, blank=True, default='e', help_text='Type of Nugget Shape')

    #Metadata
    class Meta:
        ordering = ["nug_id", "mouth_status", "eye_status", "nugget_status", "experience"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of nugget attributes
        """
        return reverse('nug-attributes-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Nugget attributes
        """
        return self.nug_color

class Inventorie(models.Model):
    """
    Model representing Items and Inventory
    """
    #Fields
    Item_id = models.IntegerField(help_text = "Unique Item ID")
    Item_name = models.CharField(max_length = 50, help_text = "Name of Item(s)")
    Inv_id = models.IntegerField(help_text = "Unique Inventory ID")

    #Metadata
    class Meta:
        ordering = ["Item_id", "Item_name", "Inv_id"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Inventory
        """
        return reverse('Inventory-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Inventory
        """
        return self.Inv_id
