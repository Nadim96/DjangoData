import csv, io
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import OrderInfo


# Create your views here.

def index(request):
    all_orders = OrderInfo.objects.all()
    return render(request, "Orders/index.html", {'Orders': all_orders})

def EditOrder(request, pk):
    single_order = OrderInfo.objects.get(pk=pk)
    return render(request, "Orders/edit.html", {'Orders': single_order})


def AddOrderForm(request):
    product_name = request.POST.get('product_name', False)
    order_description = request.POST.get('order_description', False)
    order_price = request.POST.get('order_price', False)
    order_amount = request.POST.get('order_amount', False)
    order_date = request.POST.get('order_date', False)

    order_info = OrderInfo(order_name=product_name, order_description=order_description, order_price=order_price, order_amount=order_amount, order_date=order_date)
    order_info.save()
    return HttpResponseRedirect(request.POST.get('index', '/'))

def DeleteOrder(request, pk):

    delete_info = OrderInfo.objects.get(pk=pk)
    delete_info.delete()

    return HttpResponseRedirect(request.POST.get('index', '/'))

def EditOrderForm(request, pk):
    edit_form_data = OrderInfo.objects.get(pk=pk)
    edit_form_data.order_name = request.POST.get('product_name', False)
    edit_form_data.order_description = request.POST.get('order_description', False)
    edit_form_data.order_price = request.POST.get('order_price', False)
    edit_form_data.order_amount = request.POST.get('order_amount', False)
    edit_form_data.order_date = edit_form_data.order_date

    edit_form_data.save()
    return HttpResponseRedirect(request.POST.get('index', '/'))

def UploadCsv(request):
    template = "Orders/upload.html"
    test = "Orders/index.html"

    prompt = {
        'order': "Correct csv order: order_name, order_description, order_price, order_amount, order_date"
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload a csv file.')

    data = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = OrderInfo.objects.update_or_create(
            order_name=column[0],
            order_description=column[1],
            order_price=column[2],
            order_amount=column[3],
            order_date=column[4]
        )
    context = {'order': "csv file has been uploaded!"}
    return render(request, template, context)