from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import Lead
from app.models import Storage
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/app/index/')
def lead_list_view(request):
    leads = Lead.objects.all()
    return render(request, 'srm/leads.html', context={'leads': leads})


@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/app/index/')
def lead_delete_view(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect('lead_list')


def storage_list_view(request):
    storages = Storage.objects.filter(status=1)
    total_sum = storages.aggregate(total=Sum('house__price'))['total']
    return render(request, 'srm/orders.html', context={'storages': storages, 'total_sum': total_sum})
