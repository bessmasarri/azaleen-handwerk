from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HandmadeItem
from .forms import HandmadeItemForm

def gallery_view(request):
    items = HandmadeItem.objects.all().order_by('-created_at')
    return render(request, 'gallery.html', {'images': items})

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def dashboard(request):
    if request.method == 'POST':
        form = HandmadeItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HandmadeItemForm()
    
    items = HandmadeItem.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'form': form, 'items': items})

@login_required(login_url='/login/')
def edit_item(request, pk):
    item = get_object_or_404(HandmadeItem, pk=pk)
    if request.method == 'POST':
        form = HandmadeItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HandmadeItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form, 'item': item, 'action': 'Modifier'})

@login_required(login_url='/login/')
def delete_item(request, pk):
    item = get_object_or_404(HandmadeItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return render(request, 'item_confirm_delete.html', {'item': item})
