from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import House, Storage
from srm.models import Lead
from .filters import HouseFilter
from .forms import HouseUpdateForm, HouseCreateForm


@user_passes_test(lambda u: u.status == 2, login_url='/app/index/')
def house_update_view(request, slug):
    house = House.objects.filter(slug=slug).first()

    if request.method == 'POST':
        form = HouseUpdateForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house_detail', house.slug)

    form = HouseUpdateForm(instance=house)

    return render(request, 'app/house_update.html', context={"form": form, "house": house})


def house_detail_view(request, slug):
    house = House.objects.filter(slug=slug).first()

    if 'buy' in request.POST:
        storage = Storage(
            user=request.user,
            house=house
        )
        storage.save()
        return redirect('index')

    return render(request, 'app/house_detail.html', context={'house': house})


@user_passes_test(lambda u: u.status == 2, login_url='/app/index/')
def house_create_view(request):
    if request.method == 'POST':
        form = HouseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = HouseCreateForm()

    return render(request, 'app/house_create.html', context={'form': form})


def house_delete(request, slug):
    house = House.objects.filter(slug=slug).first()
    house.delete()

    return redirect('index')


class HouseListView(ListView):
    model = House
    template_name = 'app/house_list.html'
    context_object_name = 'houses'
    filterset_class = HouseFilter
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = HouseFilter(self.request.GET, queryset=queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter'] = self.filterset

        houses = context["houses"]
        paginator = Paginator(houses, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            houses = paginator.page(page)
        except PageNotAnInteger:
            houses = paginator.page(1)
        except EmptyPage:
            houses = paginator.page(paginator.num_pages)
        context['houses'] = houses

        return context


# Create your views here.
def index(request):
    houses = House.objects.filter(is_active=True)[:6]

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        lead = Lead(
            full_name=name,
            email=email,
            subject_line=subject,
            message=message,

        )
        lead.save()
        redirect('index')

    return render(request, 'app/index.html', context={'houses': houses})






