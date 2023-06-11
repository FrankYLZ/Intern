from django.shortcuts import render, redirect
from .models import Stock
from datetime import datetime
from django.http import HttpResponseRedirect


# def home(request):
#     return render(request, 'stocks/home.html')


def predict_price(request):
    if request.method == 'POST':
        stock_symbol = request.POST.get('stockSymbol')

        # Here, you'll want to get the date and timezone based on the current date and timezone of the server, or hard-code them.
        # For example:
        date = datetime.now().date()
        timezone = 'America/New_York'
        predicted_price = datetime.now().day
        currency = 'USD'  # This could also be determined dynamically depending on your requirements.

        # save data to database
        # Stock.objects.create(date=date, timezone=timezone, stock_symbol=stock_symbol, predicted_price=predicted_price, currency=currency)
        stock = Stock(date=date, timezone=timezone, stock_symbol=stock_symbol, predicted_price=predicted_price, currency=currency)
        stock.save()
        return redirect('stocks:predict_price')

    # fetch all data from database
    stock_list = Stock.objects.all() # Get all stock data
    context = {'stock_list': stock_list}
    return render(request, 'stocks/predict_price.html', context)


def clear_history(request):
    Stock.objects.all().delete()  # assuming your model is named Stock
    return HttpResponseRedirect('/predict_price/')


