from django.shortcuts import render
from django.http import HttpResponse

from dotenv import load_dotenv
import os

from django.shortcuts import render
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

# Create your views here.
# def get_home(request):
#     return render(request, 'pages/home.html')

def get_home(request):
    load_dotenv()

    user = os.getenv('USER_NAME')
    api_key = os.getenv('API_KEY')

    user_info = user if user else "chưa thiết lập"
    api_info = '*' * (len(api_key) - 3) + api_key[-3:] if api_key else "chưa thiết lập"

    context = {
        'account': user_info,
        'api_key': api_info
    }

    return render(request, 'pages/home.html', context)

# def get_home(request):
#     plot_div = None

#     if request.method == "POST":
#         symbol = request.POST.get("symbol")
#         start_date = request.POST.get("start_date")
#         end_date = request.POST.get("end_date")

#         if symbol and start_date and end_date:
#             try:
#                 data = yf.download(symbol, start=start_date, end=end_date)
#                 fig = go.Figure(data=[go.Candlestick(
#                     x=data.index,
#                     open=data['Open'],
#                     high=data['High'],
#                     low=data['Low'],
#                     close=data['Close']
#                 )])
#                 fig.update_layout(title=f'Biểu đồ nến: {symbol}', xaxis_rangeslider_visible=False)
#                 plot_div = fig.to_html(full_html=False)
#             except Exception as e:
#                 plot_div = f"<p style='color:red;'>Lỗi tải dữ liệu: {str(e)}</p>"

#     context = {
#         "account": "Demo Account",
#         "api_key": "***abc",
#         "plot_div": plot_div,
#     }

#     return render(request, 'pages/home.html', context)


def get_env(request):
    info = ""
    user_info = ""
    api_info = ""

    load_dotenv()

    user = os.getenv('USER_NAME')
    api_key = os.getenv('API_KEY')

    if user:
        user_info = user
    else:
        user_info = "chưa thiết lập"

    # Ẩn ký tự
    if api_key:
        api_info = '*' * (len(api_key) - 3) + api_key[-3:]
    else:
        api_info = 'chưa thiết lập'

    info = f"""
            Tài khoản: {user_info} <br> 
            API_KEY: {api_info}
            """

    return HttpResponse(info)
