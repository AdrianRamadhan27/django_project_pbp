from django import forms
from wishlist.models import BarangWishlist
  
  
# creating a form
class WishlistForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = BarangWishlist
  
        # specify fields to be used
        fields = [
            "nama_barang",
            "harga_barang",
            "deskripsi",
        ]

